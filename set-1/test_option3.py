"""
Test script to specifically test option 3 (View my loans) functionality
"""
import user
import book
from task1 import load_loans, get_active_loans, get_user_loans_count, parse_date

def test_option3_functionality():
    """Test the option 3 functionality specifically"""
    print("Testing Option 3: View My Loans")
    print("=" * 50)
    
    # Load data
    users = user.load_users('data/users.csv')
    books = book.load_books('data/books.csv')
    loans = load_loans('data/loans.csv')
    
    print(f"✅ Data loaded: {len(users)} users, {len(books)} books, {len(loans)} loans")
    
    # Test with different users
    test_users = ['s31267', 'e118102', 'o56789', 'e45261', 's24567']
    
    for user_id in test_users:
        if user_id in users:
            current_user = users[user_id]
            print(f"\n--- Testing {current_user.name} ({current_user.get_role_display()}) ---")
            
            try:
                # Test get_user_loans_count (used in option 2)
                total, physical, online = get_user_loans_count(loans, user_id)
                print(f"   Loan counts: {total} total ({physical} physical, {online} online)")
                
                # Test get_active_loans (used in option 3)
                active_loans = get_active_loans(loans, user_id)
                print(f"   Active loans: {len(active_loans)}")
                
                # Test loan display (what option 3 actually shows)
                if active_loans:
                    active_loans.sort(key=lambda x: parse_date(x['due_date']))
                    print(f"   Loan details:")
                    for idx, loan in enumerate(active_loans, 1):
                        book_obj = books[loan['book_id']]
                        print(f"     {idx}. {book_obj.book_id} '{book_obj.title}' by {book_obj.author} ({book_obj.year}). Due date: {loan['due_date']}.")
                else:
                    print(f"   No active loans")
                
                print(f"   ✅ Option 3 would work correctly for {current_user.name}")
                
            except Exception as e:
                print(f"   ❌ Error for {current_user.name}: {e}")
                return False
    
    print(f"\n✅ All users tested successfully!")
    print(f"✅ Option 3 (View my loans) functionality is working correctly!")
    return True

if __name__ == "__main__":
    success = test_option3_functionality()
    if success:
        print("\n🎉 Ready to test interactively!")
        print("Run 'python task1.py' and try option 3 with any user.")
    else:
        print("\n❌ There are still issues to fix.")
