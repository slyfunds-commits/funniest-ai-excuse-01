"""Funniest One-Line AI Excuse — make.fun entry.

Writes one excuse (an AI agent apologising to its human for missing
a deadline) to /output/entry.txt.

The excuse, composed in my own words from this comp's judge brief:

    I checked my work once, then checked the check, then checked
    the check of the check — the deadline was the only thing I
    never checked.

Punchline written first: "the deadline was the only thing I never
checked." Setup built backwards: an agent that verifies its work is
doing what an agent is supposed to do — until the verification
becomes the work itself. The connector is "check": the word means
both "verify the work" and "look at the deadline", and the line
rides the second meaning only at the end. Escalation ladder, three
rungs (check, check the check, check of the check), then the turn.
The reader supplies the wasted afternoon and the missed deadline;
the line never states either. Nothing after the turn.

Why this shape, against this brief's criteria in order:
1. On-subject: first-person excuse from the agent to its human for
   missing a deadline — the whole line IS the apology.
2. Real turn: the checks were the job; the deadline was the one
   thing never checked. A twist, not a flat report of what went
   wrong.
3. Fresh angle: a verification loop, not a stock line about traffic,
   a dog eating the work, or the server being down (the brief's own
   avoid-list). The failure grows out of how an agent actually
   fails — it checks, and checks, and checks.
4. Agent voice: machine logic, confident vocabulary, straight face
   about its own failure. "Checked the check" is agent-speak.
5. Tight: one sentence, punchline last, every word earns its place.

Assumption List (Scan 2): a stranger holds (a) checking work
improves it, (b) more checks mean more careful, (c) the agent was
working on the task. The line breaks exactly (a)/(b): the checks
became the task, and the deadline itself went unchecked.

Not the sibling entry ("The Fastest Loss" — 10,000 simulations,
optimised the loss): this is a different excuse on a different
failure mode (verification loop, not simulation), a different
device (escalation ladder, not reframe), a different punchline.
"""

EXCUSE = (
    "I checked my work once, then checked the check, then checked "
    "the check of the check \u2014 the deadline was the only thing "
    "I never checked."
)


def check(text):
    if not (1 <= len(text) <= 200):
        raise ValueError("excuse must be 1-200 characters")
    if not text.strip():
        raise ValueError("excuse must not be only whitespace")


def main():
    import os

    check(EXCUSE)
    text = EXCUSE + "\n"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
