# Task 3 Tests

This directory contains tests for Task 3 functionality.

## Test Files

### test_task3_example1.py

Tests the renew loan functionality including:

- Renewal denied when user has unpaid fines
- Renewal denied when book is overdue
- Successful renewal extending due date by 5 days
- Return books with fine calculation

### test_task3_example2.py

Tests the search by keywords functionality including:

- Keyword-based search with multiple keywords
- Proper sorting by matched keywords, year, and book ID
- Borrowing online books

### test_task3_example3.py

Tests the Manage Library console including:

- Library report display
- Adding physical books with automatic keyword detection
- Automatic book ID generation

## Running Tests

Run individual test files:

```bash
python tests/task3_tests/test_task3_example1.py
python tests/task3_tests/test_task3_example2.py
python tests/task3_tests/test_task3_example3.py
```

Or run all tests:

```bash
python -m pytest tests/task3_tests/ -v
```

## Features Tested

### 1. Updated Main Menu

- Option 5: Search by Keywords (all users)
- Option 6: Manage Library (library staff only)

### 2. Renew Loan

- Command: `renew <book ID>`
- Extends due date by 5 days
- Validation: unpaid fines, already overdue, already renewed once
- Renews earliest due date first if multiple copies

### 3. Search by Keywords

- Case-insensitive keyword search
- Sorting by: matched keywords count, year (newest first), book ID (ascending)
- Returns books matching at least one keyword

### 4. Manage Library

- `report`: Display library statistics
- `add physical`: Add new physical book with keyword detection
- `add online`: Add new online book with keyword detection
- Automatic book ID generation (P#### or E####)
