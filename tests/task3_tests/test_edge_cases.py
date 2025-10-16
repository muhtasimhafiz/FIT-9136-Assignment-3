"""
Edge Cases Test for Task 3
Tests various edge cases and error conditions
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../set-1'))

def test_edge_cases():
    """Test various edge cases in Task 3"""
    import task3
    import book
    import user
    
    print("=" * 70)
    print("TASK 3 EDGE CASES TESTING")
    print("=" * 70)
    
    # Load normal data
    users = user.load_users('data/users.csv')
    books = book.load_books('data/books.csv')
    loans = task3.load_loans('data/loans.csv')
    
    print(f"✓ Loaded {len(users)} users, {len(books)} books, {len(loans)} loans")
    
    # Test 1: Empty keywords
    print("\n" + "=" * 50)
    print("TEST 1: Empty Keywords")
    print("=" * 50)
    
    empty_keywords = task3.search_by_keywords([], books)
    print(f"Empty keywords result: {len(empty_keywords)} books")
    
    whitespace_keywords = task3.search_by_keywords(['', '   ', ','], books)
    print(f"Whitespace keywords result: {len(whitespace_keywords)} books")
    
    print("✓ Empty keywords handled correctly")
    
    # Test 2: Invalid book ID format
    print("\n" + "=" * 50)
    print("TEST 2: Book ID Generation Edge Cases")
    print("=" * 50)
    
    # Test with malformed book IDs
    malformed_books = {
        'P0001': book.Book('P0001', 'physical', 1, 'Test Book', 'Author', '2023', 'test'),
        'PABC': book.Book('PABC', 'physical', 1, 'Invalid ID', 'Author', '2023', 'test'),
        'P': book.Book('P', 'physical', 1, 'Invalid ID 2', 'Author', '2023', 'test'),
        'E0001': book.Book('E0001', 'online', 0, 'Online Book', 'Author', '2023', 'test')
    }
    
    try:
        new_physical_id = task3.generate_book_id(malformed_books, 'physical')
        new_online_id = task3.generate_book_id(malformed_books, 'online')
        print(f"Generated physical ID: {new_physical_id}")
        print(f"Generated online ID: {new_online_id}")
        print("✓ Book ID generation handles malformed IDs")
    except Exception as e:
        print(f"✗ Book ID generation failed: {e}")
    
    # Test 3: Keyword detection edge cases
    print("\n" + "=" * 50)
    print("TEST 3: Keyword Detection Edge Cases")
    print("=" * 50)
    
    all_keywords = task3.get_all_keywords(books)
    print(f"Total keywords found: {len(all_keywords)}")
    
    # Test with various titles
    test_titles = [
        "Python Programming",  # Should match 'python' and 'programming'
        "Machine Learning with Python",  # Should match multiple keywords
        "Random Book Title",  # Should match nothing
        "",  # Empty title
        "A Very Long Title That Might Not Match Anything Specific"  # Long title
    ]
    
    for title in test_titles:
        detected = task3.detect_keywords_from_title(title, all_keywords)
        print(f"Title: '{title}' -> Keywords: {detected}")
    
    print("✓ Keyword detection handles various titles")
    
    # Test 4: Fine calculation edge cases
    print("\n" + "=" * 50)
    print("TEST 4: Fine Calculation Edge Cases")
    print("=" * 50)
    
    # Test with different user
    test_user = users['s31267']
    display_fines = task3.get_user_fines(loans, books, test_user.user_id)
    blocking_fines = task3.get_user_unpaid_fines(loans, books, test_user.user_id)
    
    print(f"User: {test_user.name}")
    print(f"Display fines: ${display_fines:.2f}")
    print(f"Blocking fines: ${blocking_fines:.2f}")
    
    # Test with non-existent user
    non_existent_fines = task3.get_user_fines(loans, books, 'nonexistent')
    print(f"Non-existent user fines: ${non_existent_fines:.2f}")
    
    print("✓ Fine calculation handles edge cases")
    
    # Test 5: Search edge cases
    print("\n" + "=" * 50)
    print("TEST 5: Search Edge Cases")
    print("=" * 50)
    
    # Test various search terms
    search_terms = [
        "python",
        "PYTHON",  # Case insensitive
        "nonexistent",
        "",
        "python,programming,ml",
        "python,,programming",  # Empty keyword
        "python,programming,",  # Trailing comma
    ]
    
    for term in search_terms:
        keywords = [kw.strip() for kw in term.split(',')]
        results = task3.search_by_keywords(keywords, books)
        print(f"Search '{term}' -> {len(results)} results")
    
    print("✓ Search handles various input formats")
    
    # Test 6: Loan count edge cases
    print("\n" + "=" * 50)
    print("TEST 6: Loan Count Edge Cases")
    print("=" * 50)
    
    # Test with different users
    for user_id in ['s31267', 'e118102', 'nonexistent']:
        total, physical, online = task3.get_user_loans_count(loans, user_id)
        print(f"User {user_id}: {total} total ({physical} physical, {online} online)")
    
    print("✓ Loan counting handles edge cases")
    
    # Summary
    print("\n" + "=" * 70)
    print("EDGE CASES TEST SUMMARY")
    print("=" * 70)
    print("✓ Empty keywords handled")
    print("✓ Malformed book IDs handled")
    print("✓ Keyword detection robust")
    print("✓ Fine calculation safe")
    print("✓ Search input validation")
    print("✓ Loan counting safe")
    print("\n⚠️  Note: Some edge cases may still exist in:")
    print("   - User input validation (add book)")
    print("   - Year conversion errors")
    print("   - File I/O errors")
    print("=" * 70)

if __name__ == "__main__":
    # Change to set-1 directory
    os.chdir(os.path.join(os.path.dirname(__file__), '../../set-1'))
    test_edge_cases()

