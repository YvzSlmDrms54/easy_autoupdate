# Just Copy-Paste this inside of your project! It's super easy to auto-update! (make sure to fill the blanks text!)
# Made by YvzSlmDrms54 — keep this comment and credit me if you want, remove it if you don't, no hard feelings either way!
# Licensed under PolyForm Noncommercial 1.0.0 — free for personal/non-commercial use, contact me for commercial use.
# Official download for this code : github.com/easy_autoupdate

import os, json, shutil, urllib.request as u

# >>> fill these in for your project <
GITHUB_USER, GITHUB_REPO, CURRENT_VERSION = "YOUR_USERNAME", "YOUR_REPO", "vX.X.X" # Update CURRENT_VERSION before releasing

def check_for_updates():
    # ask GitHub for the latest release info
    try:
        req = u.Request(f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/releases/latest", headers={"User-Agent": "x"})
        data = json.loads(u.urlopen(req, timeout=10).read())
    except Exception as e:
        return print(f"Update check failed: {e}")

    if data["tag_name"] == CURRENT_VERSION:
        return print(f"Already up to date! ✔ ({CURRENT_VERSION})")

    # pick the .py file from the release, or the only file if there's just one
    assets = data.get("assets", [])
    asset = next((a for a in assets if a["name"].endswith(".py")), assets[0] if len(assets) == 1 else None)
    if not asset:
        return print("No suitable file found in release assets.")

    # download it in chunks to ./downloads/
    print(f"New version {data['tag_name']} found, downloading...")
    target = f"./downloads/{asset['name']}"
    os.makedirs("./downloads", exist_ok=True)
    with u.urlopen(u.Request(asset["browser_download_url"], headers={"User-Agent": "x"})) as r, open(target, "wb") as f:
        shutil.copyfileobj(r, f)
    print(f"Downloaded {asset['name']}! ✔")

    # overwrite the currently running script with the new one
    shutil.copy(target, os.path.abspath(__file__))
    print("Update applied. Restart to take effect.")