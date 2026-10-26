
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

README = Path("README.md")
START = "<!-- DAILY-UPDATE-START -->"
END = "<!-- DAILY-UPDATE-END -->"


def main():
    content = README.read_text(encoding="utf-8")

    if START not in content or END not in content:
        raise ValueError("Daily update markers are missing.")

    today = datetime.now(
        ZoneInfo("Asia/Kolkata")
    ).strftime("%d %B %Y")

    section = (
        f"{START}\n"
        f"### Profile Last Updated\n"
        f"Last automated profile refresh: **{today}**\n"
        f"{END}"
    )

    start = content.index(START)
    end = content.index(END) + len(END)

    updated = content[:start] + section + content[end:]

    if updated != content:
        README.write_text(updated, encoding="utf-8")
        print(f"README updated: {today}")
    else:
        print("README is already up to date.")


if __name__ == "__main__":
    main()
