# Test Cases for Library Management System - Task 1

## Test Case 1: Failed Login Attempts (3 attempts)

**Input:**

- Login: s312
- Password: chr1267
- Login: s31267
- Password: chr12
- Login: s31267
- Password: chr126
- Login: quit

**Expected Output:**

```
Welcome to Library
Login as: s312
Password: chr1267
Invalid credentials. 2 attempt(s) remaining.
Login as: s31267
Password: chr12
Invalid credentials. 1 attempt(s) remaining.
Login as: s31267
Password: chr126
Sorry you're out of attempts. Please contact your librarian for assistance.
Welcome to Library
Login as: quit
Goodbye!
```

## Test Case 2: Student Login - View Policies and Loans

**Input:**

- Login: s31267
- Password: chr1267
- Choice: 2
- Choice: 3
- Choice: 0

**Expected Output:**

```
Welcome to Library
Login as: s31267
Password: chr1267
Logged in as Chris Manner (Student)
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice: 2
Student Chris Manner. Policies: maximum of 10 days, 4 items. Current loans: 2 (1 physical / 1 online).
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice: 3
You are currently have 2 loan(s).
1. P0006 'Hands-On ML' by Aurelien Geron (2019). Due date: 13/09/2025.
2. E0001 'Python Crash Course' by Eric Matthes (2015). Due date: 15/09/2025.
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice: 0
Goodbye!
```

## Test Case 3: Library Staff - View Report

**Input:**

- Login: e118102
- Password: pa55word
- Choice: 4
- Choice: 5 (invalid)
- Choice: 3
- Choice: 0

**Expected Output:**

```
Welcome to Library
Login as: e118102
Password: pa55word
Logged in as Mary Alan (Staff)
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
4. Library Report
==================================
Enter your choice: 4
Library report
- 9 users, including 4 student(s), 3 staff, and 2 others.
- 14 books, including 10 physical book(s) (7 currently available) and 4 online book(s).
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
4. Library Report
==================================
Enter your choice: 5
Enter your choice: 3
You are currently have 1 loan(s).
1. P0004 'The Hitchhiker's Guide to the Galaxy' by Douglas Adams (1985). Due date: 17/09/2025.
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
4. Library Report
==================================
Enter your choice: 0
Goodbye!
```

## Test Case 4: Others User - No Loans

**Input:**

- Login: o56789
- Password: hackme
- Choice: 2
- Choice: 3
- Choice: 0

**Expected Output:**

```
Welcome to Library
Login as: o56789
Password: hackme
Logged in as Chloe (Others)
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice: 2
Others Chloe. Policies: maximum of 7 days, 2 items. Current loans: 0 (0 physical / 0 online).
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice: 3
You are currently have 0 loan(s).
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice: 0
Goodbye!
```

## Test Case 5: Non-Library Staff - View Policies and Loans

**Input:**

- Login: e45261
- Password: readmore
- Choice: 2
- Choice: 3
- Choice: 0

**Expected Output:**

```
Welcome to Library
Login as: e45261
Password: readmore
Logged in as Lan Nguyen (Staff)
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice: 2
Staff Lan Nguyen. Policies: maximum of 14 days, 6 items. Current loans: 1 (1 physical / 0 online).
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice: 3
You are currently have 1 loan(s).
1. P0019 'Principles of Marketing' by Philip Kotler (2016). Due date: 21/09/2025.
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice: 0
Goodbye!
```

## Test Case 6: Logout and Re-login

**Input:**

- Login: s31267
- Password: chr1267
- Choice: 1
- Login: e118102
- Password: pa55word
- Choice: 0

**Expected Output:**

```
Welcome to Library
Login as: s31267
Password: chr1267
Logged in as Chris Manner (Student)
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice: 1
Welcome to Library
Login as: e118102
Password: pa55word
Logged in as Mary Alan (Staff)
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
4. Library Report
==================================
Enter your choice: 0
Goodbye!
```

## Key Points to Test:

1. Login validation (correct/incorrect credentials)
2. 3-attempt limit with proper messaging
3. Different menus for Library staff vs non-Library users
4. Policy display with correct numbers (days, items, current loans)
5. Loan display sorted by due date
6. Library report with correct counts
7. Invalid menu choices
8. Quit at login prompt
9. Logout functionality
10. Available book count calculation
