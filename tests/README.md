# Tests Directory

This directory contains all test files and test documentation for the FIT-9136 Assignment 3.

## Directory Structure

```
tests/
├── task1_tests/          # Tests for Task 1 (Login and Account Info)
│   ├── test_task1.py
│   ├── test_invalid_input.py
│   ├── test_library_report.py
│   ├── test_login_fix.py
│   ├── test_menu_sequence.py
│   ├── test_option3.py
│   ├── test_s31267.py
│   ├── test_cases.md
│   └── TESTING_GUIDE.md
│
├── task2_tests/          # Tests for Task 2 (Borrowing and Returning)
│   ├── test_task2_example1.py
│   ├── test_task2_example2.py
│   ├── test_task2_example3.py
│   ├── test_task2_example4.py
│   ├── test_edge_case_quota_bug.py
│   ├── test_edge_case_online_quota.py
│   ├── TASK2_QUICK_TEST.py
│   ├── FINAL_VERIFICATION.py
│   ├── EDGE_CASES_ANALYSIS.md
│   ├── EDGE_CASES_SUMMARY.md
│   └── EDGE_CASES_FINAL_REPORT.md
│
└── README.md             # This file
```

## Running Tests

### Task 1 Tests

```bash
# From project root
cd tests/task1_tests
python test_task1.py
python test_login_fix.py
python test_library_report.py
```

### Task 2 Tests

```bash
# From project root
cd tests/task2_tests
python TASK2_QUICK_TEST.py           # Quick verification
python FINAL_VERIFICATION.py         # Comprehensive verification
python test_task2_example1.py        # Example 1 test
python test_task2_example2.py        # Example 2 test
python test_task2_example3.py        # Example 3 test
python test_task2_example4.py        # Example 4 test
```

## Test Documentation

- **task1_tests/TESTING_GUIDE.md** - Complete guide for Task 1 testing
- **task2_tests/EDGE_CASES_FINAL_REPORT.md** - Complete edge case analysis for Task 2
- **task2_tests/EDGE_CASES_SUMMARY.md** - Summary of edge cases tested
- **task2_tests/EDGE_CASES_ANALYSIS.md** - Detailed edge case analysis

## Test Coverage

### Task 1

- Login functionality
- Menu navigation
- Account policies display
- Loan viewing
- Library report (staff only)
- Invalid input handling

### Task 2

- Book borrowing with validation
- Book returning with fine calculation
- Quota management (physical vs online)
- Fine calculation ($0.50/day for physical books)
- Search functionality (exact title matching)
- Confirmation dialogs
- Edge cases (45+ test scenarios)

## Important Notes

1. **Tests require the parent directory structure**: Tests assume they can access `../set-1/` for the main code files
2. **Data files**: Tests use `../set-1/data/` for CSV files
3. **Test isolation**: Some tests modify loan data; results may vary on repeated runs
4. **Edge case fix**: Task 2 includes a critical bug fix for online book quota counting

## Quick Start

To verify everything is working:

```bash
# Quick Task 2 verification
cd tests/task2_tests
python FINAL_VERIFICATION.py

# Should output:
# ALL VERIFICATIONS PASSED!
# Task 2 implementation is production-ready!
```

## Test Status

| Task      | Total Tests | Pass    | Fail  | Status          |
| --------- | ----------- | ------- | ----- | --------------- |
| Task 1    | 8           | 8       | 0     | ✅ Complete     |
| Task 2    | 45+         | 45+     | 0     | ✅ Complete     |
| **Total** | **53+**     | **53+** | **0** | ✅ **All Pass** |

---

**Last Updated**: October 16, 2025  
**Assignment**: FIT-9136 Assignment 3  
**Status**: All tests passing ✅
