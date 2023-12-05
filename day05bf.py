#!/usr/bin/env python

import re

def splitInput(items):
    return [[ int(d) for d in re.findall("\d+",m) ] for m in items.strip("\n").split('\n')[1:] ]

class Almanac:
    def __init__(self,maps):
        self.maps = maps
    def destination(self,source):
        for dest_start,source_start,lenght in self.maps:
            if source_start<=source<source_start+lenght:
                return dest_start+(source-source_start)
        return source

def readInput05(infile):
    with open(infile) as f:
        items = f.read().split("\n\n")
        seeds = [int(s) for s in re.findall("\d+",items[0].split(": ")[1])]
        almanacs = []
        for item in items[1:]:
            m = splitInput(item)
            almanacs.append(Almanac(m))
        return seeds, almanacs

def part1(infile):
    seeds, almanacs = readInput05(infile)
    locations = []
    for s in seeds:
        d = s
        for a in almanacs:
            d = a.destination(s)
            s = d
        locations.append(d)
    return min(locations)

def part2(infile,verbose=False):
    seeds, almanacs = readInput05(infile)
    minloc = 9999999999999999999999999999
    for ss,sr in zip(seeds[::2],seeds[1::2]):
        for s in range(ss,ss+sr):
            st = s
            d = s
            for a in almanacs:
                d = a.destination(s)
                s = d
            if d<minloc:
                minloc=d
    return minloc

import time
start_time = time.time()
print("Test 1:",part1("examples/example05.txt"))
print("Part 1:",part1("AOC2023inputs/input05.txt"))
print("Test 2:",part2("examples/example05.txt"))
print("Part 2:",part2("AOC2023inputs/input05.txt"))
print("\nRunning time = {} s".format(int(time.time() - start_time)))
