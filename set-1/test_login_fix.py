"""
Test script to demonstrate the fixed login behavior
"""
import sys
from io import StringIO
from contextlib import redirect_stdin, redirect_stdout

def test_login_flow():
    """Test the login flow with failed attempts"""
    
    # Simulate user input for failed login attempts
    test_input = """s312
chr1267
s31267
chr12
s31267
chr126
s31267
chr1267
1
0
"""
    
    # Capture output
    output = StringIO()
    
    try:
        with redirect_stdin(StringIO(test_input)):
            with redirect_stdout(output):
                # Import and run the main function
                import task1
                task1.main('data/users.csv', 'data/books.csv', 'data/loans.csv')
    except SystemExit:
        pass  # Expected when program exits
    
    # Get the output
    result = output.getvalue()
    
    print("=== TEST OUTPUT ===")
    print(result)
    print("=== END TEST OUTPUT ===")
    
    # Check if the expected behavior occurred
    lines = result.strip().split('\n')
    
    print("\n=== ANALYSIS ===")
    
    # Look for the sequence
    welcome_count = 0
    failed_attempts = 0
    lockout_message = False
    
    for i, line in enumerate(lines):
        if "Welcome to Library" in line:
            welcome_count += 1
            print(f"Line {i+1}: Found welcome message #{welcome_count}")
        elif "Invalid credentials" in line:
            failed_attempts += 1
            print(f"Line {i+1}: Found failed attempt #{failed_attempts}")
        elif "Sorry you're out of attempts" in line:
            lockout_message = True
            print(f"Line {i+1}: Found lockout message")
        elif "Logged in as" in line:
            print(f"Line {i+1}: Found successful login")
    
    print(f"\nResults:")
    print(f"- Welcome messages: {welcome_count}")
    print(f"- Failed attempts: {failed_attempts}")
    print(f"- Lockout message: {lockout_message}")
    
    # Expected behavior:
    # 1. Welcome to Library
    # 2. 3 failed attempts
    # 3. Lockout message
    # 4. Welcome to Library (again)
    # 5. Successful login
    
    if welcome_count >= 2:
        print("✅ SUCCESS: Program returns to welcome screen after lockout")
    else:
        print("❌ FAILED: Program doesn't return to welcome screen")
    
    if failed_attempts >= 3:
        print("✅ SUCCESS: Shows 3 failed attempts")
    else:
        print("❌ FAILED: Doesn't show 3 failed attempts")
    
    if lockout_message:
        print("✅ SUCCESS: Shows lockout message")
    else:
        print("❌ FAILED: Doesn't show lockout message")

if __name__ == "__main__":
    test_login_flow()
