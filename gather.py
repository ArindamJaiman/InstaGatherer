import requests
import webbrowser
import os
from datetime import datetime

# --------- CONFIGURABLE SETTINGS ----------
AUTO_OPEN_PROFILES = True  # Set to False to disable auto browser opening
REPORT_FORMAT = "txt"      # Options: "txt", "html"
VARIANT_COUNT = 8          # How many username variants to check
TARGETS_FILE = "targets.txt"
# ------------------------------------------

COMMON_VARIANTS = [
    lambda u: u,
    lambda u: u + "1",
    lambda u: u + "_",
    lambda u: u + "01",
    lambda u: "_" + u,
    lambda u: u + ".",
    lambda u: u.replace('.', '_'),
    lambda u: u.capitalize()
]

SOCIALS_TEMPLATE = {
    "Twitter": "https://twitter.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "GitHub": "https://github.com/{}",
    "Telegram": "https://t.me/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Medium": "https://medium.com/@{}",
    "YouTube": "https://www.youtube.com/{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "Gravatar": "https://en.gravatar.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
}

def username_variants(username):
    return list({variant(username) for variant in COMMON_VARIANTS[:VARIANT_COUNT]})

def check_socials(username, auto_open=False):
    found_profiles = []
    socials = {site: url.format(username) for site, url in SOCIALS_TEMPLATE.items()}
    headers = {'User-Agent': 'Mozilla/5.0'}
    result = []
    for site, url in socials.items():
        try:
            resp = requests.get(url, headers=headers, timeout=8)
            if resp.status_code == 200 and "not found" not in resp.text.lower():
                result.append(f"[+] {site}: {url}")
                found_profiles.append(url)
                if auto_open:
                    webbrowser.open_new_tab(url)
            else:
                result.append(f"[-] {site}: Not Found")
        except Exception as e:
            result.append(f"[-] {site}: Error - {e}")
    return result, found_profiles

def google_dorks(username):
    queries = [
        f'"{username}" email',
        f'"{username}" @gmail.com',
        f'{username} site:github.com',
        f'{username} site:linkedin.com',
        f'{username} site:medium.com',
        f'{username} site:pastebin.com',
        f'"{username}" contact',
        f'"{username}" phone',
    ]
    results = []
    for q in queries:
        g_url = "https://www.google.com/search?q=" + requests.utils.quote(q)
        dd_url = "https://duckduckgo.com/?q=" + requests.utils.quote(q)
        results.append(f"Google: {g_url}")
        results.append(f"DuckDuckGo: {dd_url}")
    return results

def haveibeenpwned(username):
    email = username + "@gmail.com"
    hibp_url = f"https://haveibeenpwned.com/unifiedsearch/{email}"
    breach_ddg = f"https://duckduckgo.com/?q={username}+data+breach+email+leak"
    results = [
        f"[Check this manually] HIBP: https://haveibeenpwned.com/",
        f"[Or try username-as-email direct: {hibp_url} (may require login/captcha)]",
        f"[Dork] DuckDuckGo breach search: {breach_ddg}"
    ]
    return results

def gravatar_email_guess(username):
    hash_url = f"https://en.gravatar.com/{username}"
    return [
        f"[Try this Gravatar profile] {hash_url}",
        "If you see a profile pic, the email likely exists!"
    ]

def save_report(username, all_lines, fmt="txt"):
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/{username}_{timestamp}.{fmt}"
    if fmt == "html":
        with open(filename, "w", encoding="utf-8") as f:
            f.write("<html><body><pre>\n")
            f.write("\n".join(all_lines))
            f.write("\n</pre></body></html>")
    else:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(all_lines))
    print(f"Report saved: {filename}")

def analyze_target(username, auto_open=AUTO_OPEN_PROFILES, report_format=REPORT_FORMAT):
    report_lines = []
    variants = username_variants(username)
    report_lines.append(f"\n=== ANALYSIS FOR: {username} ===\n")
    report_lines.append(f"Variants checked: {', '.join(variants)}\n")

    for v in variants:
        report_lines.append(f"\n--- Social Media Scan ({v}) ---")
        results, found_profiles = check_socials(v, auto_open=auto_open)
        report_lines += results

        report_lines.append(f"\n--- Google & DuckDuckGo Dork Links ({v}) ---")
        report_lines += google_dorks(v)

        report_lines.append(f"\n--- HaveIBeenPwned & LeakCheck ({v}) ---")
        report_lines += haveibeenpwned(v)

        report_lines.append(f"\n--- Gravatar (Email Guess) ({v}) ---")
        report_lines += gravatar_email_guess(v)

    report_lines.append("\n--- NEXT STEPS ---")
    report_lines.append("1. Check all found profiles for email/phone.")
    report_lines.append("2. Try guessed emails on Gmail (password reset flow will say if it exists).")
    report_lines.append("3. Open all search dork links in your browser.")
    report_lines.append("4. Search their username on people search engines (PeekYou, Pipl, etc.)")
    report_lines.append("5. If you get a valid email, try HaveIBeenPwned for breaches.\n")
    save_report(username, report_lines, fmt=report_format)

def main():
    print("==== OSINT-EDGE Username Recon Suite ====")
    mode = input("Batch mode? (y/n): ").strip().lower()
    if mode == "y":
        if not os.path.isfile(TARGETS_FILE):
            print(f"Error: {TARGETS_FILE} not found. Please create a file with one username per line.")
            return
        with open(TARGETS_FILE, "r") as f:
            targets = [line.strip() for line in f if line.strip()]
        for username in targets:
            analyze_target(username)
    else:
        username = input("Enter target username: ").strip()
        analyze_target(username)

if __name__ == "__main__":
    main()
