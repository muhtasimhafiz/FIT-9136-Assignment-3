"""
Test for quota calculation with online books
Scenario: User has multiple online books - should they count toward quota when borrowing physical?
"""

import sys
from io import StringIO
import task2

print("=" * 70)
print("TESTING: Physical Quota with Existing Online Loans")
print("=" * 70)

# Scenario: Noah (Others - 2 item quota) borrows 2 online books first
# Then tries to borrow 2 physical books
# Question: Do the online books count toward quota when checking physical borrow?

inputs = """o56799
noa6799
2
4
borrow Python Crash Course
E0001
borrow Machine Learning for Business
E0003
borrow Python Crash Course
P0003
borrow The Hobbit
P0008
quit
3
2
0
"""

old_stdin = sys.stdin
sys.stdin = StringIO(inputs)

try:
    task2.main('data/users.csv', 'data/books.csv', 'data/loans.csv')
except SystemExit:
    pass
finally:
    sys.stdin = old_stdin

print("\n" + "=" * 70)
print("ANALYSIS:")
print("  Noah's quota: 2 items")
print("  Borrowed: E0001 (online), E0003 (online)")
print("  Total loans: 2 (0 physical, 2 online)")
print()
print("  Then tries to borrow P0003 (physical)")
print("  Question: Should this be allowed?")
print()
print("CORRECT BEHAVIOR (online doesn't count):")
print("  - P0003 should succeed (0 physical < 2 quota)")
print("  - P0008 should succeed (1 physical < 2 quota)")
print("  - Final: 4 loans (2 physical, 2 online)")
print()
print("INCORRECT BEHAVIOR (if total_loans checked):")
print("  - P0003 blocked with 'quota reached' (2 total >= 2 quota)")
print("  - Final: 2 loans (0 physical, 2 online)")
print("=" * 70)

