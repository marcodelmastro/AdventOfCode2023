# Advent Of Code 2023

* [Day 1](Day01.ipynb). String manipulation with not-so-trivial twist for Part 2.

* [Day 2](Day02.ipynb). First tricky input parsing (if only I resolved to learn `regex`!). List comparison by element (`map`, `all`) in Part 1, matrix rotation with `numpy` in Part 2.

* [Day 3](Day03.ipynb). Ok, today I really needed regular expression! I learned `re.finditer` and that basically solved most of the problem! Part 2 came almost for free from Part1.

* [Day 4](Day04.ipynb). More `regex` to parse the input, `set` intersections to process card value overlaps.

* [Day 5](Day05.ipynb). First use of a `class` of the year. Part 1 relatively easy, Part 2 introduces the usual explosion of the phase space that makes brute forcing the solution not a viable option (even if it's still feasible with `pypy`. Using ranges is the way to go, and instead of coding my own class with overlap removal and slicing methods, I used the nice `IntervalTree` package!

* [Day 6](Day06.ipynb). Part 1 can be solved with a simple scan, but there's an analytical solution that works perfectly for both parts.

* [Day 7](Day07.ipynb). Custom `compare` functions to be used with sorting algorithm using `functools.cmp_to_key()`.
