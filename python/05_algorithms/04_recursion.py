"""Examples of recursive algorithms and their base cases."""

from typing import List, Tuple


def factorial(number: int) -> int:
    """Return number factorial, rejecting negative input."""
    if number < 0:
        raise ValueError("factorial is not defined for negative integers")
    if number < 2:
        return 1
    return number * factorial(number - 1)


def fibonacci_recursive(index: int) -> int:
    """Return a Fibonacci number using a simple, slow recursion."""
    if index < 0:
        raise ValueError("index must be non-negative")
    if index < 2:
        return index
    return fibonacci_recursive(index - 1) + fibonacci_recursive(index - 2)


def tower_of_hanoi(number_of_disks: int) -> List[Tuple[str, str]]:
    """Return the moves to transfer disks from peg A to peg C."""
    if number_of_disks < 0:
        raise ValueError("number_of_disks must be non-negative")

    moves: List[Tuple[str, str]] = []

    def move_disks(disks: int, source: str, destination: str, spare: str) -> None:
        if disks == 0:
            return
        move_disks(disks - 1, source, spare, destination)
        moves.append((source, destination))
        move_disks(disks - 1, spare, destination, source)

    move_disks(number_of_disks, "A", "C", "B")
    return moves


def main() -> None:
    print("5! =", factorial(5))
    print("Fibonacci(8) =", fibonacci_recursive(8))

    moves = tower_of_hanoi(3)
    for move_number, (source, destination) in enumerate(moves, start=1):
        print("Move {}: {} -> {}".format(move_number, source, destination))

    assert factorial(0) == 1
    assert factorial(5) == 120
    assert fibonacci_recursive(8) == 21
    assert len(tower_of_hanoi(3)) == 7


if __name__ == "__main__":
    main()
