"""
Test case for Task 2 - Example 3
Tests Noah (Others) borrowing multiple books and hitting quota limit
"""

import sys
import io

# Mock input sequence for Example 3
input_sequence = [
    "o56799",            # Login as Noah
    "noa6799",           # Password
    "4",                 # Borrow and Return
    "borrow Python Crash Course",  # Borrow first book
    "P0003",             # Confirm physical copy
    "borrow The Hitchhiker's Guide to the Galaxy",  # Try to borrow (no copies)
    "P0004",             # Confirm book ID
    "borrow The Hobbit", # Borrow second book
    "P0008",             # Confirm book ID
    "borrow The Art of Computer Programming",  # Try to borrow (quota reached)
    "P0007",             # Confirm book ID
    "quit",              # Exit borrow/return console
    "0"                  # Quit
]

def run_test():
    """Run the test with mocked inputs"""
    import task2
    
    # Mock stdin
    original_stdin = sys.stdin
    sys.stdin = io.StringIO('\n'.join(input_sequence))
    
    # Capture stdout
    original_stdout = sys.stdout
    output_buffer = io.StringIO()
    sys.stdout = output_buffer
    
    try:
        task2.main('data/users.csv', 'data/books.csv', 'data/loans.csv')
    except SystemExit:
        pass
    finally:
        # Restore stdin/stdout
        sys.stdin = original_stdin
        sys.stdout = original_stdout
    
    # Get output
    output = output_buffer.getvalue()
    
    # Print output for inspection
    print(output)
    
    # Verify key outputs
    assert "Found 2 book(s)" in output  # Python Crash Course has 2 versions
    assert "You have borrowed 'Python Crash Course' by Eric Matthes (2023). Due: 22/09/2025" in output
    assert "Available copies: 0/1" in output  # Hitchhiker's Guide
    assert "No copies available" in output
    assert "You have borrowed 'The Hobbit' by J.R.R. Tolkien (1937). Due: 22/09/2025" in output
    assert "Borrowing unavailable: quota reached" in output
    
    print("\n✓ All assertions passed for Example 3")

if __name__ == "__main__":
    run_test()

