"""
Manual test for Example 2 - Mary Alan (Staff) and Justin Bierber
This script simulates the user interaction from Example 2
"""

import sys
from io import StringIO
import task2

# Input sequence for Example 2
inputs = """e118102
pa55word
2
3
4
borrow The Hobbit
P0007
P0008
quit
1
s31245
secure99
4
borrow The Hobbit
P0008
quit
0
"""

# Redirect stdin
old_stdin = sys.stdin
sys.stdin = StringIO(inputs)

try:
    print("=" * 60)
    print("Running Example 2: Mary Alan and Justin Bierber")
    print("=" * 60)
    task2.main('data/users.csv', 'data/books.csv', 'data/loans.csv')
except SystemExit:
    pass
finally:
    sys.stdin = old_stdin

print("\n" + "=" * 60)
print("Test completed")
print("=" * 60)

