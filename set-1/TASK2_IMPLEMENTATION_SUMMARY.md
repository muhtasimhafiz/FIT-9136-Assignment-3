# Task 2 Implementation Summary

## Overview

Successfully implemented Task 2 - Borrowing and Returning Books functionality for the library management system.

## Implementation Date

October 15, 2025

## Key Features Implemented

### 1. Fine Calculation System

- **Fine Rate**: $0.50 per day for overdue physical books
- **Fine Logic**:
  - Only physical books incur fines
  - Online books are exempt (access automatically revoked)
  - Fines calculated from day after due date
  - Active loans: fines calculated up to TODAY (15/09/2025)
  - Returned loans: fines calculated up to return date

### 2. Updated Menu System

- Added option 4: "Borrow and Return" for all users
- Added option 5: "Library Report" for Library staff only
- Updated option 2: "View account policies" to display fines

### 3. View Account Policies Enhancement

Now displays:

- User role and name
- Maximum loan days and items
- Current loan counts (total, physical, online)
- **NEW**: Total outstanding fines

### 4. Borrow and Return Console

Interactive command interface with three commands:

- `borrow <query>`: Borrow a book by title or ID
- `return <book_id>`: Return a borrowed book
- `quit`: Exit console and return to main menu

### 5. Book Search Functionality

- Search by exact book title (case-insensitive)
- Search by book ID (case-insensitive)
- Displays all matching books sorted by book ID
- Shows book details: ID, type, title, author, year, availability

### 6. Borrowing Validation (Priority Order)

1. **User Eligibility**:
   - Check if quota is available
   - Check for outstanding fines (blocks borrowing)
2. **Book Availability**:
   - Verify book exists
   - Check available copies (physical books only)

### 7. Borrow Process

- Multiple books with same title: display list and confirm ID
- Invalid ID confirmation: re-prompt until valid or quit
- Calculate due date based on user role:
  - Student: 10 days
  - Staff: 14 days
  - Others: 7 days
- Online books: unlimited copies (shown as 0/0)
- Success message includes title, author, year, and due date

### 8. Return Process

- Validates loan record exists
- For multiple copies of same book: returns earliest due date first
- Sets return date to TODAY (15/09/2025)
- Calculates and displays fines if overdue
- Online books: no fine (just confirmation message)

## Files Created

### Main Implementation

- `task2.py` - Complete implementation with all features

### Test Cases

- `test_task2_example1.py` - Tests Chris Manner with fines
- `test_task2_example2.py` - Tests Mary Alan staff borrowing
- `test_task2_example3.py` - Tests Noah with quota limits
- `test_task2_example4.py` - Tests Library Report with invalid inputs

## Key Functions Added/Modified

### New Functions in task2.py

1. `calculate_fine(due_date_str, return_date_str, book_type)` - Calculate overdue fines
2. `get_user_fines(loans, books, user_id)` - Get total fines for a user
3. `get_available_copies(book_id, books, loans)` - Get available copies for a book
4. `search_books(query, books)` - Search books by title or ID
5. `borrow_book(current_user, book_id, books, loans)` - Process book borrowing
6. `return_book(current_user, book_id, books, loans)` - Process book return
7. `borrow_and_return_console(current_user, books, loans)` - Interactive console
8. `format_date(date_obj)` - Format datetime to dd/mm/yyyy string

### Modified Functions

1. `view_account_policies()` - Added fines display
2. `display_menu()` - Added Borrow and Return option
3. `main()` - Added option 4 and 5 handling

## Testing Results

### Example 1: Chris Manner (Student) with Fines ✓

- Shows $1.00 fine (P0006 overdue by 2 days)
- Blocks borrowing due to unpaid fines
- Returns P0006 with fine calculation
- Returns E0001 without fine (online book)
- Correctly shows 0 loans after returns

### Example 2: Mary Alan (Staff) and Justin Bierber ✓

- Staff shows 14-day loan period
- Invalid book ID confirmation re-prompts
- Successful borrowing updates availability
- Second user cannot borrow unavailable book

### Example 3: Noah (Others) Quota Limits ✓

- Others have 7-day loan period and 2-item quota
- Successfully borrows 2 books
- Blocks third borrowing due to quota reached
- Correctly shows "No copies available" message

### Example 4: Library Report with Invalid Inputs ✓

- Library Report displays correct statistics
- Invalid menu choices re-prompt without error
- Menu redisplays after each action

## Technical Details

### Date Handling

- TODAY constant: "15/09/2025" (defined in user.py)
- Date format: dd/mm/yyyy
- Due date calculation uses datetime.timedelta

### Search Algorithm

- Exact title matching (case-insensitive)
- Book ID matching (case-insensitive)
- Results sorted by book ID

### Quota Counting

- Online books don't count toward quota
- Physical books count toward quota
- Quota checked before allowing borrowing

### Fine Calculation

- Formula: days_overdue × $0.50
- Only positive overdue days count
- Rounded to 2 decimal places

## Edge Cases Handled

1. **Multiple books with same title**: Display all, confirm ID
2. **Invalid book ID confirmation**: Re-prompt until valid or quit
3. **No matching books**: Display "No books match" message
4. **No loan record**: Display "No loan record for" message
5. **Invalid commands**: Silently ignore and re-prompt
6. **Online books**: 0/0 availability, no fines, unlimited access
7. **Multiple loans of same book**: Return earliest due date first

## Validation Priority

As per requirements, validation follows this order:

1. User has available quota (excluding online books)
2. User has no outstanding fines
3. Book exists in catalog
4. Book has available copies (for physical books)

## Code Quality

- ✓ No linter errors
- ✓ Follows existing code style
- ✓ Comprehensive docstrings
- ✓ Type hints where applicable
- ✓ Proper error handling
- ✓ Clean separation of concerns

## Compliance with Requirements

- ✓ Uses only allowed imports (csv, datetime, typing)
- ✓ Maintains function signature for main()
- ✓ Uses TODAY constant from user.py
- ✓ Follows exact output format from examples
- ✓ Implements all required features

## Output Examples Match

All four examples produce output that matches the expected format:

- Menu display with correct options
- Fine display in policies
- Borrowing and returning messages
- Error messages and validation
- Library Report statistics

## Conclusion

Task 2 has been successfully implemented with all required features:

- ✓ Fine calculation system
- ✓ Borrowing functionality with validation
- ✓ Returning functionality with fine display
- ✓ Interactive borrow/return console
- ✓ Updated menu system
- ✓ All examples tested and working

The implementation is production-ready and handles all specified edge cases correctly.
