"""
Automated test suite for Library Management System - Task 1
"""
import sys
import io
from contextlib import contextmanager
import user
import book
from task1 import (
    load_loans, get_active_loans, get_user_loans_count,
    get_available_books_count, parse_date
)


@contextmanager
def captured_output():
    """Capture stdout for testing"""
    new_out = io.StringIO()
    old_out = sys.stdout
    try:
        sys.stdout = new_out
        yield sys.stdout
    finally:
        sys.stdout = old_out


def test_user_loading():
    """Test user loading from CSV"""
    print("\n=== Testing User Loading ===")
    users = user.load_users('data/users.csv')
    
    assert len(users) == 9, f"Expected 9 users, got {len(users)}"
    print(f"✓ Loaded {len(users)} users")
    
    # Test student
    assert 's31267' in users, "Student s31267 not found"
    chris = users['s31267']
    assert isinstance(chris, user.Student), "s31267 should be Student"
    assert chris.name == "Chris Manner", f"Expected 'Chris Manner', got '{chris.name}'"
    assert chris.password == "chr1267", "Password mismatch"
    assert chris.get_max_days() == 10, "Student max days should be 10"
    assert chris.get_max_items() == 4, "Student max items should be 4"
    print("✓ Student user loaded correctly")
    
    # Test staff
    assert 'e118102' in users, "Staff e118102 not found"
    mary = users['e118102']
    assert isinstance(mary, user.Staff), "e118102 should be Staff"
    assert mary.name == "Mary Alan", f"Expected 'Mary Alan', got '{mary.name}'"
    assert mary.department == "Library", "Department should be Library"
    assert mary.is_library_staff(), "Should be library staff"
    assert mary.get_max_days() == 14, "Staff max days should be 14"
    assert mary.get_max_items() == 6, "Staff max items should be 6"
    print("✓ Library staff user loaded correctly")
    
    # Test non-library staff
    lan = users['e45261']
    assert isinstance(lan, user.Staff), "e45261 should be Staff"
    assert lan.department == "Business", "Department should be Business"
    assert not lan.is_library_staff(), "Should not be library staff"
    print("✓ Non-library staff user loaded correctly")
    
    # Test others
    assert 'o56789' in users, "Others o56789 not found"
    chloe = users['o56789']
    assert isinstance(chloe, user.Others), "o56789 should be Others"
    assert chloe.name == "Chloe", f"Expected 'Chloe', got '{chloe.name}'"
    assert chloe.get_max_days() == 7, "Others max days should be 7"
    assert chloe.get_max_items() == 2, "Others max items should be 2"
    print("✓ Others user loaded correctly")
    
    print("✓ All user loading tests passed!")


def test_book_loading():
    """Test book loading from CSV"""
    print("\n=== Testing Book Loading ===")
    books = book.load_books('data/books.csv')
    
    assert len(books) == 14, f"Expected 14 books, got {len(books)}"
    print(f"✓ Loaded {len(books)} books")
    
    # Test physical book
    assert 'P0006' in books, "Book P0006 not found"
    hands_on = books['P0006']
    assert hands_on.is_physical(), "P0006 should be physical"
    assert not hands_on.is_online(), "P0006 should not be online"
    assert hands_on.title == "Hands-On ML", f"Expected 'Hands-On ML', got '{hands_on.title}'"
    assert hands_on.author == "Aurelien Geron", "Author mismatch"
    assert hands_on.year == "2019", "Year mismatch"
    assert hands_on.total_copies == 1, "Should have 1 copy"
    print("✓ Physical book loaded correctly")
    
    # Test online book
    assert 'E0001' in books, "Book E0001 not found"
    python_crash = books['E0001']
    assert python_crash.is_online(), "E0001 should be online"
    assert not python_crash.is_physical(), "E0001 should not be physical"
    assert python_crash.total_copies == 0, "Online books should have 0 copies"
    print("✓ Online book loaded correctly")
    
    # Count book types
    physical_count = sum(1 for b in books.values() if b.is_physical())
    online_count = sum(1 for b in books.values() if b.is_online())
    assert physical_count == 10, f"Expected 10 physical books, got {physical_count}"
    assert online_count == 4, f"Expected 4 online books, got {online_count}"
    print(f"✓ Book counts correct: {physical_count} physical, {online_count} online")
    
    print("✓ All book loading tests passed!")


def test_loan_loading():
    """Test loan loading from CSV"""
    print("\n=== Testing Loan Loading ===")
    loans = load_loans('data/loans.csv')
    
    assert len(loans) == 8, f"Expected 8 loans, got {len(loans)}"
    print(f"✓ Loaded {len(loans)} loans")
    
    # Test active loans
    active = get_active_loans(loans)
    assert len(active) == 6, f"Expected 6 active loans, got {len(active)}"
    print(f"✓ {len(active)} active loans found")
    
    # Test user-specific active loans
    chris_loans = get_active_loans(loans, 's31267')
    assert len(chris_loans) == 2, f"Expected 2 active loans for s31267, got {len(chris_loans)}"
    print("✓ User-specific loan filtering works")
    
    print("✓ All loan loading tests passed!")


