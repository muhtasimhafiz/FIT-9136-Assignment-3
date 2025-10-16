"""
Test Task 3 Example 2: Search by keywords functionality
Tests keyword search with multiple keywords and proper sorting
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../set-1'))

def test_example2():
    """Test Example 2: Search by keywords"""
    import io
    import task3
    
    # Simulate the input for Example 2
    test_input = """o56799
noa6799
5
python,programming
4
borrow E0003
E0003
quit
3
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
    
    print("=== Example 2 Output ===")
    print(output)
    print("=== End of Example 2 ===")
    
    # Verify search results
    assert "Found 7 book(s)." in output
    assert "P0003 'Python Crash Course' by Eric Matthes (2023)" in output
    assert "P0001 'Introduction to Python Programming' by S Gowrishankar (2019)" in output
    assert "You have borrowed 'Machine Learning for Business'" in output
    assert "Due date: 22/09/2025" in output
    
    print("✓ Example 2 test passed!")

if __name__ == "__main__":
    test_example2()

