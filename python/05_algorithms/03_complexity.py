"""Count simple operations to illustrate common growth rates."""

from typing import Dict, List


def logarithmic_steps(size: int) -> int:
    """Count halvings needed to reduce size to zero or one."""
    steps = 0
    while size > 1:
        size //= 2
        steps += 1
    return steps


def linear_steps(size: int) -> int:
    """Return the number of iterations in a single pass."""
    return size


def nested_loop_steps(size: int) -> int:
    """Count iterations of two loops, each running size times."""
    return size * size


def growth_examples(size: int) -> Dict[str, int]:
    """Return illustrative operation counts for the supplied input size."""
    return {
        "O(1)": 1,
        "O(log n)": logarithmic_steps(size),
        "O(n)": linear_steps(size),
        "O(n log n)": size * logarithmic_steps(size),
        "O(n^2)": nested_loop_steps(size),
        "O(2^n)": 2 ** size,
    }


def main() -> None:
    sizes: List[int] = [4, 8, 16]
    headings = ["n", "O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n^2)", "O(2^n)"]
    print(" | ".join(headings))

    for size in sizes:
        counts = growth_examples(size)
        row = [str(size)] + [str(counts[heading]) for heading in headings[1:]]
        print(" | ".join(row))

    print("\nExamples:")
    print("- Array index lookup is typically O(1).")
    print("- Linear search is O(n); binary search on sorted data is O(log n).")
    print("- A nested scan may be O(n^2).")
    print("- Merge sort is O(n log n) in the best, average, and worst cases.")
    print("- Recursive Fibonacci without caching is O(2^n) time and O(n) stack space.")

    assert logarithmic_steps(16) == 4
    assert linear_steps(16) == 16
    assert nested_loop_steps(16) == 256


if __name__ == "__main__":
    main()