def test_loan_counts():
    """Test loan counting functions"""
    print("\n=== Testing Loan Counts ===")
    loans = load_loans('data/loans.csv')
    
    # Test Chris (2 loans: 1 physical, 1 online)
    total, physical, online = get_user_loans_count(loans, 's31267')
    assert total == 2, f"Expected 2 total loans for s31267, got {total}"
    assert physical == 1, f"Expected 1 physical loan for s31267, got {physical}"
    assert online == 1, f"Expected 1 online loan for s31267, got {online}"
    print("✓ Chris's loan counts correct (2 total: 1 physical, 1 online)")
    
    # Test Mary (1 loan: 1 physical, 0 online)
    total, physical, online = get_user_loans_count(loans, 'e118102')
    assert total == 1, f"Expected 1 total loan for e118102, got {total}"
    assert physical == 1, f"Expected 1 physical loan for e118102, got {physical}"
    assert online == 0, f"Expected 0 online loans for e118102, got {online}"
    print("✓ Mary's loan counts correct (1 total: 1 physical, 0 online)")
    
    # Test Chloe (0 loans)
    total, physical, online = get_user_loans_count(loans, 'o56789')
    assert total == 0, f"Expected 0 total loans for o56789, got {total}"
    assert physical == 0, f"Expected 0 physical loans for o56789, got {physical}"
    assert online == 0, f"Expected 0 online loans for o56789, got {online}"
    print("✓ Chloe's loan counts correct (0 loans)")
    
    # Test Lan (1 loan: 1 physical, 0 online)
    total, physical, online = get_user_loans_count(loans, 'e45261')
    assert total == 1, f"Expected 1 total loan for e45261, got {total}"
    assert physical == 1, f"Expected 1 physical loan for e45261, got {physical}"
    assert online == 0, f"Expected 0 online loans for e45261, got {online}"
    print("✓ Lan's loan counts correct (1 total: 1 physical, 0 online)")
    
    print("✓ All loan count tests passed!")


def test_available_books():
    """Test available books counting"""
    print("\n=== Testing Available Books Count ===")
    books = book.load_books('data/books.csv')
    loans = load_loans('data/loans.csv')
    
    available = get_available_books_count(books, loans)
    assert available == 7, f"Expected 7 available physical books, got {available}"
    print(f"✓ Available books count correct: {available}")
    
    # Verify individual book availability
    # P0006 - 1 copy, 1 borrowed = 0 available
    p0006_loans = sum(1 for loan in get_active_loans(loans) if loan['book_id'] == 'P0006')
    assert p0006_loans == 1, "P0006 should have 1 active loan"
    
    # P0002 - 5 copies, 0 borrowed = 5 available
    p0002_loans = sum(1 for loan in get_active_loans(loans) if loan['book_id'] == 'P0002')
    assert p0002_loans == 0, "P0002 should have 0 active loans"
    
    print("✓ All available books tests passed!")


def test_user_policies():
    """Test user policy display"""
    print("\n=== Testing User Policies ===")
    users = user.load_users('data/users.csv')
    loans = load_loans('data/loans.csv')
    
    # Test Student
    chris = users['s31267']
    total, physical, online = get_user_loans_count(loans, chris.user_id)
    expected = "Student Chris Manner. Policies: maximum of 10 days, 4 items. Current loans: 2 (1 physical / 1 online)."
    actual = f"{chris.get_role_display()} {chris.name}. Policies: maximum of {chris.get_max_days()} days, {chris.get_max_items()} items. Current loans: {total} ({physical} physical / {online} online)."
    assert actual == expected, f"Student policy mismatch:\nExpected: {expected}\nActual: {actual}"
    print("✓ Student policy display correct")
    
    # Test Staff
    mary = users['e118102']
    total, physical, online = get_user_loans_count(loans, mary.user_id)
    expected = "Staff Mary Alan. Policies: maximum of 14 days, 6 items. Current loans: 1 (1 physical / 0 online)."
    actual = f"{mary.get_role_display()} {mary.name}. Policies: maximum of {mary.get_max_days()} days, {mary.get_max_items()} items. Current loans: {total} ({physical} physical / {online} online)."
    assert actual == expected, f"Staff policy mismatch:\nExpected: {expected}\nActual: {actual}"
    print("✓ Staff policy display correct")
    
    # Test Others
    chloe = users['o56789']
    total, physical, online = get_user_loans_count(loans, chloe.user_id)
    expected = "Others Chloe. Policies: maximum of 7 days, 2 items. Current loans: 0 (0 physical / 0 online)."
    actual = f"{chloe.get_role_display()} {chloe.name}. Policies: maximum of {chloe.get_max_days()} days, {chloe.get_max_items()} items. Current loans: {total} ({physical} physical / {online} online)."
    assert actual == expected, f"Others policy mismatch:\nExpected: {expected}\nActual: {actual}"
    print("✓ Others policy display correct")
    
    print("✓ All user policy tests passed!")


