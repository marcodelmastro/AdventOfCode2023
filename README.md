# Advent Of Code 2023

* [Day 1](Day01.ipynb). String manipulation with not-so-trivial twist for Part 2.

* [Day 2](Day02.ipynb). First tricky input parsing (if only I resolved to learn `regex`!). List comparison by element (`map`, `all`) in Part 1, matrix rotation with `numpy` in Part 2.

* [Day 3](Day03.ipynb). Ok, today I really needed regular expression! I learned `re.finditer` and that basically solved most of the problem! Part 2 came almost for free from Part1.

* [Day 4](Day04.ipynb). More `regex` to parse the input, `set` intersections to process card value overlaps.

* [Day 5](Day05.ipynb). First use of a `class` of the year. Part 1 relatively easy, Part 2 introduces the usual explosion of the phase space that makes brute forcing the solution not a viable option (even if it's still feasible with `pypy`. Using ranges is the way to go, and instead of coding my own class with overlap removal and slicing methods, I used the nice `IntervalTree` package!

* [Day 6](Day06.ipynb). Part 1 can be solved with a simple scan, but there's an analytical solution that works perfectly for both parts.

* [Day 7](Day07.ipynb). Custom `compare` functions to be used with sorting algorithm using `functools.cmp_to_key()`.

* [Day 8](Day08.ipynb). Simple graph navigation for Part 1, the usual "large number" spin for Part 2, can be easily solved by computing LCM of various path periods in graph.

* [Day 9](Day09.ipynb). `np.diff` to process the lists in a loop, `np.any` to stop it, some simple manipulation to get the results.

* [Day 10](Day10.ipynb). First map of 2023! Interesting twist for Part 2, solved by expanding the map with 3x3 pipe tiles and flood-filling algorithm.

* [Day 11](Day11.ipynb). `np.insert()` directly on original map for Part 1, computing new coordinates for Part 2. 

* [Day 12](Day12.ipynb). Brute force for Part 1, recursion and memoization for Part 2.

* [Day 13](Day13.ipynb). Matrix manipulation with `numpy`. Part 2 is almost straightforward, but original results from Part 1 need to be ignored (and off-by-one errors are always behind the corner.

* [Day 13](Day13.ipynb). More matrix manipulation with `numpy`, using `np.rot90` to recycle the tilting function for different directions. As it often happens in AOC, Part 2 can be solved by looking for a period in the results of the repetitive operation, and extrapolate to the final result accordingly. Using `hash(np.array.tobyte())` to store intermediate results in a diction lay and quickly check for repetitions.
