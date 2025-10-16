"""
Test Task 3 Example 3: Manage Library - Add books
Tests adding physical books and library report functionality
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../set-1'))

def test_example3():
    """Test Example 3: Manage Library console"""
    import io
    import task3
    
    # Simulate the input for Example 3
    test_input = """e118102
pa55word
6
report
add physical
A Concise and Practical Introduction to Programming Algorithms in Java
Nielsen Frank
2017
1
report
quit
0
"""
    
    sys.stdin = io.StringIO(test_input)
    original_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    try:
        task3.main('data/users.csv', 'data/books.csv', 'data/loans.csv')
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = original_stdout
        sys.stdin = sys.__stdin__
    
    print("=== Example 3 Output ===")
    print(output)
    print("=== End of Example 3 ===")
    
    # Verify library report and book addition
    assert "Library report" in output
    assert "9 users" in output
    assert "14 books" in output
    assert "Detected keywords: algorithms:programming" in output
    assert "Adding P0020" in output
    assert "15 books" in output
    assert "11 physical book(s)" in output
    
    print("✓ Example 3 test passed!")

if __name__ == "__main__":
    test_example3()

