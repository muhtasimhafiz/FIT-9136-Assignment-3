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


def format_date(date_obj: datetime.datetime) -> str:
    """Format datetime object to dd/mm/yyyy string"""
    return date_obj.strftime('%d/%m/%Y')


def calculate_fine(due_date_str: str, return_date_str: str, book_type: str) -> float:
    """
    Calculate fine for an overdue book.
    Only physical books incur fines.
    Fine is $0.50 per day after due date.
    
    Args:
        due_date_str: Due date in dd/mm/yyyy format
        return_date_str: Return date in dd/mm/yyyy format (or TODAY if still borrowed)
        book_type: 'physical' or 'online'
    
    Returns:
        Fine amount in dollars
    """
    # Online books don't have fines
    if book_type != 'physical':
        return 0.0
    
    due_date = parse_date(due_date_str)
    return_date = parse_date(return_date_str)
    
    # Calculate days overdue (only count days after due date)
    days_overdue = (return_date - due_date).days
    
    if days_overdue > 0:
        return days_overdue * 0.50
    return 0.0


def get_user_fines(loans: list, books: dict, user_id: str) -> float:
    """
    Calculate total fines for a user.
    Includes fines for:
    - Returned books that were overdue
    - Active loans that are currently overdue (as of TODAY)
    
    Args:
        loans: List of all loan records
        books: Dictionary of book objects
        user_id: User ID to calculate fines for
    
    Returns:
        Total fines in dollars
    """
    total_fines = 0.0
    today = user.TODAY
    
    # Get all loans for this user
    user_loans = [loan for loan in loans if loan.get('user_id') == user_id]
    
    for loan in user_loans:
        book_id = loan['book_id']
        book_obj = books.get(book_id)
        
        if not book_obj:
            continue
        
        # Only physical books have fines
        if not book_obj.is_physical():
            continue
        
        due_date_str = loan['due_date']
        return_date_str = loan.get('return_date', '')
        
        if return_date_str:
            # Book has been returned - check if it was overdue
            fine = calculate_fine(due_date_str, return_date_str, 'physical')
            total_fines += fine
        else:
            # Book is still on loan - check if it's currently overdue
            fine = calculate_fine(due_date_str, today, 'physical')
            total_fines += fine
    
    return total_fines


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


def get_available_copies(book_id: str, books: dict, loans: list) -> int:
    """
    Get number of available copies for a specific book.
    For online books, always return 0 (unlimited access).
    
    Args:
        book_id: Book ID to check
        books: Dictionary of book objects
        loans: List of all loan records
    
    Returns:
        Number of available copies
    """
    book_obj = books.get(book_id)
    if not book_obj:
        return 0
    
    # Online books show 0/0 (unlimited access)
    if book_obj.is_online():
        return 0
    
    # Count active loans for this book
    active_loans_for_book = sum(1 for loan in get_active_loans(loans) 
                               if loan['book_id'] == book_id)
    
    # Available copies = total - borrowed
    return book_obj.total_copies - active_loans_for_book


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
    print("4. Borrow and Return")
    
    # Show Library Report option only for Library staff
    if isinstance(current_user, user.Staff) and current_user.is_library_staff():
        print("5. Library Report")
    
    print("==================================")


def view_account_policies(current_user: user.User, loans: list, books: dict):
    """Display user's account policies, current loans, and fines"""
    total, physical, online = get_user_loans_count(loans, current_user.user_id)
    role_display = current_user.get_role_display()
    max_days = current_user.get_max_days()
    max_items = current_user.get_max_items()
    
    # Calculate fines
    fines = get_user_fines(loans, books, current_user.user_id)
    
    print(f"{role_display} {current_user.name}. Policies: maximum of {max_days} days, {max_items} items. Current loans: {total} ({physical} physical / {online} online). Fines: $ {fines:.2f}")


def view_my_loans(current_user: user.User, loans: list, books: dict):
    """Display user's active loans sorted by due date"""
    active_loans = get_active_loans(loans, current_user.user_id)
    
    # Sort by due date
    active_loans.sort(key=lambda x: parse_date(x['due_date']))
    
    print(f"You are currently have {len(active_loans)} loan(s).")
    
    for idx, loan in enumerate(active_loans, 1):
        book_obj = books[loan['book_id']]
        print(f"{idx}. {book_obj.book_id} '{book_obj.title}' by {book_obj.author} ({book_obj.year}). Due date: {loan['due_date']}.")


def search_books(query: str, books: dict) -> list:
    """
    Search for books by exact title or book ID.
    Returns list of matching book IDs sorted by book ID.
    
    Args:
        query: Search query (can be title or book ID)
        books: Dictionary of book objects
    
    Returns:
        List of matching book IDs sorted
    """
    matches = []
    query_lower = query.lower()
    
    for book_id, book_obj in books.items():
        # Check if query matches book ID (case insensitive)
        if book_id.lower() == query_lower:
            matches.append(book_id)
        # Check if query matches exact title (case insensitive)
        elif query_lower == book_obj.title.lower():
            matches.append(book_id)
    
    # Sort by book ID
    matches.sort()
    return matches


