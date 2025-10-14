"""
Test to simulate the exact sequence that's causing the issue
"""
import sys
from io import StringIO
from contextlib import redirect_stdin, redirect_stdout

def test_menu_sequence():
    """Test the exact menu sequence that's causing the issue"""
    
    # Simulate the exact input sequence
    test_input = """e118102
pa55word
4
3
0
"""
    
    print("=== SIMULATING THE EXACT SEQUENCE ===")
    print("Input sequence:")
    print(test_input)
    
    try:
        with redirect_stdin(StringIO(test_input)):
            with redirect_stdout(StringIO()) as output:
                # Import and run the main function
                import task1
                task1.main('data/users.csv', 'data/books.csv', 'data/loans.csv')
    except SystemExit:
        pass  # Expected when program exits
    
    # Get the output
    result = output.getvalue()
    
    print("\n=== OUTPUT ANALYSIS ===")
    lines = result.strip().split('\n')
    
    # Look for the problematic sequence
    for i, line in enumerate(lines):
        if "Enter your choice:" in line:
            print(f"Line {i+1}: '{line}'")
            # Check if the next line also has "Enter your choice:"
            if i+1 < len(lines) and "Enter your choice:" in lines[i+1]:
                print(f"Line {i+2}: '{lines[i+1]}' - DUPLICATE PROMPT FOUND!")
    
    print(f"\nTotal lines: {len(lines)}")
    print("Full output:")
    print(result)

if __name__ == "__main__":
    test_menu_sequence()
