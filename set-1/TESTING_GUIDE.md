# Testing Guide for Library Management System - Task 1

## Automated Tests

Run the automated test suite:
```bash
python test_task1.py
```

This validates:
- ✅ User loading from CSV
- ✅ Book loading from CSV
- ✅ Loan loading from CSV
- ✅ Active loan filtering
- ✅ User loan counts (physical/online)
- ✅ Available books calculation
- ✅ User policies display
- ✅ Date parsing and sorting
- ✅ Library report statistics
- ✅ Role display formatting
- ✅ Library staff detection

## Manual Interactive Tests

Run the program:
```bash
python task1.py
```

### Test 1: Failed Login (3 attempts)
**Steps:**
1. Login: `s312` Password: `chr1267` → Invalid
2. Login: `s31267` Password: `chr12` → Invalid
3. Login: `s31267` Password: `chr126` → Out of attempts
4. Login: `quit` → Exit

**Expected:**
- Shows "Invalid credentials. X attempt(s) remaining." after each failed attempt
- Shows "Sorry you're out of attempts..." after 3rd failure
- Returns to welcome screen
- Exits with "Goodbye!" when typing quit

---

### Test 2: Student Login - View Policies and Loans
**Credentials:** `s31267` / `chr1267` (Chris Manner)

**Menu Options:**
- Should show options 0-3 only (no Library Report)

**Test Option 2 (View account policies):**
```
Student Chris Manner. Policies: maximum of 10 days, 4 items. Current loans: 2 (1 physical / 1 online).
```

**Test Option 3 (View my loans):**
```
You are currently have 2 loan(s).
1. P0006 'Hands-On ML' by Aurelien Geron (2019). Due date: 13/09/2025.
2. E0001 'Python Crash Course' by Eric Matthes (2015). Due date: 15/09/2025.
```
- Verify loans are sorted by due date

**Test Option 0:** Exit with "Goodbye!"

---

### Test 3: Library Staff - Full Access
**Credentials:** `e118102` / `pa55word` (Mary Alan)

**Menu Options:**
- Should show options 0-4 (includes Library Report)

**Test Option 4 (Library Report):**
```
Library report
- 9 users, including 4 student(s), 3 staff, and 2 others.
- 14 books, including 10 physical book(s) (7 currently available) and 4 online book(s).
```

**Test Invalid Choice:**
- Enter `5` → Should re-prompt without error message
- Enter `3` → Should show Mary's 1 loan

**Test Option 3 (View my loans):**
```
You are currently have 1 loan(s).
1. P0004 'The Hitchhiker's Guide to the Galaxy' by Douglas Adams (1985). Due date: 17/09/2025.
```

---

### Test 4: Others User - No Loans
**Credentials:** `o56789` / `hackme` (Chloe)

**Test Option 2 (View account policies):**
```
Others Chloe. Policies: maximum of 7 days, 2 items. Current loans: 0 (0 physical / 0 online).
```

**Test Option 3 (View my loans):**
```
You are currently have 0 loan(s).
```

---

### Test 5: Non-Library Staff
**Credentials:** `e45261` / `readmore` (Lan Nguyen)

**Menu Options:**
- Should show options 0-3 only (NO Library Report)
- Even though Lan is staff, she's from Business department

**Test Option 2 (View account policies):**
```
Staff Lan Nguyen. Policies: maximum of 14 days, 6 items. Current loans: 1 (1 physical / 0 online).
```

**Test Option 3 (View my loans):**
```
You are currently have 1 loan(s).
1. P0019 'Principles of Marketing' by Philip Kotler (2016). Due date: 21/09/2025.
```

---

### Test 6: Logout and Re-login
**Steps:**
1. Login as: `s31267` / `chr1267`
2. Choose Option 1 (Log out)
3. Verify return to "Welcome to Library" screen
4. Login as: `e118102` / `pa55word`
5. Verify different menu (with option 4)
6. Choose Option 0 (Quit)

---

## Additional Test Cases

### Test 7: Student with Multiple Loans
**Credentials:** `s24567` / `qwerty88` (Mia)

**Expected:**
- 2 active loans (both physical)
- Loans should be sorted by due date:
  1. P0009 due 09/09/2025
  2. P0008 due 12/09/2025

---

### Test 8: Invalid Username
**Steps:**
1. Login: `invalid_user` Password: `anything`
2. Should show "Invalid credentials"

---

### Test 9: Case Sensitivity
**Steps:**
1. Login: `QUIT` (uppercase)
2. Should exit (case insensitive)

---

## Validation Checklist

### Data Loading
- [x] All 9 users loaded correctly
- [x] All 14 books loaded correctly
- [x] All 8 loans loaded correctly
- [x] User types (Student/Staff/Others) correctly identified
- [x] Book types (Physical/Online) correctly identified

### User Policies
- [x] Student: 10 days, 4 items
- [x] Staff: 14 days, 6 items
- [x] Others: 7 days, 2 items

### Menu Display
- [x] Non-library users: options 0-3
- [x] Library staff: options 0-4
- [x] Invalid choices re-prompt without error

### Login System
- [x] Valid credentials accepted
- [x] Invalid credentials rejected
- [x] 3 attempts limit enforced
- [x] "quit" exits program
- [x] Logout returns to welcome screen

### Loan Display
- [x] Only active loans shown (no returned loans)
- [x] Loans sorted by due date
- [x] Correct format: "ID 'Title' by Author (Year). Due date: DD/MM/YYYY."
- [x] Correct count display

### Library Report
- [x] User counts correct by role
- [x] Book counts correct by type
- [x] Available books calculated correctly
- [x] Only accessible to Library department staff

### Output Formatting
- [x] Welcome message displays correctly
- [x] Login message shows name and role
- [x] Menu borders (==================================)
- [x] All output matches examples exactly

---

## Test Results Summary

✅ **Automated Tests:** All 10 test suites passed
✅ **Data Loading:** All CSV files parsed correctly
✅ **User Classes:** Student, Staff, Others working correctly
✅ **Book Classes:** Physical and online books working
✅ **Loan System:** Active loans filtered and displayed correctly
✅ **Authentication:** Login with 3-attempt limit working
✅ **Authorization:** Library staff menu access control working
✅ **Output Format:** All outputs match specification

**Status: Implementation Complete and Validated**

