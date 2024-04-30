#! /usr/bin/env python3

import sys
import argparse
from copy import deepcopy
from queue import deque

def shortest_path_length(graph):
    q = deque([(0, 0, 0)])
    visited = set()

    while q:
        i, j, length = q.popleft()

        if i == len(graph)-1 and j == len(graph[-1])-1:
            return length
        
        if (i, j) in visited:
            continue

        visited.add((i, j))

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < len(graph) and 0 <= nj < len(graph[ni]) and (ni, nj) not in visited:
                q.append((ni, nj, length + 1))
    
    return -1

def evaluate_path(graph, path):
    if len(graph) == 0 or len(graph[0]) == 0:
        print("❓ Empty graph", file=sys.stderr)
        return False, []

    expected_length = shortest_path_length(graph)
    if expected_length == -1:
        print("❗ There is no path from top left to bottom right in this graph")
    if len(path) < expected_length:
        print(f"❕ Path is too short (expected {expected_length} but got {len(path)})")
    elif len(path) > expected_length:
        print(f"❕ Path is too long (expected {expected_length} but got {len(path)})")

    out_graph = deepcopy(graph)
    i = 0
    j = 0
    if graph[i][j] == '#':
        out_graph[i][j] = 'T'
    else:
        out_graph[i][j] = 'X'
        print(f"🤯 Timmy falls into the water at spawn ({i}, {j})")
        return False, out_graph
    
    for index in range(len(path)):
        if path[index] == 'R':
            j += 1
        elif path[index] == 'D':
            i += 1
        elif path[index] == 'L':
            j -= 1
        elif path[index] == 'U':
            i -= 1
        else:
            print(f"🧭 Invalid direction at position {index} (wtf is {path[index]} ?)")
            return False, out_graph
        
        if i < 0 or i >= len(graph) or j < 0 or j >= len(graph[i]):
            print(f"😱 Timmy falls out of bounds at coordinnates ({i}, {j})")
            return False, out_graph

        if graph[i][j] == '#':
            out_graph[i][j] = 'T'
        else:
            out_graph[i][j] = 'X'
            print(f"🥶 Timmy falls into the water at coordinnates ({i}, {j})")
            return False, out_graph

    result = False
    if i == len(graph)-1 and j == len(graph[-1])-1:
        result = True
    
    return result, out_graph


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="evaluate_path",
        description="Test if a path is valid for the given input for the 5th problem")
    parser.add_argument(
        "INPUT_FILE", help="input file, the graph to test the path on", action="store", type=str)
    parser.add_argument(
        "PATH_FILE", help="path file, the path to evaluate", action="store", type=str)
    parser.add_argument(
        "OUTPUT_FILE", help="output file, file to write the out-graph with the path displayed to (T for valid squares, X for invalid squares)",
        action="store", type=str, nargs="?")
    
    args = parser.parse_args()
    INPUT_FILE = args.INPUT_FILE
    PATH_FILE = args.PATH_FILE
    OUTPUT_FILE = args.OUTPUT_FILE

    try:
        inputfile = open(INPUT_FILE, "r")
    except (OSError, IOError):
        print(f"Error: {INPUT_FILE}: cannot read input file", file=sys.stderr)
        exit(1)
    
    try:
        pathfile = open(PATH_FILE, "r")
    except (OSError, IOError):
        print(f"Error: {PATH_FILE}: cannot read path file", file=sys.stderr)
        exit(1)
    
    graph = [list(line[:-1]) for line in inputfile.readlines()]
    path = [line[:-1] for line in pathfile.readlines()]
    
    result, out_graph = evaluate_path(graph, path)

    if result:
        print("✅ Valid path")
    else:
        print("❌ Invalid path")
    

    if OUTPUT_FILE:
        try:
            outfile = open(OUTPUT_FILE, "w")
        except (OSError, IOError):
            print(f"Error: {OUTPUT_FILE}: cannot open output file", file=sys.stderr)
            exit(1)

        for line in out_graph:
            outfile.write("".join(line))
            outfile.write("\n")
        
        print(f"🗺️  Wrote out-graph to {OUTPUT_FILE}")
