# Task 2 - Usage Guide

## How to Run

### Main Program
```bash
cd set-1
python task2.py
```

### Quick Verification Test
```bash
cd set-1
python TASK2_QUICK_TEST.py
```

## Available Test Scripts

### Automated Test Cases
1. `test_task2_example1.py` - Chris Manner with fines
2. `test_task2_example2.py` - Mary Alan staff borrowing
3. `test_task2_example3.py` - Noah quota limits
4. `test_task2_example4.py` - Library report

## User Credentials for Testing

### Students
- **Chris Manner**: s31267 / chr1267 (has $1.00 fine)
- **Justin Bierber**: s31245 / secure99
- **Dao Lee**: s41267 / pass123
- **Mia**: s24567 / qwerty88

### Staff
- **Mary Alan**: e118102 / pa55word (Library staff)
- **Mashid Saga**: e23456 / gogogo (Library staff)
- **Lan Nguyen**: e45261 / readmore (Business staff)

### Others
- **Noah**: o56799 / noa6799
- **Chloe**: o56789 / hackme

## Borrow and Return Console Commands

### Borrow a Book
```
> borrow <book title or ID>
```

Examples:
- `borrow Python Crash Course` - Search by title
- `borrow P0003` - Borrow by book ID
- `borrow The Hobbit` - Search by exact title

### Return a Book
```
> return <book ID>
```

Examples:
- `return P0006` - Return physical book
- `return E0001` - Return online book

### Exit Console
```
> quit
```

## Menu Options

### All Users
- **0**: Quit program
- **1**: Log out
- **2**: View account policies (shows fines)
- **3**: View my loans
- **4**: Borrow and Return (new!)

### Library Staff Only
- **5**: Library Report (new!)

## Fine System

### Fine Rate
- **$0.50 per day** for overdue physical books
- **Online books**: No fines (access revoked automatically)

### When Fines Apply
- Physical books returned after due date
- Physical books still on loan past due date

### Fine Examples
- Book due 13/09/2025, today is 15/09/2025: **2 days × $0.50 = $1.00**
- Online book (any overdue): **$0.00**

## Borrowing Rules

### Quota Limits
- **Students**: 4 items, 10 days
- **Staff**: 6 items, 14 days
- **Others**: 2 items, 7 days
- **Note**: Online books don't count toward quota

### Borrowing Validation (in order)
1. User must have available quota
2. User must have no outstanding fines
3. Book must exist in catalog
4. Book must have available copies (physical only)

### Cannot Borrow When:
- You have unpaid fines
- You've reached your quota
- No copies available (physical books)
- Book doesn't exist

## Return Rules

### What Happens on Return
1. Return date set to TODAY (15/09/2025)
2. Fine calculated if overdue (physical books only)
3. Display confirmation with fine amount (if applicable)

### Multiple Copies
If you borrowed multiple copies of the same book, the system returns the one with the earliest due date first.

## Example Session

```
Welcome to Library
Login as: o56799
Password: noa6799
Logged in as Noah (Others)
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
4. Borrow and Return
==================================
Enter your choice: 4
> borrow Python Crash Course
Found 2 book(s).
- E0001 (online) 'Python Crash Course' by Eric Matthes (2015). Available copies: 0/0.
- P0003 (physical) 'Python Crash Course' by Eric Matthes (2023). Available copies: 2/2.
Confirm the Book ID you'd like to borrow: P0003
You have borrowed 'Python Crash Course' by Eric Matthes (2023). Due: 22/09/2025.
> quit
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
4. Borrow and Return
==================================
Enter your choice: 0
Goodbye!
```

## Troubleshooting

### "No books match '<title>'"
- Book title must match exactly (case-insensitive)
- Try the full title: "The Hobbit" not "Hobbit"
- Or use the book ID directly: "P0008"

### "Borrowing unavailable: unpaid fines"
- Return your overdue books first
- Fines are shown in "View account policies" (option 2)

### "Borrowing unavailable: quota reached"
- Return some books to free up quota
- Check your loans with option 3

### "No copies available"
- All physical copies are currently borrowed
- Wait for someone to return the book
- Online books (E####) are always available

### "No loan record for <book_id>"
- You haven't borrowed this book
- Check your active loans with option 3

## Important Notes

1. **TODAY is set to 15/09/2025** for this assignment
2. **Book search requires exact title match** (not substring)
3. **Online books show 0/0 copies** (unlimited access)
4. **Invalid commands are silently ignored** in the console
5. **Invalid menu choices re-prompt** without showing menu again

## Files Structure

```
set-1/
├── task2.py                    # Main implementation
├── user.py                     # User classes
├── book.py                     # Book class
├── data/
│   ├── users.csv              # User data
│   ├── books.csv              # Book catalog
│   └── loans.csv              # Loan records
├── test_task2_example1.py     # Test case 1
├── test_task2_example2.py     # Test case 2
├── test_task2_example3.py     # Test case 3
├── test_task2_example4.py     # Test case 4
├── TASK2_QUICK_TEST.py        # Quick verification
├── TASK2_IMPLEMENTATION_SUMMARY.md
└── TASK2_USAGE_GUIDE.md       # This file
```

## Success Criteria

All examples produce correct output matching the specification:
- ✓ Example 1: Fines and returns
- ✓ Example 2: Staff borrowing and availability
- ✓ Example 3: Quota enforcement
- ✓ Example 4: Library report

## Support

If you encounter any issues:
1. Check the implementation summary: `TASK2_IMPLEMENTATION_SUMMARY.md`
2. Run the quick test: `python TASK2_QUICK_TEST.py`
3. Review the test cases in `test_task2_example*.py`

