"""
Test case for Task 2 - Example 1
Tests Chris Manner (Student) with fines, borrowing blocked by fines, returning books
"""

import sys
import io

# Mock input sequence for Example 1
input_sequence = [
    "s31267",           # Login as
    "chr1267",          # Password
    "2",                # View account policies
    "3",                # View my loans
    "4",                # Borrow and Return
    "borrow The Hobbit", # Try to borrow (should fail - has fines)
    "P0008",            # Confirm book ID
    "return P0006",     # Return overdue book
    "return P0011",     # Return non-existent loan
    "return E0001",     # Return online book
    "quit",             # Exit borrow/return console
    "3",                # View my loans again
    "0"                 # Quit
]

def run_test():
    """Run the test with mocked inputs"""
    # Import after setting up the path
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
    assert "Fines: $ 1.00" in output, "Should show $1.00 fine"
    assert "Borrowing unavailable: unpaid fines" in output, "Should block borrowing due to fines"
    assert "Overdue by 2 day(s). Fine: $ 1.00" in output, "Should show fine when returning"
    assert "No loan record for P0011" in output, "Should show no loan record message"
    assert "You are currently have 0 loan(s)" in output, "Should show 0 loans after returns"
    
    print("\n✓ All assertions passed for Example 1")

if __name__ == "__main__":
    run_test()

