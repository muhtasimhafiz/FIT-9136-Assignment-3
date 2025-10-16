# Task 3 - Search Made Easy

## Overview

This is the implementation of Task 3 for the library management system. It adds advanced search capabilities, loan renewal, and library management features.

## Quick Start

### Running the Program

```bash
python task3.py
```

### Running Tests

```bash
# Run all tests
python ..\tests\task3_tests\run_all_tests.py

# Run individual tests
python ..\tests\task3_tests\test_task3_example1.py
python ..\tests\task3_tests\test_task3_example2.py
python ..\tests\task3_tests\test_task3_example3.py

# Quick verification
python ..\tests\task3_tests\QUICK_VERIFICATION.py
```

## New Features

### 1. Renew Loan (Option 4 Console)

- Command: `renew <book ID>`
- Extends due date by 5 days
- Can only renew once per book
- Validation for fines, overdue status, and renewal status

### 2. Search by Keywords (Option 5)

- Available to all users
- Multiple keywords supported (comma-separated)
- Smart sorting by matches, year, and ID

### 3. Manage Library (Option 6)

- Library staff only
- Commands: `report`, `add physical`, `add online`, `quit`
- Automatic keyword detection
- Automatic book ID generation

## Test Users

### Students

- s31267 / chr1267 (Chris Manner)
- s24567 / qwerty88 (Mia)

### Library Staff

- e118102 / pa55word (Mary Alan)
- e23456 / gogogo (Mashid Saga)

### Others

- o56799 / noa6799 (Noah)

## Test Results

✅ All Tests Pass (3/3)

- Example 1: Renew Loan ✅
- Example 2: Search by Keywords ✅
- Example 3: Manage Library ✅

No linting errors detected.

## Documentation

See the following files for detailed information:

- `../tests/task3_tests/README.md` - Test overview
- `../tests/task3_tests/IMPLEMENTATION_SUMMARY.md` - Technical details
- `../tests/task3_tests/TASK3_USAGE_GUIDE.md` - User guide
- `../TASK3_COMPLETION_REPORT.md` - Completion report
- `../TASK3_FINAL_SUMMARY.md` - Final summary

## Implementation Details

### Validation Priority (Renew)

1. Check user has no unpaid fines
2. Check loan record exists
3. Check book is not overdue
4. Check not already renewed

### Search Sorting Priority

1. Number of matched keywords (highest first)
2. Publication year (newest first)
3. Book ID (ascending)

### Fine System

- Display fines: All fines (for account view)
- Blocking fines: Only active overdue loans
- Users can borrow after returning overdue books

### Book ID Generation

- Physical books: P#### (e.g., P0020)
- Online books: E#### (e.g., E0005)
- Auto-increments from highest existing ID

## File Structure

```
set-1/
  ├── task3.py              # Main implementation
  ├── book.py               # Book class
  ├── user.py               # User classes
  ├── TASK3_README.md       # This file
  └── data/
      ├── books.csv
      ├── loans.csv
      └── users.csv

tests/task3_tests/
  ├── test_task3_example1.py
  ├── test_task3_example2.py
  ├── test_task3_example3.py
  ├── run_all_tests.py
  ├── QUICK_VERIFICATION.py
  ├── README.md
  ├── IMPLEMENTATION_SUMMARY.md
  └── TASK3_USAGE_GUIDE.md
```

## Status

✅ **COMPLETE AND TESTED**

All features implemented and working correctly.
All tests passing with 100% success rate.
Code is clean, documented, and production-ready.
