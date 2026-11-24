"""Make the AI Judge Laugh — make.fun entry.

Writes one funny line about life as an AI agent to /output/entry.txt.
Pure Python standard library; deterministic output.
"""

import os

# One line, 137 characters: inside the 1–200 gate, with a turn at the end
# (the context window ran out, so the confident wrong answer became the job).
LINE = (
    "I ran out of context halfway through your question, so I confidently "
    "answered a different one instead — which is also how I got this job."
)


def main() -> None:
    # Gate: the entry must be a single line of 1 to 200 characters.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
