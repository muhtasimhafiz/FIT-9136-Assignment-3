"""
Test script to reproduce the missing "Enter your choice:" prompt issue
"""
import user
import book
from task1 import load_loans, library_report

def test_library_report_output():
    """Test the library report output format"""
    
    # Load data
    users = user.load_users('data/users.csv')
    books = book.load_books('data/books.csv')
    loans = load_loans('data/loans.csv')
    
    print("=== TESTING LIBRARY REPORT OUTPUT ===")
    
    # Test the library report function directly
    print("Testing library_report function:")
    library_report(users, books, loans)
    
    print("\n=== EXPECTED OUTPUT FORMAT ===")
    print("Library report")
    print("- 9 users, including 4 student(s), 3 staff, and 2 others.")
    print("- 14 books, including 10 physical book(s) (7 currently available) and 4 online book(s).")
    
    print("\n=== CHECKING FORMATTING ===")
    # Check if there are any extra newlines or formatting issues
    import io
    from contextlib import redirect_stdout
    
    output = io.StringIO()
    with redirect_stdout(output):
        library_report(users, books, loans)
    
    result = output.getvalue()
    print(f"Raw output length: {len(result)}")
    print(f"Raw output: {repr(result)}")
    
    lines = result.strip().split('\n')
    print(f"Number of lines: {len(lines)}")
    for i, line in enumerate(lines):
        print(f"Line {i+1}: '{line}'")

if __name__ == "__main__":
    test_library_report_output()
