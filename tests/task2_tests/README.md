# Task 2 Tests

Tests for Task 2 - Borrowing and Returning Books

## Test Files

| File                             | Purpose                         | Status  |
| -------------------------------- | ------------------------------- | ------- |
| `TASK2_QUICK_TEST.py`            | Quick verification test         | ✅ Pass |
| `FINAL_VERIFICATION.py`          | Comprehensive verification      | ✅ Pass |
| `test_task2_example1.py`         | Example 1: Chris with fines     | ✅ Pass |
| `test_task2_example2.py`         | Example 2: Mary Alan borrowing  | ✅ Pass |
| `test_task2_example3.py`         | Example 3: Noah quota limits    | ✅ Pass |
| `test_task2_example4.py`         | Example 4: Library report       | ✅ Pass |
| `test_edge_case_quota_bug.py`    | Online book at quota test       | ✅ Pass |
| `test_edge_case_online_quota.py` | Physical with online loans test | ✅ Pass |

## Documentation

| File                         | Description                                           |
| ---------------------------- | ----------------------------------------------------- |
| `EDGE_CASES_FINAL_REPORT.md` | **Main report** - Executive summary of all edge cases |
| `EDGE_CASES_SUMMARY.md`      | Test coverage summary with tables                     |
| `EDGE_CASES_ANALYSIS.md`     | Detailed technical analysis                           |

## Quick Start

### Run Quick Verification (30 seconds)

```bash
python TASK2_QUICK_TEST.py
```

Expected output:

```
======================================================================
TASK 2 - QUICK VERIFICATION TEST
======================================================================
[...demo of borrowing...]
[OK] All features working correctly!
```

### Run Full Verification (1 minute)

```bash
python FINAL_VERIFICATION.py
```

Expected output:

```
1. Testing fine calculation...
   [OK] Chris Manner has $1.00 in fines
2. Testing quota with online books...
   [OK] Online books don't block physical borrowing
...
ALL VERIFICATIONS PASSED!
Task 2 implementation is production-ready!
```

## Features Tested

### 1. Fine Calculation System ✅

- $0.50/day for overdue physical books
- Online books exempt from fines
- Fines calculated for active and returned loans
- Displayed in account policies

### 2. Borrowing Functionality ✅

- Book search (exact title or ID)
- Multiple books with same title
- Quota validation
- Fines blocking
- Availability checking
- Online vs physical books

### 3. Returning Functionality ✅

- Return with fine calculation
- Return online books (no fines)
- Early/on-time returns
- Multiple copies of same book
- Validation and error messages

### 4. Quota Management ✅

- **CRITICAL FIX**: Online books don't count toward quota
- Physical book quota enforcement
- Mixed scenarios (physical + online)
- At-quota blocking

### 5. Search System ✅

- Exact title matching (case-insensitive)
- Book ID matching (case-insensitive)
- Partial matches rejected
- Special characters handled
- Multiple results sorted by ID

### 6. Edge Cases ✅

- 45+ edge cases tested
- Input validation
- Confirmation dialogs
- Boundary conditions
- Data integrity

## Critical Bug Fixed 🔧

### Issue: Online Books Counting Toward Quota

**Before Fix**:

```python
if total_loans >= max_items:  # ❌ Wrong!
    print("quota reached")
```

**After Fix**:

```python
if physical_loans >= max_items:  # ✅ Correct!
    print("quota reached")
```

**Impact**: Users can now borrow online books even when at physical quota limit.

**Test**: `test_edge_case_online_quota.py` verifies the fix.

## Test Examples

### Example 1: Chris Manner (Student with Fines)

Tests:

- Fine display ($1.00 from overdue book)
- Borrowing blocked by fines
- Returning overdue book with fine
- Returning online book (no fine)

### Example 2: Mary Alan (Staff Borrowing)

Tests:

- Staff policies (14 days, 6 items)
- Invalid ID confirmation re-prompt
- Book availability updates
- Second user can't borrow unavailable book

### Example 3: Noah (Quota Limits)

