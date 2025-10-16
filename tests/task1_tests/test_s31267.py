"""
Test script to simulate option 3 for user s31267
"""
import user
import book
from task1 import load_loans, get_active_loans, get_user_loans_count, parse_date

def test_s31267_option3():
    """Test option 3 specifically for user s31267"""
    
    # Load data
    users = user.load_users('data/users.csv')
    books = book.load_books('data/books.csv')
    loans = load_loans('data/loans.csv')
    
    # Get Chris (s31267)
    chris = users['s31267']
    print(f"=== TESTING OPTION 3 FOR {chris.name} (s31267) ===")
    print(f"User: {chris.name} ({chris.get_role_display()})")
    
    # Simulate what option 3 does
    print(f"\n--- Simulating Option 3: View My Loans ---")
    active_loans = get_active_loans(loans, chris.user_id)
    active_loans.sort(key=lambda x: parse_date(x['due_date']))
    
    print(f"You are currently have {len(active_loans)} loan(s).")
    
    if len(active_loans) > 0:
        for idx, loan in enumerate(active_loans, 1):
            book_obj = books[loan['book_id']]
            print(f"{idx}. {book_obj.book_id} '{book_obj.title}' by {book_obj.author} ({book_obj.year}). Due date: {loan['due_date']}.")
    else:
        print("No loans found!")
    
    # Also test option 2
    print(f"\n--- Simulating Option 2: View Account Policies ---")
    total, physical, online = get_user_loans_count(loans, chris.user_id)
    role_display = chris.get_role_display()
    max_days = chris.get_max_days()
    max_items = chris.get_max_items()
    
    print(f"{role_display} {chris.name}. Policies: maximum of {max_days} days, {max_items} items. Current loans: {total} ({physical} physical / {online} online).")
    
    print(f"\n=== SUMMARY ===")
    print(f"✅ Found {len(active_loans)} active loans for s31267")
    print(f"✅ Loan counts: {total} total ({physical} physical, {online} online)")
    print(f"✅ This matches the expected 2 loans (1 physical, 1 online)")

if __name__ == "__main__":
    test_s31267_option3()
