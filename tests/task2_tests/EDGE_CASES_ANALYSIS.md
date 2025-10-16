# Task 2 - Edge Cases Analysis

## Overview

This document identifies potential edge cases in the Task 2 implementation and provides test scenarios.

---

## Category 1: Input Validation

### 1.1 Empty Commands

**Scenario**: User presses Enter without typing anything

```
>
>
```

**Expected**: Should silently re-prompt
**Status**: ✅ Handled (empty string split returns empty list)

### 1.2 Commands with Extra Spaces

**Scenario**: User types command with multiple spaces

```
> borrow    Python Crash Course
> return     P0003
```

**Expected**: Should work correctly (maxsplit=1 handles this)
**Status**: ✅ Handled

### 1.3 Case Variations

**Scenario**: User types commands in different cases

```
> BORROW The Hobbit
> ReTuRn P0003
> QUIT
```

**Expected**: Should work (commands converted to lowercase)
**Status**: ✅ Handled

### 1.4 Commands Without Arguments

**Scenario**: User types command without required argument

```
> borrow
> return
```

**Expected**: Should silently re-prompt
**Status**: ✅ Handled (len(parts) < 2 check)

### 1.5 Invalid Commands

**Scenario**: User types unrecognized commands

```
> help
> exit
> list
> show books
```

**Expected**: Should silently re-prompt
**Status**: ✅ Handled (no matching command branch)

---

## Category 2: Book Search Edge Cases

### 2.1 Book Title with Special Characters

**Scenario**: Search for book with special characters in title

```
> borrow The Hitchhiker's Guide to the Galaxy
```

**Expected**: Should find the book
**Status**: ⚠️ POTENTIAL ISSUE - Apostrophe in title

### 2.2 Book Title Case Sensitivity

**Scenario**: Search with wrong case

```
> borrow the hobbit
> borrow THE HOBBIT
> borrow ThE hObBiT
```

**Expected**: Should all find P0008
**Status**: ✅ Handled (case-insensitive comparison)

### 2.3 Partial Title Match

**Scenario**: Search with partial title

```
> borrow Hobbit
> borrow Python
```

**Expected**: Should NOT find books (exact match only)
**Status**: ✅ Correct behavior

### 2.4 Non-Existent Book

**Scenario**: Search for book that doesn't exist

```
> borrow Harry Potter
> borrow XYZ123
```

**Expected**: "No books match" message
**Status**: ✅ Handled

### 2.5 Book ID with Wrong Case

**Scenario**: Search by book ID with different case

```
> borrow p0008
> borrow E0001
```

**Expected**: Should find the book
**Status**: ✅ Handled (case-insensitive)

---

## Category 3: Borrowing Edge Cases

### 3.1 Borrow When Exactly At Quota

**Scenario**: User has borrowed max items minus 1, tries to borrow 1 more

```
Student with 3/4 items -> borrow 1 more -> should succeed
Student with 4/4 items -> borrow 1 more -> should fail
```

**Expected**: Allow at quota, deny over quota
**Status**: ⚠️ NEEDS TESTING

### 3.2 Borrow Same Book Multiple Times

**Scenario**: User tries to borrow a book they already have

```
User borrows P0003
User tries to borrow P0003 again
```

**Expected**: Should succeed if copies available (no restriction mentioned)
**Status**: ⚠️ NOT RESTRICTED - May be intentional or oversight

### 3.3 Online Book Quota

**Scenario**: User at quota tries to borrow online book

```
Others user with 2/2 physical books -> borrow E0001
```

