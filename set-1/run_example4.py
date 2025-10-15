"""
Manual test for Example 4 - Library Report with invalid inputs
This script simulates the user interaction from Example 4
"""

import sys
from io import StringIO
import task2

# Input sequence for Example 4
inputs = """e118102
pa55word
5
P01
5
Python Crash Course
0
"""

# Redirect stdin
old_stdin = sys.stdin
sys.stdin = StringIO(inputs)

try:
    print("=" * 60)
    print("Running Example 4: Library Report with invalid inputs")
    print("=" * 60)
    task2.main('data/users.csv', 'data/books.csv', 'data/loans.csv')
except SystemExit:
    pass
finally:
    sys.stdin = old_stdin

print("\n" + "=" * 60)
print("Test completed")
print("=" * 60)

