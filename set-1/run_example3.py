"""
Manual test for Example 3 - Noah borrowing multiple books and hitting quota
This script simulates the user interaction from Example 3
"""

import sys
from io import StringIO
import task2

# Input sequence for Example 3
inputs = """o56799
noa6799
4
borrow Python Crash Course
P0003
borrow The Hitchhiker's Guide to the Galaxy
P0004
borrow The Hobbit
P0008
borrow The Art of Computer Programming
P0007
quit
0
"""

# Redirect stdin
old_stdin = sys.stdin
sys.stdin = StringIO(inputs)

try:
    print("=" * 60)
    print("Running Example 3: Noah with quota limits")
    print("=" * 60)
    task2.main('data/users.csv', 'data/books.csv', 'data/loans.csv')
except SystemExit:
    pass
finally:
    sys.stdin = old_stdin

print("\n" + "=" * 60)
print("Test completed")
print("=" * 60)

