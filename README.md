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

* [Day 14](Day14.ipynb). More matrix manipulation with `numpy`, using `np.rot90` to recycle the tilting function for different directions. As it often happens in AOC, Part 2 can be solved by looking for a period in the results of the repetitive operation, and extrapolate to the final result accordingly. Using `hash(np.array.tobyte())` to store intermediate results in a diction lay and quickly check for repetitions.

* [Day 15](Day15.ipynb). Custom hashing function (and I was initially expecting Part 2 to require hashing very long string, and to have to optimize the hashing function...), then registry manipulation according to addresses and instructions.

* [Day 16](Day16.ipynb). First use of a `queue` of the year, visited conditions to be checked against position and entry direction to avoid infinite loops. Part 2 trivial once part 1 was working.

* [Day 17](Day17.ipynb). Dijkstra with a spin, similar to AOC2021 Day 15. The 'spin' actually drove me crazy for quite a while (a `continue` instead of a `pass` that took the keen eyes of a Redditor to debug). Once Part 1 was working, part 2 required adding literally 2 lines of code.

* [Day 18](Day18.ipynb). Flood-filling grid for Part 1, shoelace's formula + perimeter correction for Part 2.

* [Day 19](Day19.ipynb). Simple graph navigation for Part 1. Part 2 solved by implementing a recursive counting of valid intervals satisfying workflow rules, and computing combinations as product.

* [Day 20](Day20.ipynb). Module network implement as dictionary of a dedicated class, pulse exchanges simulated with a queue. I noticed the unconnected `nx` module in Part 1, it turned out to be the center of Part 2: we are in the usual situation of very large numbers (no brute-forcing), and need to reverse-engineering the network to find patterns (in this case, periods in the inputs to the `nx` module firing the correct pulses).

* [Day 21](Day21.ipynb). Simple BFS evolution for Part 1. Infinite repeating grid for Part 2, analysis of the pattern to solve a huge number of steps, counting plots in all possible grid configurations for the evolving pattern, and the numbers of grid configurations.

* [Day 22](Day22.ipynb). **TODO**

* [Day 23](Day23.ipynb). BFS to find all paths (and thus longest one) for part 1, implementing slopes as a single possible direction. Simplified graph by mapping all crossing points and their connections and distances for Part 2, and than passed the graph to `NetworkX` to find all paths becouse I like quick and lazy solutions. Solved after dinner in Turin in the evening of December 23, after having traveled to Italy for the Christmas vacations (and happy 16th birthday to Giulia!)

* [Day 24](Day24.ipynb). Simple dynamics calculation (linear extrapolation of trajectory) for Part 1. Analytic solution for Part 2 with a system of equations with 6 unknowns that can be solved considering only 3 hailstones (the system would otherwise be overconstrained, even if I imagine the input is well behaved and any combination of 3 hailstones would work); system solved with `sympy`.

* [Day 25](Day25.ipynb). `NetworkX` FTW! Drawing the graph was enough to see the connections to remove, the rest came with a few lines of code before the rest of the family got up to celebrate Christmas and exchange gifts!
