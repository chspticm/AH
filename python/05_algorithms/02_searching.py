"""Demonstrate linear and binary search."""

from typing import List, Optional


def linear_search(values: List[int], target: int) -> Optional[int]:
    """Return the first matching index, or None if the target is absent."""
    for index, value in enumerate(values):
        if value == target:
            return index
    return None


def binary_search(sorted_values: List[int], target: int) -> Optional[int]:
    """Return the first matching index in an ascending list, or None.

    The input must already be sorted. This implementation uses a half-open
    search range and finds the first occurrence when duplicates are present.
    """
    lower_bound = 0
    upper_bound = len(sorted_values)

    while lower_bound < upper_bound:
        middle_index = (lower_bound + upper_bound) // 2
        if sorted_values[middle_index] < target:
            lower_bound = middle_index + 1
        else:
            upper_bound = middle_index

    if lower_bound < len(sorted_values) and sorted_values[lower_bound] == target:
        return lower_bound
    return None


def main() -> None:
    values = [3, 8, 12, 17, 17, 24, 31]
    target = 17

    print("Linear search index:", linear_search(values, target))
    print("Binary search index:", binary_search(values, target))
    print("Missing target:", binary_search(values, 99))

    assert linear_search(values, target) == 3
    assert binary_search(values, target) == 3
    assert binary_search(values, 99) is None
    assert binary_search([], 1) is None


if __name__ == "__main__":
    main()
