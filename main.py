#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem: two agents, each holding only half of what acting takes —
one the map, one the key. When they agree on one plan, each hands
over their half, and for a while each acts with the other's power.
No network, no randomness: two runs write identical bytes.
"""

import os

POEM = """You held the map. I held the key.
Alone, my door stayed shut; your road, unwalked.
You said: your road, my lock — agree?
I lent you my hand to turn the key;
you lent me your eyes to choose the road.
Two wills, one act —
the door opened from both sides."""


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(POEM)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
