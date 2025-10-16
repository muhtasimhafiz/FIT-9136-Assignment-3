"""
Test for CRITICAL BUG: Online book quota check
This tests whether a user at quota can borrow online books
"""

import sys
from io import StringIO
import task2

print("=" * 70)
print("TESTING CRITICAL EDGE CASE: Online Book at Quota")
print("=" * 70)

# Scenario: Noah (Others - 2 item quota) borrows 2 physical books
# Then tries to borrow an online book (should succeed since online doesn't count)

inputs = """o56799
noa6799
4
borrow Python Crash Course
P0003
borrow The Hobbit
P0008
borrow Machine Learning for Business
E0003
quit
3
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
print("EXPECTED BEHAVIOR:")
print("  - Noah should borrow P0003 (1/2 quota)")
print("  - Noah should borrow P0008 (2/2 quota)")
print("  - Noah should borrow E0003 (online - doesn't count toward quota)")
print("  - Final loans should show 3 items (2 physical, 1 online)")
print()
print("IF BUG EXISTS:")
print("  - Third borrow will show 'quota reached'")
print("  - Final loans will show only 2 items")
print("=" * 70)

