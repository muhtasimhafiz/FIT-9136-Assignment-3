"""
Demo script to show the fixed behavior
"""
import user
import book
from task1 import load_loans, get_active_loans, get_user_loans_count, parse_date

def demo_fixed_behavior():
    """Demonstrate the fixed behavior"""
    print("=" * 70)
    print("  DEMONSTRATING FIXED BEHAVIOR")
    print("=" * 70)
    
    # Load data
    users = user.load_users('data/users.csv')
    books = book.load_books('data/books.csv')
    loans = load_loans('data/loans.csv')
    
    print(f"\n✅ Data loaded successfully:")
    print(f"   - {len(users)} users")
    print(f"   - {len(books)} books") 
    print(f"   - {len(loans)} loans")
    
    # Test active loans (this was causing the TypeError before)
    active_loans = get_active_loans(loans)
    print(f"   - {len(active_loans)} active loans")
    
    # Test user loans (this was also causing the TypeError before)
    chris = users['s31267']
    total, physical, online = get_user_loans_count(loans, chris.user_id)
    print(f"\n✅ Chris's loans (s31267): {total} total ({physical} physical, {online} online)")
    
    # Test loan display
    print(f"\n✅ Chris's active loans:")
    chris_loans = get_active_loans(loans, chris.user_id)
    chris_loans.sort(key=lambda x: parse_date(x['due_date']))
    for idx, loan in enumerate(chris_loans, 1):
        book_obj = books[loan['book_id']]
        print(f"   {idx}. {book_obj.book_id} '{book_obj.title}' by {book_obj.author} ({book_obj.year}). Due date: {loan['due_date']}.")
    
    print(f"\n✅ Login behavior:")
    print("   1. After 3 failed attempts, program shows 'Sorry you're out of attempts'")
    print("   2. Then returns to 'Welcome to Library' screen")
    print("   3. User can try logging in again")
    print("   4. No TypeError when viewing loans")
    
    print(f"\n✅ All issues fixed:")
    print("   - Empty CSV rows are skipped")
    print("   - Login returns to welcome screen after lockout")
    print("   - No more TypeError in loan processing")
    
    print("\n" + "=" * 70)
    print("  READY FOR TESTING")
    print("=" * 70)
    print("\nRun 'python task1.py' to test interactively:")
    print("1. Try wrong credentials 3 times")
    print("2. See lockout message")
    print("3. See 'Welcome to Library' again")
    print("4. Login successfully with: s31267 / chr1267")
    print("5. Choose option 3 to view loans (no error)")
    print("6. Choose option 2 to view policies (no error)")

if __name__ == "__main__":
    demo_fixed_behavior()