def test_date_parsing():
    """Test date parsing and sorting"""
    print("\n=== Testing Date Parsing ===")
    
    date1 = parse_date("13/09/2025")
    date2 = parse_date("15/09/2025")
    date3 = parse_date("17/09/2025")
    
    assert date1 < date2 < date3, "Date sorting not working correctly"
    print("✓ Date parsing and sorting works correctly")
    
    print("✓ All date parsing tests passed!")


def test_library_report():
    """Test library report statistics"""
    print("\n=== Testing Library Report ===")
    users = user.load_users('data/users.csv')
    books = book.load_books('data/books.csv')
    loans = load_loans('data/loans.csv')
    
    # Count users by role
    students = sum(1 for u in users.values() if isinstance(u, user.Student))
    staff = sum(1 for u in users.values() if isinstance(u, user.Staff))
    others = sum(1 for u in users.values() if isinstance(u, user.Others))
    
    assert students == 4, f"Expected 4 students, got {students}"
    assert staff == 3, f"Expected 3 staff, got {staff}"
    assert others == 2, f"Expected 2 others, got {others}"
    print(f"✓ User counts correct: {students} students, {staff} staff, {others} others")
    
    # Count books by type
    physical_books = sum(1 for b in books.values() if b.is_physical())
    online_books = sum(1 for b in books.values() if b.is_online())
    
    assert physical_books == 10, f"Expected 10 physical books, got {physical_books}"
    assert online_books == 4, f"Expected 4 online books, got {online_books}"
    print(f"✓ Book counts correct: {physical_books} physical, {online_books} online")
    
    # Count available books
    available = get_available_books_count(books, loans)
    assert available == 7, f"Expected 7 available books, got {available}"
    print(f"✓ Available books count correct: {available}")
    
    # Test report format
    expected_line1 = f"- {len(users)} users, including {students} student(s), {staff} staff, and {others} others."
    expected_line2 = f"- {len(books)} books, including {physical_books} physical book(s) ({available} currently available) and {online_books} online book(s)."
    
    print("✓ Library report statistics correct")
    print(f"  {expected_line1}")
    print(f"  {expected_line2}")
    
    print("✓ All library report tests passed!")


def test_role_display():
    """Test role display formatting"""
    print("\n=== Testing Role Display ===")
    users = user.load_users('data/users.csv')
    
    chris = users['s31267']
    assert chris.get_role_display() == "Student", f"Expected 'Student', got '{chris.get_role_display()}'"
    
    mary = users['e118102']
    assert mary.get_role_display() == "Staff", f"Expected 'Staff', got '{mary.get_role_display()}'"
    
    chloe = users['o56789']
    assert chloe.get_role_display() == "Others", f"Expected 'Others', got '{chloe.get_role_display()}'"
    
    print("✓ All role display tests passed!")


def test_library_staff_detection():
    """Test library staff detection"""
    print("\n=== Testing Library Staff Detection ===")
    users = user.load_users('data/users.csv')
    
    # Mary is library staff
    mary = users['e118102']
    assert isinstance(mary, user.Staff), "Mary should be Staff"
    assert mary.is_library_staff(), "Mary should be library staff"
    print("✓ Mary correctly identified as library staff")
    
    # Lan is not library staff
    lan = users['e45261']
    assert isinstance(lan, user.Staff), "Lan should be Staff"
    assert not lan.is_library_staff(), "Lan should not be library staff"
    print("✓ Lan correctly identified as non-library staff")
    
    # Mashid is library staff
    mashid = users['e23456']
    assert isinstance(mashid, user.Staff), "Mashid should be Staff"
    assert mashid.is_library_staff(), "Mashid should be library staff"
    print("✓ Mashid correctly identified as library staff")
    
    print("✓ All library staff detection tests passed!")


def run_all_tests():
    """Run all test suites"""
    print("=" * 60)
    print("RUNNING LIBRARY MANAGEMENT SYSTEM TESTS")
    print("=" * 60)
    
    try:
        test_user_loading()
        test_book_loading()
        test_loan_loading()
        test_loan_counts()
        test_available_books()
        test_user_policies()
        test_date_parsing()
        test_library_report()
        test_role_display()
        test_library_staff_detection()
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        return True
        
    except AssertionError as e:
        print("\n" + "=" * 60)
        print(f"❌ TEST FAILED: {e}")
        print("=" * 60)
        return False
    except Exception as e:
        print("\n" + "=" * 60)
        print(f"❌ ERROR: {e}")
        print("=" * 60)
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)

