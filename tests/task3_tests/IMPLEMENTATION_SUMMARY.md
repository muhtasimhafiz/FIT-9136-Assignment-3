# Task 3 Implementation Summary

## Overview

Task 3 extends the library system with advanced search capabilities, loan renewal, and library management features.

## Features Implemented

### 1. Updated Main Menu

- **All Users**: Added "Search by Keywords" (Option 5)
- **Library Staff**: Added "Manage Library" (Option 6) in addition to Option 5
- Menu dynamically adjusts based on user role

### 2. Renew Loan Functionality

Implemented in `renew_loan()` function with the following features:

#### Command

- `renew <book ID>` in the Borrow and Return console

#### Validation Priority

1. **User Eligibility**: Check if user has unpaid fines from currently overdue books
2. **Loan Validity**: Check if loan record exists for the specified book
3. **Overdue Status**: Check if book is already overdue (due date has passed or equals today)
4. **Renewal Status**: Check if book has already been renewed once

#### Key Rules

- Extends due date by 5 days
- Each book can only be renewed once
- If multiple copies of same book borrowed, renews the one with earliest due date
- Book is considered overdue on or after its due date (using >= comparison)
- Unpaid fines only count active overdue loans, not fines from returned books

#### Error Messages

- `"Renewal denied: You have unpaid fines."` - User has currently overdue books
- `"No loan record for {book_id}."` - No active loan found
- `"Renewal denied: This book is already overdue."` - Book's due date has passed/equals today
- `"Renewal unavailable: Each book can only be renewed once."` - Already renewed

### 3. Search by Keywords

Implemented in `search_by_keywords()` and `search_by_keywords_menu()` functions.

#### Features

- Case-insensitive keyword matching
- Multiple keywords separated by commas
- Matches books containing at least one keyword
- Returns empty result for empty keyword list

#### Sorting Priority

1. Number of matched keywords (highest first)
2. Publication year (newest first)
3. Book ID (ascending order)

#### Implementation Details

- Keywords extracted from `keywords` field in books.csv (colon-separated)
- Normalized to lowercase for matching
- Display format: `{index}. {book_id} '{title}' by {author} ({year}).`

### 4. Manage Library Console (Library Staff Only)

Implemented in `manage_library_console()` function.

#### Commands

- `report`: Display library statistics (existing functionality)
- `add physical`: Add new physical book
- `add online`: Add new online book
- `quit`: Exit console

#### Add Book Features

- Prompts for: Title, Authors, Year
- For physical books: Also prompts for Copies
- For online books: Copies set to 0

#### Automatic Keyword Detection

Implemented in `detect_keywords_from_title()`:

- Matches words in title against existing keywords from books.csv
- Exact word matching (case-insensitive)
- Results sorted alphabetically
- Display format: `keywords1:keywords2:keywords3`

#### Automatic ID Generation

Implemented in `generate_book_id()`:

- Physical books: P#### (e.g., P0020)
- Online books: E#### (e.g., E0005)
- Finds highest existing ID and increments by 1
- Zero-padded to 4 digits

### 5. Fine System Refinement

Created two separate functions for fine calculation:

#### `get_user_fines()`

- For display purposes (account policies)
- Includes ALL fines:
  - Returned books that were overdue
  - Active loans that are currently overdue

#### `get_user_unpaid_fines()`

- For borrowing/renewal restrictions
- Only includes active overdue loans
- Does not count fines from already returned books
- This allows users to continue borrowing after returning overdue books

## Code Structure

### New Functions

- `renew_loan()` - Process loan renewal with validation
- `search_by_keywords()` - Search books by keywords with sorting
- `search_by_keywords_menu()` - Interactive keyword search interface
- `get_all_keywords()` - Extract all unique keywords from books
- `detect_keywords_from_title()` - Detect keywords in new book titles
- `generate_book_id()` - Generate unique book IDs
- `add_book()` - Add new book to library
- `manage_library_console()` - Library management interface
- `get_user_unpaid_fines()` - Calculate fines that block actions

### Modified Functions

- `display_menu()` - Added options 5 and 6
- `borrow_and_return_console()` - Added renew command
- `main()` - Added handlers for options 5 and 6
- `load_loans()` - Added 'renewed' field tracking

### Data Structure Updates

- Loan records now include `'renewed'` field (default: 'False')

## Testing

All three example tests pass successfully:

- ✓ Example 1: Renew loan with various validation scenarios
- ✓ Example 2: Search by keywords and borrow online book
- ✓ Example 3: Manage library - add book and view reports

## Key Design Decisions

### 1. Overdue Date Comparison

- Used `today >= due_date` for renewal checks
- Books are considered overdue on their due date for renewal purposes
- This prevents renewing books on their due date

### 2. Fine Separation

- Separated display fines from restriction fines
- Allows users to continue using the library after returning overdue books
- Matches the expected behavior in the examples

### 3. Keyword Matching

- Exact word matching (not substring)
- Case-insensitive for flexibility
- Only matches against existing keywords in the database

### 4. ID Generation

- Finds maximum ID per type (P or E)
- Increments by 1 for new books
- Zero-padded for consistent formatting

## Files Modified

- `set-1/task3.py` - Main implementation
- `tests/task3_tests/` - Test suite with 3 example tests

## Validation & Error Handling

- All validation follows specified priority order
- Clear error messages for each failure case
- Graceful handling of edge cases (empty keywords, missing books, etc.)
