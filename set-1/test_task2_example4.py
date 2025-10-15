"""
Test case for Task 2 - Example 4
Tests Mary Alan (Staff) accessing Library Report with invalid menu inputs
"""

import sys
import io

# Mock input sequence for Example 4
input_sequence = [
    "e118102",           # Login as Mary
    "pa55word",          # Password
    "5",                 # Library Report
    "P01",               # Invalid choice
    "5",                 # Library Report again
    "Python Crash Course",  # Invalid choice
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
    assert "Library report" in output
    assert "9 users, including 4 student(s), 3 staff, and 2 others" in output
    assert "14 books, including 10 physical book(s)" in output
    # Should display menu twice after Library Report calls
    output_lines = output.split('\n')
    menu_count = sum(1 for line in output_lines if "5. Library Report" in line)
    assert menu_count >= 2, "Menu should appear at least twice"
    
    print("\n✓ All assertions passed for Example 4")

if __name__ == "__main__":
    run_test()

