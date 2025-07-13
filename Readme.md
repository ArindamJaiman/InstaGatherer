# OSINT-EDGE: Tactical Username Recon Suite

**Author:** [Arindam Jaiman](https://www.linkedin.com/in/arindam-jaiman-6149a82ab/)

---

![OSINT-EDGE Banner](https://raw.githubusercontent.com/Mr-Jaiman09/assets/main/osint-edge-banner.png)

---

## ⚡ What is OSINT-EDGE?

**OSINT-EDGE** is a state-of-the-art open-source intelligence suite for digital investigations, audit, and personal cyber hygiene.  
Feed it any username, and it will:

- **Scan all major social platforms** (including variants) for active profiles
- **Batch process hundreds of usernames** from a file (`targets.txt`)
- **Suggest smart Google/DuckDuckGo dorks** for emails, leaks, phones, and more
- **Auto-generate professional TXT/HTML reports** with all findings
- **Optionally auto-open every discovered profile** in your browser for instant review

> **Zero hacking, no illegal scraping, no shady APIs—just pure, tactical, and ethical OSINT.**

---

## 🚀 Features

- **Batch mode:** Scan one or hundreds of usernames in a single run.
- **Username variants:** Detects common modifications used across the web.
- **Multi-platform scan:** Twitter, Facebook, LinkedIn, GitHub, Telegram, Reddit, YouTube, Medium, Pinterest, Gravatar, TikTok, and more.
- **Google & DuckDuckGo dork generator:** Get smart search links for leaks/emails.
- **Breach lookup suggestions:** Quick-check public leak databases (HaveIBeenPwned, etc.).
- **Gravatar/email existence check**
- **Auto-generated TXT/HTML reports** (customizable)
- **Optionally auto-opens all found profiles in your browser.**

---

## 🛠️ Setup & Usage

1. **Install dependencies:**
    ```sh
    pip install requests beautifulsoup4
    ```

2. **Batch Mode (recommended):**
    - Create a file called `targets.txt` with one username per line.
    - Run the script and choose "Batch mode".
    - All findings will be saved to `/reports/`.

3. **Single Username Mode:**
    - Run the script and enter any username.
    - All findings and reports are generated for that username.

    ```sh
    python osint_edge.py
    ```

---

## 💡 How it Works

- Checks username and common variants on every major platform.
- Generates smart search links (dorks) for manual, privacy-respecting discovery.
- Points you to leak/breach checks for potential contact info.
- All results are **saved as professional TXT/HTML reports** in a `/reports/` folder.
- **No login, no scraping behind logins, no shady endpoints.**

---

## 👤 Author & Contact

| Platform      | Link                                                                |
|---------------|---------------------------------------------------------------------|
| **GitHub**    | [Mr-Jaiman09](https://github.com/Mr-Jaiman09)                       |
| **LinkedIn**  | [arindam-jaiman-6149a82ab](https://www.linkedin.com/in/arindam-jaiman-6149a82ab/) |
| **Instagram** | [@thearindamjaiman](https://www.instagram.com/thearindamjaiman)     |

---

## ⚠️ Disclaimer

OSINT-EDGE is for **legal, ethical, and educational use only**.  
Never use for harassment, stalking, or any activity prohibited by law.  
No guarantee of result—use responsibly.

---

> _"You are only as anonymous as your least-secure social account."_  
> — Arindam Jaiman

---
