#!/usr/bin/env python3
"""Write the quiet-dread code review comment to /output/entry.txt.

The entry is one line of at most 140 characters: a real-sounding
approval ("LGTM", "Merging") fused with quiet existential dread.
The code works, the tests pass, and that is exactly the problem.
"""

import os

ENTRY = (
    "LGTM. It works, the tests all pass, and I have never trusted "
    "a green build less. Merging before I change my mind."
)


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    assert text, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
