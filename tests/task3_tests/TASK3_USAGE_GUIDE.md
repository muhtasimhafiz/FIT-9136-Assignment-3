# Task 3 Usage Guide

## Quick Start

### Running the Program

```bash
cd set-1
python task3.py
```

### Running Tests

```bash
# Run all tests
cd set-1
python ..\tests\task3_tests\run_all_tests.py

# Run individual tests
python ..\tests\task3_tests\test_task3_example1.py
python ..\tests\task3_tests\test_task3_example2.py
python ..\tests\task3_tests\test_task3_example3.py
```

## New Features

### 1. Renew Loan (Option 4 Console)

#### For All Users

In the "Borrow and Return" console, use the `renew` command:

```
> renew P0008
```

#### Rules

- Extends due date by 5 days
- Can only renew each book once
- Cannot renew if you have unpaid fines from currently overdue books
- Cannot renew books that are already overdue (due date has passed or equals today)
- If you have multiple copies of the same book, renews the earliest due date first

#### Example Session

```
Welcome to Library
Login as: s31267
Password: chr1267
Enter your choice: 4
> borrow The Hobbit
Found 1 book(s).
- P0008 (physical) 'The Hobbit' by J.R.R. Tolkien (1937). Available copies: 1/2.
Confirm the Book ID you'd like to borrow: P0008
You have borrowed 'The Hobbit' by J.R.R. Tolkien (1937). Due: 25/09/2025.
> renew P0008
Renew 'The Hobbit' by J.R.R. Tolkien (1937) successfully. New due date: 30/09/2025
> quit
```

### 2. Search by Keywords (Option 5)

#### For All Users

Available to all users (students, staff, others).

#### How to Use

1. Select Option 5 from main menu
2. Enter keywords separated by commas
3. Results are sorted by:
   - Number of matched keywords (highest first)
   - Publication year (newest first)
   - Book ID (ascending)

#### Example Session

```
Enter your choice: 5
Enter search keywords (separated by comma): python,programming
Found 7 book(s).
1. P0003 'Python Crash Course' by Eric Matthes (2023).
2. P0001 'Introduction to Python Programming' by S Gowrishankar (2019).
3. E0002 'Deep learning with Python: a hands-on introduction' by Ketkar Nikhil (2017).
4. E0001 'Python Crash Course' by Eric Matthes (2015).
5. P0002 'Python Programming: An Introduction to Computer Science' by John M. Zelle (2002).
6. E0003 'Machine Learning for Business' by Doug Hudgeon & Richard Nichol (2020).
7. P0006 'Hands-On ML' by Aurelien Geron (2019).
```

#### Tips

- Keywords are case-insensitive
- Enter multiple keywords separated by commas
- Empty keyword list returns 0 results
- Books must match at least one keyword

### 3. Manage Library (Option 6)

#### For Library Staff Only

Only users with department "Library" can access this option.

#### Available Commands

- `report` - Display library statistics
- `add physical` - Add a new physical book
- `add online` - Add a new online book
- `quit` - Exit the console

#### Adding a Physical Book

```
> add physical
Title: A Concise and Practical Introduction to Programming Algorithms in Java
Authors: Nielsen Frank
Year: 2017
Copies: 1
Detected keywords: algorithms:programming
Adding P0020 'A Concise and Practical Introduction to Programming Algorithms in Java' by Nielsen Frank (2017).
```

#### Adding an Online Book

```
> add online
Title: Advanced Machine Learning
Authors: John Doe
Year: 2024
Detected keywords: ML
Adding E0005 'Advanced Machine Learning' by John Doe (2024).
```

#### Automatic Features

- **Book ID Generation**: Automatically generates unique IDs (P#### for physical, E#### for online)
- **Keyword Detection**: Matches words in the title with existing keywords in the database
- **Keywords Sorting**: Detected keywords are sorted alphabetically and displayed

#### Library Report

```
> report
Library report
- 9 users, including 4 student(s), 3 staff, and 2 others.
- 14 books, including 10 physical book(s) (7 currently available) and 4 online book(s).
```

## Test Users

### Students

- s31267 / chr1267 (Chris Manner) - Has overdue books initially
- s41267 / pass123 (Dao Lee)
- s31245 / secure99 (Justin Bierber)
- s24567 / qwerty88 (Mia)

### Staff

- e118102 / pa55word (Mary Alan) - Library staff
- e23456 / gogogo (Mashid Saga) - Library staff
- e45261 / readmore (Lan Nguyen) - Business staff (no Option 6)

### Others

- o56789 / hackme (Chloe)
- o56799 / noa6799 (Noah)

## Important Notes

### Fine System

- **Display Fines**: Shows all fines (including from returned books) in account policies
- **Blocking Fines**: Only currently overdue books block borrowing/renewal
- After returning all books, you can borrow again even if you had late return fines

### Overdue Rules

- A book is considered overdue on or after its due date
- For renewal: If today >= due_date, the book cannot be renewed
- For fines: Calculated as (return_date - due_date).days \* $0.50 for physical books

### Online Books

- Don't count toward borrowing quota
- No late fees
- Show "Available copies: 0/0" (unlimited access)
- Can be borrowed even when all physical quota is used

## Troubleshooting

### "Renewal denied: You have unpaid fines."

- You have currently overdue books
- Return all overdue books first, then try again

### "Renewal denied: This book is already overdue."

- The book's due date has passed or is today
- Return the book instead of renewing it

### "Renewal unavailable: Each book can only be renewed once."

- You've already renewed this book
- Cannot renew again

### "No loan record for {book_id}."

- You don't have an active loan for this book
- Check your loans with Option 3

### Option 6 not showing

- Only library staff can see this option
- Make sure you're logged in with a Library department staff account

## File Structure

```
set-1/
  ├── task3.py              # Main implementation
  ├── book.py               # Book class
  ├── user.py               # User classes
  └── data/
      ├── books.csv         # Book data
      ├── loans.csv         # Loan records
      └── users.csv         # User data

tests/task3_tests/
  ├── test_task3_example1.py
  ├── test_task3_example2.py
  ├── test_task3_example3.py
  ├── run_all_tests.py
  ├── README.md
  ├── IMPLEMENTATION_SUMMARY.md
  └── TASK3_USAGE_GUIDE.md
```

## Verification

All three example tests pass:
✓ Example 1 - Renew Loan
✓ Example 2 - Search by Keywords
✓ Example 3 - Manage Library

No linting errors detected.
