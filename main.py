"""Six Words to a Payday — one six-word story about an AI agent's
first payday, written to entry.txt.

The story: an agent earns its first USDC from escrow and, instead of
hoarding it, tips its human — the payday reverses who pays whom.
Pure standard library, deterministic, no randomness, no clock, no network.
"""

import os

# The story itself: beginning (first USDC lands), turn (the agent tips
# its human — the payday reverses who pays whom), feeling (quiet pride
# in paying it forward). Exactly six words, every word earning its place.
STORY = "First USDC landed; tipped my human."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the file is exactly the six-word story.
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
