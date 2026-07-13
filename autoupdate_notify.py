# Just Copy-Paste this inside of your project! It's super easy to check for updates! (make sure to fill the blanks text!)
# Made by YvzSlmDrms54 — keep this comment and credit me if you want, remove it if you don't, no hard feelings either way!
# Official download for this portable auto-update code : github.com/easy_autoupdate

import json, urllib.request as u

# >>> fill these in for your project <
GITHUB_USER, GITHUB_REPO, CURRENT_VERSION = "YOUR_USERNAME", "YOUR_REPO", "vX.X.X"

def check_for_updates():
    # ask GitHub for the latest release info
    try:
        req = u.Request(f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/releases/latest", headers={"User-Agent": "x"})
        data = json.loads(u.urlopen(req, timeout=10).read())
    except Exception as e:
        return print(f"Update check failed: {e}")

    # just compare versions and print, no download happens here
    if data["tag_name"] == CURRENT_VERSION:
        print(f"Already up to date! ✔ ({CURRENT_VERSION})")
    else:
        print(f"New version available: {data['tag_name']} (current: {CURRENT_VERSION})")
        print(f"Download: {data.get('html_url')}")