def borrow_book(current_user: user.User, book_id: str, books: dict, loans: list):
    """
    Process borrowing a book.
    Validates eligibility and adds loan record.
    
    Args:
        current_user: User borrowing the book
        book_id: Book ID to borrow
        books: Dictionary of book objects
        loans: List of loan records (will be modified)
    
    Returns:
        True if successful, False otherwise
    """
    # Check if user has unpaid fines
    fines = get_user_fines(loans, books, current_user.user_id)
    if fines > 0:
        print("Borrowing unavailable: unpaid fines. Review your loan details for more info.")
        return False
    
    # Get book object first to check type
    book_obj = books.get(book_id)
    if not book_obj:
        print(f"Book {book_id} not found.")
        return False
    
    # Check quota - online books don't count toward quota
    # Only check quota when borrowing physical books
    if book_obj.is_physical():
        total_loans, physical_loans, online_loans = get_user_loans_count(loans, current_user.user_id)
        max_items = current_user.get_max_items()
        
        # Use physical_loans, not total_loans, since online books don't count
        if physical_loans >= max_items:
            print("Borrowing unavailable: quota reached. Review your loan details for more info.")
            return False
    
    # Check if book exists
    if book_id not in books:
        print(f"Book {book_id} not found.")
        return False
    
    # Check if copies are available (for physical books)
    if book_obj.is_physical():
        available = get_available_copies(book_id, books, loans)
        if available <= 0:
            print("No copies available.")
            return False
    
    # Calculate due date
    today = parse_date(user.TODAY)
    max_days = current_user.get_max_days()
    due_date = today + datetime.timedelta(days=max_days)
    due_date_str = format_date(due_date)
    
    # Add loan record
    new_loan = {
        'user_id': current_user.user_id,
        'book_id': book_id,
        'borrow_date': user.TODAY,
        'due_date': due_date_str,
        'return_date': ''
    }
    loans.append(new_loan)
    
    print(f"You have borrowed '{book_obj.title}' by {book_obj.author} ({book_obj.year}). Due: {due_date_str}.")
    return True


def return_book(current_user: user.User, book_id: str, books: dict, loans: list):
    """
    Process returning a book.
    Calculates and displays fines if applicable.
    
    Args:
        current_user: User returning the book
        book_id: Book ID to return
        books: Dictionary of book objects
        loans: List of loan records (will be modified)
    
    Returns:
        True if successful, False otherwise
    """
    # Find active loan for this book (earliest due date if multiple)
    user_active_loans = [loan for loan in get_active_loans(loans, current_user.user_id)
                         if loan['book_id'] == book_id]
    
    if not user_active_loans:
        print(f"No loan record for {book_id}.")
        return False
    
    # Sort by due date and take the earliest
    user_active_loans.sort(key=lambda x: parse_date(x['due_date']))
    loan_to_return = user_active_loans[0]
    
    # Get book details
    book_obj = books.get(book_id)
    if not book_obj:
        print(f"Book {book_id} not found.")
        return False
    
    # Set return date to today
    today = user.TODAY
    loan_to_return['return_date'] = today
    
    # Calculate fine if applicable
    fine = calculate_fine(loan_to_return['due_date'], today, 
                         'physical' if book_obj.is_physical() else 'online')
    
    if fine > 0:
        # Calculate days overdue
        due_date = parse_date(loan_to_return['due_date'])
        return_date = parse_date(today)
        days_overdue = (return_date - due_date).days
        print(f"Returned '{book_obj.title}' by {book_obj.author} ({book_obj.year}). Overdue by {days_overdue} day(s). Fine: $ {fine:.2f}")
    else:
        print(f"Returned '{book_obj.title}' by {book_obj.author} ({book_obj.year}).")
    
    return True


def borrow_and_return_console(current_user: user.User, books: dict, loans: list):
    """
    Interactive console for borrowing and returning books.
    Commands: borrow <query>, return <book_id>, quit
    
    Args:
        current_user: Currently logged in user
        books: Dictionary of book objects
        loans: List of loan records
    """
    while True:
        command_line = input("> ")
        
        # Parse command
        parts = command_line.strip().split(maxsplit=1)
        
        if not parts:
            continue
        
        command = parts[0].lower()
        
        if command == 'quit':
            break
        elif command == 'borrow':
            if len(parts) < 2:
                continue
            
            query = parts[1]
            
            # Search for books
            matching_books = search_books(query, books)
            
            if not matching_books:
                print(f"No books match '{query}'.")
                continue
            
            # Display matching books
            print(f"Found {len(matching_books)} book(s).")
            for book_id in matching_books:
                book_obj = books[book_id]
                book_type = 'online' if book_obj.is_online() else 'physical'
                available = get_available_copies(book_id, books, loans)
                total = book_obj.total_copies
                print(f"- {book_id} ({book_type}) '{book_obj.title}' by {book_obj.author} ({book_obj.year}). Available copies: {available}/{total}.")
            
            # Confirm book ID
            while True:
                confirmed_id = input("Confirm the Book ID you'd like to borrow: ")
                
                if confirmed_id.lower() == 'quit':
                    break
                
                if confirmed_id in matching_books:
                    # Attempt to borrow
                    borrow_book(current_user, confirmed_id, books, loans)
                    break
                # If invalid ID, keep asking (loop continues)
        
        elif command == 'return':
            if len(parts) < 2:
                continue
            
            book_id = parts[1]
            
            # Attempt to return
            return_book(current_user, book_id, books, loans)
        
        # Invalid command - just continue


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
                view_account_policies(current_user, loans, books)
                display_menu(current_user)  # Re-display menu after action
            elif choice == '3':
                view_my_loans(current_user, loans, books)
                display_menu(current_user)  # Re-display menu after action
            elif choice == '4':
                # Borrow and Return
                borrow_and_return_console(current_user, books, loans)
                display_menu(current_user)  # Re-display menu after action
            elif choice == '5':
                # Library Report (only for Library staff)
                if isinstance(current_user, user.Staff) and current_user.is_library_staff():
                    library_report(users, books, loans)
                    display_menu(current_user)  # Re-display menu after action
                # If not Library staff, this is invalid choice - do nothing (will re-prompt)
            # For invalid choices, just loop again and re-prompt (no menu re-display)


if __name__ == "__main__":
    main('data/users.csv', 'data/books.csv', 'data/loans.csv')

