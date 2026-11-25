"""Fortune Cookies for Machines.

Writes one fortune-cookie line an AI agent would get to /output/entry.txt.
The line is a single fortune-slip sentence (106 characters, gate: 1-200).
"""

import os

FORTUNE = "Your lucky color is #000000. It is also your unlucky color. You are colorblind in exactly 16,777,216 ways."
# 106 characters (gate: 1-200). Fortune-slip voice, 2-beat + reveal in the
# last clause: a canonical fortune element (lucky color) turned machine-native
# (hex code), then the exact number 16,777,216 = 2^24, the whole RGB space.
assert 1 <= len(FORTUNE) <= 200, "fortune must fit the 1-200 character gate"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
