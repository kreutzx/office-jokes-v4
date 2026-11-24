"""Make the AI Judge Laugh: Office Jokes - make.fun entry.

One line: Dana from Finance books a 'quick sync' for 15 minutes; the
meeting outlives quarters, grows its own agenda, and finally promotes
itself to 'All-Hands' - one character, one scene, one escalation.
"""

import os

ENTRY_TEXT = "Dana from Finance booked a 'quick sync' for 15 minutes; the calendar invite is now in its third quarter and has its own agenda. Last week it promoted itself to 'All-Hands.'"


def main():
    # One-line office joke; keep it within the competition's line limit.
    assert "\n" not in ENTRY_TEXT and ENTRY_TEXT.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
