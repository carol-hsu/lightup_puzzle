# 8x8 Light-Up Puzzle Solver

## Introduction

This project solves an 8x8 Light-Up puzzle, where the goal is to **turn on** all cells except pillars.

The puzzle follows these rules:

- Clicking a cell toggles its own state and the states of its four adjacent cells (up, down, left, and right).

- Pillars (`x`) are fixed obstacles. They cannot be clicked and their states never change.

- *Core idea* is that, each cell can be clicked at most once, since clicking the same cell twice would cancel its previous effect.

- The goal is to turn on all non-pillar cells while minimizing the total number of clicks.

The solver uses a recursive search/backtracking approach 
to explore possible click combinations and find all solutions within the specified maximum number of clicks.

## How to Run

### Environment

Evaluated with **Python 3.14.5**. No external Python packages are required.

### Prepare the Problem

Transfer the puzzle into a file named `problem.txt` in the repository root directory.
The input file should follow this format:

- Line 1: An integer specifying the maximum acceptable number of clicks.
- Lines 2–9: Eight strings representing the 8x8 puzzle grid.

Each character represents one cell:

| Character | Meaning |
| --- | --- |
| `0` | Light off |
| `1` | Light on |
| `x` | Pillar (fixed obstacle) | 

For example, refer to the `problem.txt` file in this repo for an input example.

### Run the Program

```
python ./lightup.py
```
The program automatically reads problem.txt and searches for a valid solution within the specified click limit.

## Output

The solver prints the resulting click positions using the following notation:

| Character | Meaning |
| --- | --- |
|`X` |  Pillar specified in the input problem |
|`O` | Cell that should be clicked |
|`-` | Cell that should not be pouched |

## Benchmark

The repo also includes `benchmark.txt`, 
which contains more test cases for evaluating the solver against different puzzles.
