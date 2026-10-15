"""Implement common comparison-based sorting algorithms."""

from typing import List


def bubble_sort(values: List[int]) -> List[int]:
    """Return a sorted copy using repeated adjacent swaps."""
    result = values.copy()
    for end_index in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end_index):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if not swapped:
            break
    return result


def selection_sort(values: List[int]) -> List[int]:
    """Return a sorted copy by selecting the smallest remaining value."""
    result = values.copy()
    for start_index in range(len(result)):
        smallest_index = start_index
        for index in range(start_index + 1, len(result)):
            if result[index] < result[smallest_index]:
                smallest_index = index
        result[start_index], result[smallest_index] = (
            result[smallest_index],
            result[start_index],
        )
    return result


def insertion_sort(values: List[int]) -> List[int]:
    """Return a sorted copy by inserting each value into a sorted prefix."""
    result = values.copy()
    for index in range(1, len(result)):
        current_value = result[index]
        insert_index = index - 1
        while insert_index >= 0 and result[insert_index] > current_value:
            result[insert_index + 1] = result[insert_index]
            insert_index -= 1
        result[insert_index + 1] = current_value
    return result


def merge_sort(values: List[int]) -> List[int]:
    """Return a sorted copy using divide and conquer."""
    if len(values) < 2:
        return values.copy()

    middle_index = len(values) // 2
    left_half = merge_sort(values[:middle_index])
    right_half = merge_sort(values[middle_index:])
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            merged.append(left_half[left_index])
            left_index += 1
        else:
            merged.append(right_half[right_index])
            right_index += 1

    merged.extend(left_half[left_index:])
    merged.extend(right_half[right_index:])
    return merged


def quick_sort(values: List[int]) -> List[int]:
    """Return a sorted copy using the last value as a pivot.

    This readable recursive version creates temporary lists. Its worst-case
    running time is quadratic when the partitions are highly unbalanced.
    """
    if len(values) < 2:
        return values.copy()

    pivot = values[-1]
    lower_values = [value for value in values[:-1] if value <= pivot]
    higher_values = [value for value in values[:-1] if value > pivot]
    return quick_sort(lower_values) + [pivot] + quick_sort(higher_values)


def main() -> None:
    sample_values = [64, 25, 12, 22, 11, 25]
    sorting_algorithms = [
        bubble_sort,
        selection_sort,
        insertion_sort,
        merge_sort,
        quick_sort,
    ]

    for sorting_algorithm in sorting_algorithms:
        result = sorting_algorithm(sample_values)
        print("{}: {}".format(sorting_algorithm.__name__, result))
        assert result == sorted(sample_values)

    assert sample_values == [64, 25, 12, 22, 11, 25]
    assert merge_sort([]) == []
    assert quick_sort([3, 3, 3]) == [3, 3, 3]


if __name__ == "__main__":
    main()
