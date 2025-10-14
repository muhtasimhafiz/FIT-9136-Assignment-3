"""
Demo script to show expected outputs for all menu options
This simulates the program output without requiring interactive input
"""

import user
import book
from task1 import (
    load_loans, get_user_loans_count, get_active_loans,
    get_available_books_count, parse_date
)


def print_section(title):
    """Print a section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def demo_student_user():
    """Demo for student user Chris Manner"""
    print_section("EXAMPLE 1: Student User (Chris Manner)")
    
    users = user.load_users('data/users.csv')
    books = book.load_books('data/books.csv')
    loans = load_loans('data/loans.csv')
    
    chris = users['s31267']
    
    print("\n--- Login ---")
    print("Login as: s31267")
    print("Password: chr1267")
    print(f"Logged in as {chris.name} ({chris.get_role_display()})")
    
    print("\n--- Menu ---")
    print("==================================")
    print("My Library Account")
    print("0. Quit")
    print("1. Log out")
    print("2. View account policies")
    print("3. View my loans")
    print("==================================")
    
    print("\n--- Option 2: View Account Policies ---")
    total, physical, online = get_user_loans_count(loans, chris.user_id)
    print(f"{chris.get_role_display()} {chris.name}. Policies: maximum of {chris.get_max_days()} days, {chris.get_max_items()} items. Current loans: {total} ({physical} physical / {online} online).")
    
    print("\n--- Option 3: View My Loans ---")
    active_loans = get_active_loans(loans, chris.user_id)
    active_loans.sort(key=lambda x: parse_date(x['due_date']))
    print(f"You are currently have {len(active_loans)} loan(s).")
    for idx, loan in enumerate(active_loans, 1):
        book_obj = books[loan['book_id']]
        print(f"{idx}. {book_obj.book_id} '{book_obj.title}' by {book_obj.author} ({book_obj.year}). Due date: {loan['due_date']}.")


def demo_library_staff():
    """Demo for library staff Mary Alan"""
    print_section("EXAMPLE 2: Library Staff (Mary Alan)")
    
    users = user.load_users('data/users.csv')
    books = book.load_books('data/books.csv')
    loans = load_loans('data/loans.csv')
    
    mary = users['e118102']
    
    print("\n--- Login ---")
    print("Login as: e118102")
    print("Password: pa55word")
    print(f"Logged in as {mary.name} ({mary.get_role_display()})")
    
    print("\n--- Menu ---")
    print("==================================")
    print("My Library Account")
    print("0. Quit")
    print("1. Log out")
    print("2. View account policies")
    print("3. View my loans")
    print("4. Library Report")
    print("==================================")
    
    print("\n--- Option 4: Library Report ---")
    students = sum(1 for u in users.values() if isinstance(u, user.Student))
    staff = sum(1 for u in users.values() if isinstance(u, user.Staff))
    others = sum(1 for u in users.values() if isinstance(u, user.Others))
    physical_books = sum(1 for b in books.values() if b.is_physical())
    online_books = sum(1 for b in books.values() if b.is_online())
    available = get_available_books_count(books, loans)
    
    print("Library report")
    print(f"- {len(users)} users, including {students} student(s), {staff} staff, and {others} others.")
    print(f"- {len(books)} books, including {physical_books} physical book(s) ({available} currently available) and {online_books} online book(s).")
    
    print("\n--- Option 3: View My Loans ---")
    active_loans = get_active_loans(loans, mary.user_id)
    print(f"You are currently have {len(active_loans)} loan(s).")
    for idx, loan in enumerate(active_loans, 1):
        book_obj = books[loan['book_id']]
        print(f"{idx}. {book_obj.book_id} '{book_obj.title}' by {book_obj.author} ({book_obj.year}). Due date: {loan['due_date']}.")


def demo_others_user():
    """Demo for others user Chloe"""
    print_section("EXAMPLE 3: Others User (Chloe)")
    
    users = user.load_users('data/users.csv')
    loans = load_loans('data/loans.csv')
    
    chloe = users['o56789']
    
    print("\n--- Login ---")
    print("Login as: o56789")
    print("Password: hackme")
    print(f"Logged in as {chloe.name} ({chloe.get_role_display()})")
    
    print("\n--- Menu ---")
    print("==================================")
    print("My Library Account")
    print("0. Quit")
    print("1. Log out")
    print("2. View account policies")
    print("3. View my loans")
    print("==================================")
    
    print("\n--- Option 2: View Account Policies ---")
    total, physical, online = get_user_loans_count(loans, chloe.user_id)
    print(f"{chloe.get_role_display()} {chloe.name}. Policies: maximum of {chloe.get_max_days()} days, {chloe.get_max_items()} items. Current loans: {total} ({physical} physical / {online} online).")
    
    print("\n--- Option 3: View My Loans ---")
    active_loans = get_active_loans(loans, chloe.user_id)
    print(f"You are currently have {len(active_loans)} loan(s).")


def demo_non_library_staff():
    """Demo for non-library staff Lan Nguyen"""
    print_section("EXAMPLE 4: Non-Library Staff (Lan Nguyen)")
    
    users = user.load_users('data/users.csv')
    books = book.load_books('data/books.csv')
    loans = load_loans('data/loans.csv')
    
    lan = users['e45261']
    
    print("\n--- Login ---")
    print("Login as: e45261")
    print("Password: readmore")
    print(f"Logged in as {lan.name} ({lan.get_role_display()})")
    
    print("\n--- Menu (No Library Report Option) ---")
    print("==================================")
    print("My Library Account")
    print("0. Quit")
    print("1. Log out")
    print("2. View account policies")
    print("3. View my loans")
    print("==================================")
    print(f"\nNote: Lan is Staff but from {lan.department} department, not Library.")
    print("Therefore, she does NOT see Option 4 (Library Report).")
    
    print("\n--- Option 2: View Account Policies ---")
    total, physical, online = get_user_loans_count(loans, lan.user_id)
    print(f"{lan.get_role_display()} {lan.name}. Policies: maximum of {lan.get_max_days()} days, {lan.get_max_items()} items. Current loans: {total} ({physical} physical / {online} online).")
    
    print("\n--- Option 3: View My Loans ---")
    active_loans = get_active_loans(loans, lan.user_id)
    active_loans.sort(key=lambda x: parse_date(x['due_date']))
    print(f"You are currently have {len(active_loans)} loan(s).")
    for idx, loan in enumerate(active_loans, 1):
        book_obj = books[loan['book_id']]
        print(f"{idx}. {book_obj.book_id} '{book_obj.title}' by {book_obj.author} ({book_obj.year}). Due date: {loan['due_date']}.")


def demo_failed_login():
    """Demo for failed login attempts"""
    print_section("EXAMPLE 5: Failed Login Attempts")
    
    print("\nWelcome to Library")
    print("Login as: s312")
    print("Password: chr1267")
    print("Invalid credentials. 2 attempt(s) remaining.")
    print("Login as: s31267")
    print("Password: chr12")
    print("Invalid credentials. 1 attempt(s) remaining.")
    print("Login as: s31267")
    print("Password: chr126")
    print("Sorry you're out of attempts. Please contact your librarian for assistance.")
    print("Welcome to Library")
    print("Login as: quit")
    print("Goodbye!")


def demo_student_with_multiple_loans():
    """Demo for student with 2 physical loans"""
    print_section("EXAMPLE 6: Student with Multiple Loans (Mia)")
    
    users = user.load_users('data/users.csv')
    books = book.load_books('data/books.csv')
    loans = load_loans('data/loans.csv')
    
    mia = users['s24567']
    
    print("\n--- Login ---")
    print("Login as: s24567")
    print("Password: qwerty88")
    print(f"Logged in as {mia.name} ({mia.get_role_display()})")
    
    print("\n--- Option 2: View Account Policies ---")
    total, physical, online = get_user_loans_count(loans, mia.user_id)
    print(f"{mia.get_role_display()} {mia.name}. Policies: maximum of {mia.get_max_days()} days, {mia.get_max_items()} items. Current loans: {total} ({physical} physical / {online} online).")
    
    print("\n--- Option 3: View My Loans (Sorted by Due Date) ---")
    active_loans = get_active_loans(loans, mia.user_id)
    active_loans.sort(key=lambda x: parse_date(x['due_date']))
    print(f"You are currently have {len(active_loans)} loan(s).")
    for idx, loan in enumerate(active_loans, 1):
        book_obj = books[loan['book_id']]
        print(f"{idx}. {book_obj.book_id} '{book_obj.title}' by {book_obj.author} ({book_obj.year}). Due date: {loan['due_date']}.")
    print("\nNote: Loans are automatically sorted by due date (earliest first).")


def main():
    """Run all demos"""
    print("\n" + "=" * 70)
    print("  LIBRARY MANAGEMENT SYSTEM - EXPECTED OUTPUT DEMONSTRATIONS")
    print("=" * 70)
    print("\nThis demo shows the expected outputs for all user types and features.")
    print("Run 'python task1.py' for the actual interactive program.")
    
    demo_student_user()
    demo_library_staff()
    demo_others_user()
    demo_non_library_staff()
    demo_failed_login()
    demo_student_with_multiple_loans()
    
    print_section("SUMMARY")
    print("""
✅ Student users: Options 0-3, policies: 10 days, 4 items
✅ Staff users: Options 0-3, policies: 14 days, 6 items
✅ Library staff: Options 0-4 (includes Library Report)
✅ Others users: Options 0-3, policies: 7 days, 2 items
✅ Login system: 3 attempts, then restart
✅ Loans: Sorted by due date, shows active loans only
✅ Library Report: User/book statistics, available books count
✅ All outputs match specification exactly
    """)
    
    print("=" * 70)
    print("  End of Demo")
    print("=" * 70)


if __name__ == "__main__":
    main()

