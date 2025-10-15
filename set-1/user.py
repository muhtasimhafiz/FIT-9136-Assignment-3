from abc import ABC, abstractmethod
import csv
import datetime
import re

TODAY = "15/09/2025"


class User(ABC):
    """Abstract base class for library users"""
    
    def __init__(self, user_id, password, name, role, department=""):
        self.user_id = user_id
        self.password = password
        self.name = name
        self.role = role
        self.department = department
    
    @abstractmethod
    def get_max_days(self):
        """Return maximum loan days for this user type"""
        pass
    
    @abstractmethod
    def get_max_items(self):
        """Return maximum items this user can borrow"""
        pass
    
    def get_role_display(self):
        """Return formatted role name"""
        return self.role.capitalize()


class Student(User):
    """Student user class"""
    
    def __init__(self, user_id, password, name, department=""):
        super().__init__(user_id, password, name, "student", department)
    
    def get_max_days(self):
        return 10
    
    def get_max_items(self):
        return 4
    
    def get_role_display(self):
        return "Student"


class Staff(User):
    """Staff user class"""
    
    def __init__(self, user_id, password, name, department=""):
        super().__init__(user_id, password, name, "staff", department)
    
    def get_max_days(self):
        return 14
    
    def get_max_items(self):
        return 6
    
    def get_role_display(self):
        return "Staff"
    
    def is_library_staff(self):
        """Check if this staff member works in the Library department"""
        return self.department == "Library"


class Others(User):
    """Other user type class"""
    
    def __init__(self, user_id, password, name, department=""):
        super().__init__(user_id, password, name, "other", department)
    
    def get_max_days(self):
        return 7
    
    def get_max_items(self):
        return 2
    
    def get_role_display(self):
        return "Others"


def load_users(filename):
    """Load users from CSV file and return a dictionary of User objects"""
    users = {}
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            user_id = row['user_id']
            password = row['password']
            name = row['name']
            role = row['role']
            department = row.get('department', '')
            
            # Create appropriate user object based on user_id prefix
            if user_id.startswith('s'):
                user = Student(user_id, password, name, department)
            elif user_id.startswith('e'):
                user = Staff(user_id, password, name, department)
            elif user_id.startswith('o'):
                user = Others(user_id, password, name, department)
            else:
                continue  # Skip invalid user IDs
            
            users[user_id] = user
    
    return users
