#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

# Test cases
test_cases = [
    {
        "coins": [1, 2, 5],
        "total": 11,
        "expected": 3  # 5 + 5 + 1 = 11
    },
    {
        "coins": [2, 4, 6],
        "total": 7,
        "expected": -1  # No combination can make 7 with 2, 4, 6
    },
    {
        "coins": [1, 3, 4],
        "total": 6,
        "expected": 2  # 3 + 3 = 6
    },
    {
        "coins": [1, 3, 4],
        "total": 0,
        "expected": 0  # Total is 0, no coins needed
    },
    {
        "coins": [1, 5, 10, 25],
        "total": 30,
        "expected": 2  # 25 + 5 = 30
    }
]

# Run tests
for i, case in enumerate(test_cases):
    result = makeChange(case["coins"], case["total"])
    print(
        f"Test Case {i+1}: {'Passed' if result == case['expected'] else 'Failed'}")
    print(
        f"Coins: {case['coins']}, Total: {case['total']}, Expected: {case['expected']}, Got: {result}")
    print()