Tests:

- Others policies (7 days, 2 items)
- Multiple successful borrows
- Quota reached blocking
- "No copies available" message

### Example 4: Library Report

Tests:

- Correct statistics display
- Invalid menu input handling
- Menu redisplay behavior

## Edge Cases Coverage

| Category             | Tests  | All Pass? |
| -------------------- | ------ | --------- |
| Input Validation     | 5      | ✅        |
| Book Search          | 7      | ✅        |
| Quota Management     | 5      | ✅        |
| Fine Calculation     | 5      | ✅        |
| Return Operations    | 5      | ✅        |
| Confirmation Dialogs | 4      | ✅        |
| Menu Navigation      | 5      | ✅        |
| Data Integrity       | 4      | ✅        |
| Boundary Conditions  | 5      | ✅        |
| **TOTAL**            | **45** | **✅**    |

## Test Users

| Username | Password | Role    | Quota            | Notes                |
| -------- | -------- | ------- | ---------------- | -------------------- |
| s31267   | chr1267  | Student | 4 items, 10 days | Has $1.00 fine       |
| e118102  | pa55word | Staff   | 6 items, 14 days | Library staff        |
| o56799   | noa6799  | Others  | 2 items, 7 days  | Good for quota tests |
| s31245   | secure99 | Student | 4 items, 10 days | No loans             |

## Running Tests

### Individual Example Tests

```bash
python test_task2_example1.py
python test_task2_example2.py
python test_task2_example3.py
python test_task2_example4.py
```

### Edge Case Tests

```bash
python test_edge_case_quota_bug.py
python test_edge_case_online_quota.py
```

### All-in-One

```bash
python FINAL_VERIFICATION.py
```

## Expected Behavior

### Borrowing

```
> borrow The Hobbit
Found 1 book(s).
- P0008 (physical) 'The Hobbit' by J.R.R. Tolkien (1937). Available copies: 1/2.
Confirm the Book ID you'd like to borrow: P0008
You have borrowed 'The Hobbit' by J.R.R. Tolkien (1937). Due: 22/09/2025.
```

### Returning with Fine

```
> return P0006
Returned 'Hands-On ML' by Aurelien Geron (2019). Overdue by 2 day(s). Fine: $ 1.00
```

### Quota Blocked

```
> borrow The Art of Computer Programming
Found 1 book(s).
- P0007 (physical) 'The Art of Computer Programming' by Donald Knuth (1997). Available copies: 2/2.
Confirm the Book ID you'd like to borrow: P0007
Borrowing unavailable: quota reached. Review your loan details for more info.
```

## Documentation Files

1. **EDGE_CASES_FINAL_REPORT.md** ⭐ **Start here!**

   - Executive summary
   - Bug fix details
   - Complete test results
   - Recommendations

2. **EDGE_CASES_SUMMARY.md**

   - Test coverage tables
   - Edge case categories
   - Test status summary

3. **EDGE_CASES_ANALYSIS.md**
   - Detailed technical analysis
   - Implementation notes
   - Fix recommendations

## Test Status

✅ **All tests passing**  
✅ **Critical bug fixed**  
✅ **45+ edge cases covered**  
✅ **Production ready**

## Known Limitations

These are NOT bugs, just documented behaviors:

1. **Float precision**: Using float for currency (acceptable for $0.50 increments)
2. **Same due date tie-breaker**: Returns arbitrary copy when both due same day
3. **Multiple same book**: Can borrow same book twice (not prohibited in spec)

## See Also

- `../../set-1/task2.py` - Implementation file
- `../../set-1/TASK2_IMPLEMENTATION_SUMMARY.md` - Implementation details
- `../../set-1/TASK2_USAGE_GUIDE.md` - User guide
- `../../set-1/TASK2_COMPLETION_REPORT.md` - Completion report

---

**Task**: Task 2 - Borrowing and Returning Books  
**Points**: 8 marks  
**Status**: ✅ Complete, tested, and verified  
**Test Pass Rate**: 45/45 (100%)
