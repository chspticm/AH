"""Worked practice examples for searching, recursion, and backtracking."""

from typing import List, Optional


def find_pattern(text: str, pattern: str) -> List[int]:
    """Return all starting positions of pattern using a simple scan."""
    if pattern == "":
        return list(range(len(text) + 1))

    matches = []
    for start_index in range(len(text) - len(pattern) + 1):
        if text[start_index : start_index + len(pattern)] == pattern:
            matches.append(start_index)
    return matches


def first_prime_after(number: int) -> int:
    """Return the first prime strictly greater than number."""
    candidate = max(2, number + 1)
    while True:
        is_prime = True
        divisor = 2
        while divisor * divisor <= candidate:
            if candidate % divisor == 0:
                is_prime = False
                break
            divisor += 1
        if is_prime:
            return candidate
        candidate += 1


def n_queens_solutions(board_size: int) -> List[List[int]]:
    """Return solutions as column positions, one position per row."""
    if board_size < 0:
        raise ValueError("board_size must be non-negative")

    solutions: List[List[int]] = []
    placement: List[int] = []

    def place_queen(row: int) -> None:
        if row == board_size:
            solutions.append(placement.copy())
            return

        for column in range(board_size):
            conflicts = any(
                previous_column == column
                or abs(previous_column - column) == row - previous_row
                for previous_row, previous_column in enumerate(placement)
            )
            if not conflicts:
                placement.append(column)
                place_queen(row + 1)
                placement.pop()

    place_queen(0)
    return solutions


def main() -> None:
    pattern_positions = find_pattern("bananarama", "ana")
    print("Pattern positions:", pattern_positions)
    print("First prime after 20:", first_prime_after(20))

    four_queen_solutions = n_queens_solutions(4)
    print("Number of 4-Queens solutions:", len(four_queen_solutions))
    for solution in four_queen_solutions:
        print("  columns by row:", solution)

    assert pattern_positions == [1, 3]
    assert find_pattern("abc", "") == [0, 1, 2, 3]
    assert first_prime_after(20) == 23
    assert len(n_queens_solutions(4)) == 2
    assert n_queens_solutions(0) == [[]]


if __name__ == "__main__":
    main()
