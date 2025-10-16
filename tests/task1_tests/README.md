# Task 1 Tests

Tests for Task 1 - Login and Account Information Display

## Test Files

| File                     | Purpose                          | Status  |
| ------------------------ | -------------------------------- | ------- |
| `test_task1.py`          | Main Task 1 functionality test   | ✅ Pass |
| `test_invalid_input.py`  | Invalid input handling           | ✅ Pass |
| `test_library_report.py` | Library report for staff         | ✅ Pass |
| `test_login_fix.py`      | Login functionality verification | ✅ Pass |
| `test_menu_sequence.py`  | Menu navigation testing          | ✅ Pass |
| `test_option3.py`        | View loans functionality         | ✅ Pass |
| `test_s31267.py`         | Specific user scenario test      | ✅ Pass |

## Documentation

- **TESTING_GUIDE.md** - Comprehensive testing guide for Task 1
- **test_cases.md** - Test case descriptions and expected outputs

## Running Tests

### From this directory:

```bash
# Run individual tests
python test_task1.py
python test_login_fix.py
python test_library_report.py
python test_menu_sequence.py
python test_option3.py
python test_invalid_input.py
python test_s31267.py
```

### From project root:

```bash
cd tests/task1_tests
python test_task1.py
```

## Features Tested

### 1. Login System ✅

- Valid credentials
- Invalid credentials (3 attempts)
- Quit during login
- Multiple login attempts

### 2. Menu Navigation ✅

- Menu display based on user role
- Option selection
- Invalid menu choices
- Quit and logout functionality

### 3. Account Policies Display ✅

- Student policies (10 days, 4 items)
- Staff policies (14 days, 6 items)
- Others policies (7 days, 2 items)
- Current loan counts display

### 4. View Loans ✅

- Active loans display
- Sorted by due date
- No loans scenario
- Book details display

### 5. Library Report (Staff Only) ✅

- User statistics
- Book statistics
- Available books count
- Access control (staff only)

### 6. Error Handling ✅

- Invalid login attempts
- Invalid menu choices
- Non-staff accessing staff features

## Test Users

| Username | Password | Role    | Department |
| -------- | -------- | ------- | ---------- |
| s31267   | chr1267  | Student | IT         |
| e118102  | pa55word | Staff   | Library    |
| o56799   | noa6799  | Others  | -          |

## Expected Outputs

### Example: Student Login

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
4. Library Report
==================================
```

### Example: View Account Policies

```
Enter your choice: 2
Student Chris Manner. Policies: maximum of 10 days, 4 items. Current loans: 2 (1 physical / 1 online).
```

## Test Coverage

- ✅ Login authentication
- ✅ Role-based menu display
- ✅ Account policy calculations
- ✅ Loan display formatting
- ✅ Library report statistics
- ✅ Error handling
- ✅ Input validation

## Known Issues

None - all tests passing ✅

## See Also

- `TESTING_GUIDE.md` - Detailed testing guide
- `../../set-1/task1.py` - Implementation file
- `../../set-1/IMPLEMENTATION_SUMMARY.md` - Implementation details

---

**Task**: Task 1 - Login and Account Info  
**Points**: 5 marks  
**Status**: ✅ Complete and tested
