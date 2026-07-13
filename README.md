# Easy Auto-Update
Auto-Update shouldn't be hard!

## Features

- Zero dependencies — uses only Python's standard library - no effort 
- Checks the latest GitHub release automatically
- Two versions available:
  - **Auto-update**: downloads and applies the update automatically
  - **Notify-only**: just tells you a new version is available, you decide what to do

## Usage

1. Copy the code from [`autoupdate.py`](./autoupdate.py) into your project
2. Fill in these three values at the top:

```python
GITHUB_USER, GITHUB_REPO, CURRENT_VERSION = "your_username", "your_repo", "v1.0.0"
```

3. Call it somewhere in your script:

```python
check_for_updates()
```

4. Publish releases on GitHub with a `.py` file attached — the script picks up new versions automatically based on the release tag.

## How it works

- Pulls/Fetches the latest release info from the GitHub Releases API
- Compares the release tag with your `CURRENT_VERSION`
- If a newer version exists, downloads the attached `.py` file
- (Optional) Overwrites the currently running script with the new version

## License

Licensed under [PolyForm Noncommercial 1.0.0](./LICENSE) — free for personal, non-commercial use. For commercial use, please contact me first.

## Credit

Made by [YvzSlmDrms54](https://github.com/YvzSlmDrms54). Feel free to use and modify — credit is appreciated but not required.
