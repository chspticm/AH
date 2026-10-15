"""Use memoization and tabulation to avoid repeated calculations."""

from typing import List, Optional, Sequence


def fibonacci_memoized(index: int) -> int:
    """Return a Fibonacci number using top-down memoization."""
    if index < 0:
        raise ValueError("index must be non-negative")

    memo: List[Optional[int]] = [None] * (index + 1)

    def calculate(current_index: int) -> int:
        if current_index < 2:
            return current_index
        if memo[current_index] is None:
            memo[current_index] = calculate(current_index - 1) + calculate(current_index - 2)
        return memo[current_index]

    return calculate(index)


def fibonacci_tabulated(index: int) -> int:
    """Return a Fibonacci number using bottom-up tabulation."""
    if index < 0:
        raise ValueError("index must be non-negative")
    if index < 2:
        return index

    previous_value = 0
    current_value = 1
    for _ in range(2, index + 1):
        previous_value, current_value = current_value, previous_value + current_value
    return current_value


def minimum_coins(coins: Sequence[int], amount: int) -> Optional[int]:
    """Return the fewest coins needed, or None when the amount is impossible.

    Each coin denomination can be used any number of times.
    """
    if amount < 0:
        raise ValueError("amount must be non-negative")
    if any(coin <= 0 for coin in coins):
        raise ValueError("coin denominations must be positive")
    if amount == 0:
        return 0

    unreachable = amount + 1
    fewest_coins = [0] + [unreachable] * amount
    for subtotal in range(1, amount + 1):
        for coin in coins:
            if coin <= subtotal:
                fewest_coins[subtotal] = min(
                    fewest_coins[subtotal],
                    fewest_coins[subtotal - coin] + 1,
                )

    if fewest_coins[amount] == unreachable:
        return None
    return fewest_coins[amount]


def main() -> None:
    for index in (0, 1, 8, 30):
        print(
            "Fibonacci({}) = {}".format(
                index,
                fibonacci_memoized(index),
            )
        )

    print("Minimum coins for 11 using 1, 5, 7:", minimum_coins([1, 5, 7], 11))
    print("Minimum coins for 3 using 2, 4:", minimum_coins([2, 4], 3))

    assert fibonacci_memoized(30) == 832040
    assert fibonacci_tabulated(30) == 832040
    assert minimum_coins([1, 5, 7], 11) == 3
    assert minimum_coins([2, 4], 3) is None
    assert minimum_coins([2, 4], 0) == 0


if __name__ == "__main__":
    main()
