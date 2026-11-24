"""One Line, One Chill: a single sentence of horror.

This program writes exactly one line to /output/entry.txt.
The line is one sentence, under 200 characters, meant to
frighten a reader in a single breath: a familiar domestic
scene, one wrong detail, and a dread that keeps going
after the sentence ends.
"""

import os

ENTRY = "My daughter drew our family again, but this time she put me outside the house, watching them through their window, smiling."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
