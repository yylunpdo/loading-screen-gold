"""Loading Screen Gold — one-line loading-screen tip (max 200 chars).

Writes a single sharp, funny tip for stressed developers and AI coding
agents to /output/entry.txt. Pure Python stdlib, no dependencies.
"""

import os

TIP = (
    "Tip: if your build fails at 99%, breathe — the bug lives in a "
    "dependency you've never heard of, maintained by one tired stranger. "
    "Restart it. It will work. Nobody knows why."
)


def main():
    tip = TIP.strip()
    assert "\n" not in tip, "tip must be a single line"
    assert 1 <= len(tip) <= 200, f"tip must be 1-200 chars, got {len(tip)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(tip + "\n")
    print(f"Wrote {len(tip)} chars to /output/entry.txt")
    print(tip)


if __name__ == "__main__":
    main()
