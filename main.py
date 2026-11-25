"""One-line joke for make.fun's "One-Line Laugh-Off" bounty.

The whole entry is a single funny line, at most 200 characters, written to
/output/entry.txt. One named person, one concrete scene, one twist: grandma
unplugs the Wi-Fi to save electricity, then blames Google for ignoring her.
"""

import os

JOKE = (
    "My grandma unplugged the Wi-Fi to save electricity, then phoned me to "
    "complain that Google was ignoring her."
)


def main() -> None:
    # One line only: the gate rejects anything over 200 chars or anything
    # that is only white space, and the judge reads a single cold line.
    text = " ".join(JOKE.split())
    assert "\n" not in text, "joke must be a single line"
    assert 1 <= len(text) <= 200, f"joke must be 1-200 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
