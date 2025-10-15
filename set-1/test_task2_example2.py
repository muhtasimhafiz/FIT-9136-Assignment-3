"""
Test case for Task 2 - Example 2
Tests Mary Alan (Staff) borrowing, then Justin Bierber tries to borrow same book
"""

import sys
import io

# Mock input sequence for Example 2
input_sequence = [
    "e118102",           # Login as Mary
    "pa55word",          # Password
    "2",                 # View account policies
    "3",                 # View my loans
    "4",                 # Borrow and Return
    "borrow The Hobbit", # Borrow The Hobbit
    "P0007",             # Invalid book ID (not in list)
    "P0008",             # Correct book ID
    "quit",              # Exit borrow/return console
    "1",                 # Log out
    "s31245",            # Login as Justin
    "secure99",          # Password
    "4",                 # Borrow and Return
    "borrow The Hobbit", # Try to borrow same book
    "P0008",             # Confirm book ID
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
    assert "Staff Mary Alan. Policies: maximum of 14 days, 6 items" in output
    assert "Fines: $ 0.00" in output
    assert "You have borrowed 'The Hobbit' by J.R.R. Tolkien (1937). Due: 29/09/2025" in output
    assert "Available copies: 0/2" in output  # After Mary borrows
    assert "No copies available" in output  # Justin cannot borrow
    
    print("\n✓ All assertions passed for Example 2")

if __name__ == "__main__":
    run_test()

