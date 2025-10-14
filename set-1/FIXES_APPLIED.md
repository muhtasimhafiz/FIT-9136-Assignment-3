# Fixes Applied to Library Management System

## Issues Fixed

### 1. ✅ Login System - Return to Welcome Screen After Lockout

**Problem**: After 3 failed login attempts, the program wasn't returning to the "Welcome to Library" screen as specified.

**Root Cause**: The login function was using recursive calls instead of returning to the main loop.

**Solution Applied**:

- Modified `login()` function to return `None` after lockout instead of recursive call
- Updated main loop to use `continue` when `current_user is None`
- Added special handling for "quit" command with return value "quit"

**Code Changes**:

```python
# In login() function:
if user_id.lower() == 'quit':
    print("Goodbye!")
    return "quit"  # Special return value to indicate quit
# ...
print("Sorry you're out of attempts. Please contact your librarian for assistance.")
return None  # Return None to go back to main loop

# In main() function:
if current_user == "quit":
    return  # Exit the program
elif current_user is None:
    continue  # Go back to welcome screen for another login attempt
```

**Result**: ✅ Program now correctly returns to "Welcome to Library" after 3 failed attempts.

---

### 2. ✅ TypeError in Option 3 - View My Loans

**Problem**: `TypeError: string indices must be integers, not 'str'` when selecting option 3 to view loans.

**Root Cause**: Empty rows in the CSV file were being processed as loan records, causing the loan data to be strings instead of dictionaries.

**Solution Applied**:

- Enhanced `load_loans()` function to skip empty rows
- Added defensive programming to `get_active_loans()` function
- Used `.get()` method with default values for safer dictionary access

**Code Changes**:

```python
# In load_loans() function:
for row in reader:
    # Skip empty rows - check if any required fields are empty
    if not row.get('user_id') or not row.get('book_id') or not row.get('borrow_date'):
        continue
    loans.append({
        'user_id': row['user_id'],
        'book_id': row['book_id'],
        'borrow_date': row['borrow_date'],
        'due_date': row['due_date'],
        'return_date': row.get('return_date', '')  # Use get with default empty string
    })

# In get_active_loans() function:
for loan in loans:
    # Ensure loan is a dictionary
    if not isinstance(loan, dict):
        continue
    # Check if return_date is empty (active loan)
    if loan.get('return_date', '') == '':
        if user_id is None or loan.get('user_id') == user_id:
            active.append(loan)
```

**Result**: ✅ Option 3 now works without errors for all users.

---

## Testing Results

### ✅ Automated Tests

- All 10 test suites pass
- Data loading works correctly
- Loan processing works without errors
- User authentication works properly

### ✅ Manual Testing

- Option 3 (View my loans) works for all user types:
  - Chris (Student): 2 loans displayed correctly
  - Mary (Library Staff): 1 loan displayed correctly
  - Chloe (Others): 0 loans displayed correctly
  - Lan (Non-Library Staff): 1 loan displayed correctly
  - Mia (Student): 2 loans displayed correctly

### ✅ Login System

- 3-attempt limit works correctly
- Lockout message displays properly
- Returns to welcome screen after lockout
- Allows new login attempts after lockout
- Quit functionality works correctly

## Files Modified

1. **`task1.py`**:
   - Fixed `login()` function return logic
   - Enhanced `load_loans()` function with empty row filtering
   - Added defensive programming to `get_active_loans()` function
   - Updated main loop to handle login states properly

## Verification Commands

Run these commands to verify the fixes:

```bash
# Run automated tests
python test_task1.py

# Test option 3 specifically
python test_option3.py

# Test interactively
python task1.py
```

## Test Credentials

Use these credentials to test different scenarios:

- **Student with loans**: `s31267` / `chr1267` (Chris - 2 loans)
- **Library Staff**: `e118102` / `pa55word` (Mary - 1 loan)
- **Others (no loans)**: `o56789` / `hackme` (Chloe - 0 loans)
- **Non-Library Staff**: `e45261` / `readmore` (Lan - 1 loan)

## Status: ✅ ALL ISSUES RESOLVED

The library management system now works exactly as specified:

- Login system returns to welcome screen after lockout
- Option 3 (View my loans) works without errors
- All menu options function correctly
- All outputs match the specification exactly
