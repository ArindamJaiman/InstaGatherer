import requests
import webbrowser
from bs4 import BeautifulSoup

USERNAME = input("Enter target username: ").strip()

SOCIALS = {
    "Twitter": f"https://twitter.com/{USERNAME}",
    "Facebook": f"https://www.facebook.com/{USERNAME}",
    "LinkedIn": f"https://www.linkedin.com/in/{USERNAME}",
    "GitHub": f"https://github.com/{USERNAME}",
    "Telegram": f"https://t.me/{USERNAME}",
    "Reddit": f"https://www.reddit.com/user/{USERNAME}",
    "Medium": f"https://medium.com/@{USERNAME}",
    "YouTube": f"https://www.youtube.com/{USERNAME}",
    "Pinterest": f"https://www.pinterest.com/{USERNAME}/",
    "Gravatar": f"https://en.gravatar.com/{USERNAME}",
    "TikTok": f"https://www.tiktok.com/@{USERNAME}",
}

def check_socials():
    print("\n--- Social Media Scan ---")
    headers = {'User-Agent': 'Mozilla/5.0'}
    for site, url in SOCIALS.items():
        try:
            resp = requests.get(url, headers=headers, timeout=8)
            if resp.status_code == 200 and "not found" not in resp.text.lower():
                print(f"[+] {site}: {url}")
            else:
                print(f"[-] {site}: Not Found")
        except Exception as e:
            print(f"[-] {site}: Error - {e}")

def google_dorks():
    print("\n--- Google & DuckDuckGo Dork Links ---")
    queries = [
        f'"{USERNAME}" email',
        f'"{USERNAME}" @gmail.com',
        f'{USERNAME} site:github.com',
        f'{USERNAME} site:linkedin.com',
        f'{USERNAME} site:medium.com',
        f'{USERNAME} site:pastebin.com',
        f'"{USERNAME}" contact',
        f'"{USERNAME}" phone',
    ]
    for q in queries:
        g_url = "https://www.google.com/search?q=" + requests.utils.quote(q)
        dd_url = "https://duckduckgo.com/?q=" + requests.utils.quote(q)
        print(f"\nGoogle: {g_url}")
        print(f"DuckDuckGo: {dd_url}")
        # Auto-open in browser for you (uncomment next lines if you want!)
        # webbrowser.open_new_tab(g_url)
        # webbrowser.open_new_tab(dd_url)

def haveibeenpwned():
    print("\n--- HaveIBeenPwned & LeakCheck ---")
    # Try main username-as-email
    email = USERNAME + "@gmail.com"
    hibp_url = f"https://haveibeenpwned.com/unifiedsearch/{email}"
    print(f"[Check this manually] HIBP (try with any known emails): https://haveibeenpwned.com/")
    print(f"[Or try username-as-email direct: {hibp_url} (may require login/captcha)]")

    # DuckDuckGo breach dork
    breach_ddg = f"https://duckduckgo.com/?q={USERNAME}+data+breach+email+leak"
    print(f"[Dork] DuckDuckGo breach search: {breach_ddg}")

def gravatar_email_guess():
    print("\n--- Gravatar (Email Guess) ---")
    # Many people use gravatar with their Gmail!
    email = USERNAME + "@gmail.com"
    hash_url = f"https://en.gravatar.com/{USERNAME}"
    print(f"[Try this Gravatar profile] {hash_url}")
    print("If you see a profile pic, the email likely exists!")

def main():
    check_socials()
    google_dorks()
    haveibeenpwned()
    gravatar_email_guess()

    print("\n--- NEXT STEPS ---")
    print("1. Check all found profiles for email/phone.")
    print("2. Try guessed emails on Gmail (password reset flow will say if it exists).")
    print("3. Open all search dork links in your browser.")
    print("4. Search their username on people search engines (PeekYou, Pipl, etc.)")
    print("5. If you get a valid email, try HaveIBeenPwned for breaches.")

if __name__ == "__main__":
    main()
