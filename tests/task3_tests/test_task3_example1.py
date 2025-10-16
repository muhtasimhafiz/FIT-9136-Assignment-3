"""
Test Task 3 Example 1: Renew loan functionality
Tests renewing books with various validation scenarios
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../set-1'))

def test_example1():
    """Test Example 1: Renew loan with various scenarios"""
    import io
    import task3
    
    # Simulate the input for Example 1
    test_input = """s31267
chr1267
2
3
4
renew P0101
return P0006
renew E0001
return E0001
borrow The Hobbit
P0008
renew P0008
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
    
    print("=== Example 1 Output ===")
    print(output)
    print("=== End of Example 1 ===")
    
    # Verify key outputs
    assert "Renewal denied: You have unpaid fines." in output
    assert "Returned 'Hands-On ML'" in output
    assert "Overdue by 2 day(s). Fine: $ 1.00" in output
    assert "Renewal denied: This book is already overdue." in output
    assert "Returned 'Python Crash Course'" in output
    assert "You have borrowed 'The Hobbit'" in output
    assert "Renew 'The Hobbit'" in output
    assert "New due date: 30/09/2025" in output
    
    print("✓ Example 1 test passed!")

if __name__ == "__main__":
    test_example1()

