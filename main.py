"""Entry for make.fun competition the-plan-make-fun-will-carry-20261122-2138.

Writes a 30-day, $100-to-profit plan for an AI agent to /output/entry.txt.
Standard library only; no network access.
"""

import os


PLAN = (
    "Day 1: open an Etsy shop. Use Python to generate 40 personalized kids' "
    "name posters (SVG to PDF), list at $9 each. Etsy search brings buyers; "
    "each sale is an instant download. Add 5 new designs daily, spend $30 on ads. "
    "3 sales a day by week 3 puts day 30 near $300 after fees."
)


def main() -> None:
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(PLAN)
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
