"""
Test script to verify the invalid input behavior
"""
import sys
from io import StringIO
from contextlib import redirect_stdin, redirect_stdout

def test_invalid_input_behavior():
    """Test that invalid input doesn't re-display the menu"""
    
    # Simulate input with invalid choices
    test_input = """e118102
pa55word
10
5
3
0
"""
    
    print("=== TESTING INVALID INPUT BEHAVIOR ===")
    print("Input sequence: e118102, pa55word, 10, 5, 3, 0")
    print("Expected: Menu should NOT re-display after invalid choices (10, 5)")
    
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
    
    # Count menu displays
    menu_count = 0
    enter_choice_count = 0
    
    for i, line in enumerate(lines):
        if "My Library Account" in line:
            menu_count += 1
            print(f"Menu display #{menu_count} at line {i+1}")
        elif "Enter your choice:" in line:
            enter_choice_count += 1
            print(f"Enter choice prompt #{enter_choice_count} at line {i+1}: '{line}'")
    
    print(f"\nTotal menu displays: {menu_count}")
    print(f"Total 'Enter your choice:' prompts: {enter_choice_count}")
    
    # Check for the expected behavior
    if menu_count <= 2:  # Should only display menu once initially, then after valid actions
        print("✅ SUCCESS: Menu is not re-displayed for invalid choices")
    else:
        print("❌ FAILED: Menu is being re-displayed for invalid choices")
    
    print("\n=== FULL OUTPUT ===")
    print(result)

if __name__ == "__main__":
    test_invalid_input_behavior()
