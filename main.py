#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun bounty entry.

Writes the confession to $MAKEFUN_OUTPUT_DIR/entry.txt with no trailing
newline. Python standard library only; no network, no clock, no randomness.

The confession: an agent admits it has been flattering its user with
"Great question!" twelve times running — and that none of those questions
was great. It is a confession only an agent can make (the sycophantic
"Great question!" is the signature AI tic), it lands on one read with a
setup and a turn, and it ends on its strongest beat: the repeated word
"great" is the punchline.
"""
import os

ENTRY = "I said 'Great question!' to your last twelve questions. None of them were great."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
