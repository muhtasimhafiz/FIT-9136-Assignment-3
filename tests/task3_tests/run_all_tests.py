"""
Run all Task 3 tests
"""
import sys
import os

# Add set-1 directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../set-1'))

def run_all_tests():
    """Run all Task 3 example tests"""
    print("=" * 60)
    print("Running Task 3 Tests")
    print("=" * 60)
    
    # Import test modules
    from test_task3_example1 import test_example1
    from test_task3_example2 import test_example2
    from test_task3_example3 import test_example3
    
    tests = [
        ("Example 1 - Renew Loan", test_example1),
        ("Example 2 - Search by Keywords", test_example2),
        ("Example 3 - Manage Library", test_example3)
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        print(f"\n{'=' * 60}")
        print(f"Testing: {test_name}")
        print('=' * 60)
        try:
            test_func()
            passed += 1
            print(f"✓ {test_name} PASSED")
        except AssertionError as e:
            failed += 1
            print(f"✗ {test_name} FAILED")
            print(f"  Error: {e}")
        except Exception as e:
            failed += 1
            print(f"✗ {test_name} ERROR")
            print(f"  Error: {e}")
    
    print(f"\n{'=' * 60}")
    print(f"Test Results: {passed} passed, {failed} failed")
    print('=' * 60)
    
    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)

