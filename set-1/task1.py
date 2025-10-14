import user
import book
import csv
import datetime
import typing


def load_loans(loan_file: str) -> list:
    """Load loans from CSV file and return a list of loan dictionaries"""
    loans = []
    with open(loan_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Skip empty rows - check if any required fields are empty
            if not row.get('user_id') or not row.get('book_id') or not row.get('borrow_date'):
                continue
            loans.append({
                'user_id': row['user_id'],
                'book_id': row['book_id'],
                'borrow_date': row['borrow_date'],
                'due_date': row['due_date'],
                'return_date': row.get('return_date', '')  # Use get with default empty string
            })
    return loans


def get_active_loans(loans: list, user_id: str = None) -> list:
    """Get active loans (not returned) for a user or all users"""
    active = []
    for loan in loans:
        # Ensure loan is a dictionary
        if not isinstance(loan, dict):
            continue
        # Check if return_date is empty (active loan)
        if loan.get('return_date', '') == '':
            if user_id is None or loan.get('user_id') == user_id:
                active.append(loan)
    return active


def parse_date(date_str: str) -> datetime.datetime:
    """Parse date string in dd/mm/yyyy format"""
    return datetime.datetime.strptime(date_str, '%d/%m/%Y')


def get_user_loans_count(loans: list, user_id: str) -> tuple:
    """Get count of active loans (total, physical, online) for a user"""
    active_loans = get_active_loans(loans, user_id)
    total = len(active_loans)
    physical = sum(1 for loan in active_loans if loan['book_id'].startswith('P'))
    online = sum(1 for loan in active_loans if loan['book_id'].startswith('E'))
    return total, physical, online


def get_available_books_count(books: dict, loans: list) -> int:
    """Get count of physical books with at least one available copy"""
    available_count = 0
    for book_id, book_obj in books.items():
        if book_obj.is_physical():
            # Count active loans for this book
            active_loans_for_book = sum(1 for loan in get_active_loans(loans) 
                                       if loan['book_id'] == book_id)
            # Available copies = total - borrowed
            available_copies = book_obj.total_copies - active_loans_for_book
            if available_copies > 0:
                available_count += 1
    return available_count


def login(users: dict) -> typing.Optional[user.User]:
    """Handle user login with 3 attempts"""
    attempts = 3
    
    while attempts > 0:
        user_id = input("Login as: ")
        
        if user_id.lower() == 'quit':
            print("Goodbye!")
            return "quit"  # Special return value to indicate quit
        
        password = input("Password: ")
        
        # Check if user exists and password matches
        if user_id in users and users[user_id].password == password:
            return users[user_id]
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Invalid credentials. {attempts} attempt(s) remaining.")
            else:
                print("Sorry you're out of attempts. Please contact your librarian for assistance.")
                return None  # Return None to go back to main loop
    
    return None


def display_menu(current_user: user.User):
    """Display menu based on user role"""
    print("==================================")
    print("My Library Account")
    print("0. Quit")
    print("1. Log out")
    print("2. View account policies")
    print("3. View my loans")
    
    # Show Library Report option only for Library staff
    if isinstance(current_user, user.Staff) and current_user.is_library_staff():
        print("4. Library Report")
    
    print("==================================")


def view_account_policies(current_user: user.User, loans: list):
    """Display user's account policies and current loans"""
    total, physical, online = get_user_loans_count(loans, current_user.user_id)
    role_display = current_user.get_role_display()
    max_days = current_user.get_max_days()
    max_items = current_user.get_max_items()
    
    print(f"{role_display} {current_user.name}. Policies: maximum of {max_days} days, {max_items} items. Current loans: {total} ({physical} physical / {online} online).")


def view_my_loans(current_user: user.User, loans: list, books: dict):
    """Display user's active loans sorted by due date"""
    active_loans = get_active_loans(loans, current_user.user_id)
    
    # Sort by due date
    active_loans.sort(key=lambda x: parse_date(x['due_date']))
    
    print(f"You are currently have {len(active_loans)} loan(s).")
    
    for idx, loan in enumerate(active_loans, 1):
        book_obj = books[loan['book_id']]
        print(f"{idx}. {book_obj.book_id} '{book_obj.title}' by {book_obj.author} ({book_obj.year}). Due date: {loan['due_date']}.")


def library_report(users: dict, books: dict, loans: list):
    """Display library statistics (for Library staff only)"""
    # Count users by role
    students = sum(1 for u in users.values() if isinstance(u, user.Student))
    staff = sum(1 for u in users.values() if isinstance(u, user.Staff))
    others = sum(1 for u in users.values() if isinstance(u, user.Others))
    total_users = len(users)
    
    # Count books by type
    physical_books = sum(1 for b in books.values() if b.is_physical())
    online_books = sum(1 for b in books.values() if b.is_online())
    total_books = len(books)
    
    # Count available physical books
    available_physical = get_available_books_count(books, loans)
    
    print("Library report")
    print(f"- {total_users} users, including {students} student(s), {staff} staff, and {others} others.")
    print(f"- {total_books} books, including {physical_books} physical book(s) ({available_physical} currently available) and {online_books} online book(s).")


def main(user_file: str, book_file:str, loan_file:str) -> None:
    """
    This is the entry of your program. Please DO NOT modify this function signature, i.e. function name, parameters
    Parameteres:
    - user_file (str): path the `users.csv` which stores user information
    - book_file (str): path the `books.csv` which stores book information
    - loan_file (str): path the `loans.csv` which stores loan information
    """
    # Load data
    users = user.load_users(user_file)
    books = book.load_books(book_file)
    loans = load_loans(loan_file)
    
    # Main program loop
    while True:
        print("Welcome to Library")
        current_user = login(users)
        
        if current_user == "quit":
            return  # Exit the program
        elif current_user is None:
            continue  # Go back to welcome screen for another login attempt
        
        print(f"Logged in as {current_user.name} ({current_user.get_role_display()})")
        
        # Display menu once
        display_menu(current_user)
        
        # User menu loop
        while True:
            choice = input("Enter your choice: ")
            
            if choice == '0':
                print("Goodbye!")
                return
            elif choice == '1':
                # Log out
                break
            elif choice == '2':
                view_account_policies(current_user, loans)
                display_menu(current_user)  # Re-display menu after action
            elif choice == '3':
                view_my_loans(current_user, loans, books)
                display_menu(current_user)  # Re-display menu after action
            elif choice == '4':
                # Library Report (only for Library staff)
                if isinstance(current_user, user.Staff) and current_user.is_library_staff():
                    library_report(users, books, loans)
                    display_menu(current_user)  # Re-display menu after action
                # If not Library staff, this is invalid choice - do nothing (will re-prompt)
            # For invalid choices, just loop again and re-prompt (no menu re-display)


if __name__ == "__main__":
    main('data/users.csv', 'data/books.csv', 'data/loans.csv')