**Expected**: Should succeed (online doesn't count toward quota)
**Status**: ⚠️ NEEDS VERIFICATION - Code shows quota check before book type check

### 3.4 Borrow with Exactly $0.00 Fines

**Scenario**: User has no fines

```
fines = 0.0 -> should allow borrowing
```

**Expected**: Should succeed
**Status**: ✅ Handled (fines > 0 check)

### 3.5 Last Available Copy

**Scenario**: Two users try to borrow the last copy simultaneously

```
P0008 has 1/2 available
User A borrows P0008
User B tries to borrow P0008
```

**Expected**: User B should see "No copies available"
**Status**: ✅ Should work (recalculates each time)

---

## Category 4: Returning Edge Cases

### 4.1 Return Same Book Twice

**Scenario**: User returns a book, then tries to return it again

```
> return P0003
> return P0003
```

**Expected**: Second attempt should show "No loan record"
**Status**: ✅ Handled (return_date set, not in active loans)

### 4.2 Return Book Borrowed by Someone Else

**Scenario**: User tries to return a book they didn't borrow

```
User A borrows P0003
User B tries: return P0003
```

**Expected**: "No loan record for P0003"
**Status**: ✅ Handled (searches user's active loans only)

### 4.3 Return Book Due Today

**Scenario**: Book due 15/09/2025, returned 15/09/2025

```
due_date = 15/09/2025
return_date = 15/09/2025
days_overdue = 0
```

**Expected**: No fine (fine only after due date)
**Status**: ✅ Handled (days_overdue > 0 check)

### 4.4 Return Online Book That's Overdue

**Scenario**: Online book overdue when returned

```
E0001 due 10/09/2025, returned 15/09/2025
```

**Expected**: No fine (online books exempt)
**Status**: ✅ Handled (book_type check)

### 4.5 Return Non-Existent Book ID

**Scenario**: User tries to return invalid book ID

```
> return XYZ999
```

**Expected**: "No loan record for XYZ999"
**Status**: ✅ Handled

### 4.6 Multiple Copies with Same Due Date

**Scenario**: User borrows P0003 twice on same day

```
Loan 1: P0003 due 25/09/2025
Loan 2: P0003 due 25/09/2025
> return P0003
```

**Expected**: Returns one of them (deterministic order)
**Status**: ⚠️ EDGE CASE - Both have same due date, sort is stable

---

## Category 5: Date Handling Edge Cases

### 5.1 Books Overdue by Many Days

**Scenario**: Book overdue by 100 days

```
due_date = 07/06/2025
return_date = 15/09/2025
days_overdue = 100
fine = $50.00
```

**Expected**: Should calculate correctly
**Status**: ✅ Should work (no upper limit in code)

### 5.2 Book Returned Early

**Scenario**: Book returned before due date

```
due_date = 20/09/2025
return_date = 15/09/2025
days_overdue = -5
```

**Expected**: No fine (fine only for positive overdue)
**Status**: ✅ Handled (days_overdue > 0 check)

### 5.3 Book Due in the Future

**Scenario**: Book borrowed today

```
borrow_date = 15/09/2025
due_date = 25/09/2025
```

**Expected**: No current fine
**Status**: ✅ Correct

---

## Category 6: Confirmation Edge Cases

### 6.1 Quit During Confirmation

**Scenario**: User types 'quit' when asked to confirm book ID

```
> borrow The Hobbit
Confirm the Book ID you'd like to borrow: quit
```

**Expected**: Should exit to previous prompt
**Status**: ✅ Handled (quit check in confirmation loop)

### 6.2 Invalid ID, Then Valid ID

**Scenario**: User enters wrong ID, then correct one

```
> borrow The Hobbit
Confirm the Book ID you'd like to borrow: P0007
Confirm the Book ID you'd like to borrow: P0008
```

**Expected**: Should re-prompt until valid
**Status**: ✅ Handled (loop continues on invalid)

### 6.3 Book ID from Different Search

**Scenario**: User confirms with ID not in search results

```
> borrow The Hobbit
Found 1 book(s).
- P0008 ...
Confirm the Book ID you'd like to borrow: P0003
```

**Expected**: Should re-prompt (P0003 not in matching list)
**Status**: ✅ Handled (confirmed_id in matching_books check)

### 6.4 Empty Confirmation

**Scenario**: User presses Enter without typing

```
Confirm the Book ID you'd like to borrow:
```

**Expected**: Should re-prompt
**Status**: ✅ Handled (won't match any book ID)

---

## Category 7: Menu Navigation Edge Cases

### 7.1 Invalid Menu Choice

**Scenario**: User enters invalid option

```
Enter your choice: 99
Enter your choice: abc
Enter your choice: -1
```

**Expected**: Should re-prompt without showing menu
**Status**: ✅ Handled (no matching elif, loops)

### 7.2 Library Report for Non-Staff

**Scenario**: Student tries option 5

```
Student user
Enter your choice: 5
```

**Expected**: Should re-prompt (option doesn't exist for them)
**Status**: ✅ Handled (menu doesn't show option 5)

### 7.3 Accessing Option 4 Multiple Times

**Scenario**: User enters and exits borrow/return console multiple times

```
Enter your choice: 4
> quit
Enter your choice: 4
> quit
```

**Expected**: Should work each time
**Status**: ✅ Should work (console is re-callable)

---

## Category 8: Data Integrity Edge Cases

### 8.1 Empty Loans List

**Scenario**: New user with no loans

```
User has never borrowed anything
View account policies -> 0 loans, $0.00 fines
```

**Expected**: Should display correctly
**Status**: ✅ Handled

### 8.2 All Copies Borrowed

**Scenario**: All copies of a physical book are out

```
P0002 has 5 copies, all borrowed
Available: 0/5
```

**Expected**: Should show 0 available, "No copies available"
**Status**: ✅ Handled

### 8.3 Online Book "Copies"

**Scenario**: Online book shows in availability

```
E0001 has 0 total copies
Available: 0/0 (unlimited)
```

**Expected**: Should always show 0/0
**Status**: ✅ Handled (explicit check for online books)

---

## Category 9: Discovered Critical Edge Cases

### 9.1 🚨 CRITICAL: Online Book Quota Check

**Issue**: Code checks quota BEFORE determining if book is online

```python
# Current code:
if total_loans >= max_items:
    print("quota reached")
    return False

# Then later:
if book_obj.is_physical():
    # check availability
```

**Problem**: If user has 2/2 quota (Others), they might be blocked from borrowing online books

**Test Scenario**:

```
Noah (2 item quota) borrows P0003 and P0008 (2/2)
Noah tries to borrow E0001 (online)
```

**Expected**: Should succeed (online doesn't count)
**Actual**: Might fail with "quota reached"

**Status**: ⚠️ CRITICAL BUG - Needs fixing!

### 9.2 Fine Precision

**Issue**: Float arithmetic may cause precision issues

**Scenario**:

```
7 days overdue = 7 * 0.50 = 3.50
But: 0.1 + 0.1 + 0.1 != 0.3 in floating point
```

**Status**: ⚠️ Minor - Use Decimal for currency or ensure proper rounding

### 9.3 Multiple Loans, Same Book, Same Due Date

**Issue**: Sort stability when returning

**Scenario**:

```
User borrows P0003 on 15/09 -> due 25/09
User borrows P0003 on 15/09 -> due 25/09
> return P0003
```

**Expected**: Return deterministically (maybe first borrowed?)
**Actual**: Returns arbitrary one (sort is stable but both have same date)

**Status**: ⚠️ Minor edge case - Spec says "earliest due date" but doesn't specify tie-breaker

---

## Category 10: Command Parsing Edge Cases

### 10.1 Leading/Trailing Spaces

**Scenario**: User adds extra spaces

```
>    borrow The Hobbit
>   return P0003
```

**Expected**: Should work (strip() called)
**Status**: ✅ Handled (.strip() in command_line)

### 10.2 Tabs Instead of Spaces

**Scenario**: User uses tab character

```
> borrow	The Hobbit
```

**Expected**: Should work (split handles whitespace)
**Status**: ✅ Handled (split() handles all whitespace)

---

## Summary of Issues Found

### Critical Issues

1. **Online Book Quota Bug**: Quota check happens before book type check
   - Severity: HIGH
   - Impact: Online books may be incorrectly blocked when at quota

### Minor Issues

2. **Float Precision**: Using float for currency
   - Severity: LOW
   - Impact: Potential rounding errors with large fines
3. **Same Due Date Tie-Breaker**: No secondary sort for identical due dates
   - Severity: LOW
   - Impact: Non-deterministic return order for edge case

### Working Correctly

- ✅ Input validation (empty, invalid, case)
- ✅ Book search (exact match, case-insensitive)
- ✅ Return validation
- ✅ Fine calculation
- ✅ Menu navigation
- ✅ Confirmation loops

---

## Recommended Fixes

### Fix 1: Online Book Quota Check

Move quota check to only apply to physical books:

```python
def borrow_book(current_user: user.User, book_id: str, books: dict, loans: list):
    # Check if user has unpaid fines
    fines = get_user_fines(loans, books, current_user.user_id)
    if fines > 0:
        print("Borrowing unavailable: unpaid fines. Review your loan details for more info.")
        return False

    # Get book object first
    book_obj = books.get(book_id)
    if not book_obj:
        print(f"Book {book_id} not found.")
        return False

    # Check quota ONLY for physical books
    if book_obj.is_physical():
        total_loans, physical_loans, online_loans = get_user_loans_count(loans, current_user.user_id)
        max_items = current_user.get_max_items()

        if total_loans >= max_items:
            print("Borrowing unavailable: quota reached. Review your loan details for more info.")
            return False

    # ... rest of function
```

### Fix 2: Add Borrow Date to Tie-Breaker

Add borrow_date as secondary sort for returns:

```python
# Sort by due date, then by borrow date
user_active_loans.sort(key=lambda x: (parse_date(x['due_date']), parse_date(x['borrow_date'])))
```

### Fix 3: Document Float Precision

Add comment noting float is acceptable for this use case:

```python
# Using float for currency - acceptable for this application
# as fines are always multiples of $0.50
```
