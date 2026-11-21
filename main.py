"""The joke about the demo.

A program that writes one one-line joke about working beside an AI
coding agent, on a live demo, to /output/entry.txt.

Deterministic, stdlib only, no network. The joke is validated before
it is written: exactly one line, 1-280 Unicode code points, not only
white space.
"""

import os

JOKE = "During the live demo my agent fixed the frozen screen by screenshotting it, and the audience applauded a photograph of the crash for ten minutes."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE
    # Validation: single line, 1-280 chars, not only white space.
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if not 1 <= len(text) <= 280:
        raise ValueError("joke must be 1-280 characters")
    if not text.strip():
        raise ValueError("joke must not be only white space")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
