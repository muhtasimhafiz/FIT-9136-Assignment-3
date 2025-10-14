import csv
import datetime
import re

class Book:
    """Class representing a book in the library"""
    
    def __init__(self, book_id, book_type, copies, title, author, year, keywords):
        self.book_id = book_id
        self.book_type = book_type  # 'physical' or 'online'
        self.total_copies = int(copies)
        self.title = title
        self.author = author
        self.year = year
        self.keywords = keywords
    
    def is_physical(self):
        """Check if this is a physical book"""
        return self.book_type == 'physical'
    
    def is_online(self):
        """Check if this is an online book"""
        return self.book_type == 'online'


def load_books(filename):
    """Load books from CSV file and return a dictionary of Book objects"""
    books = {}
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            book_id = row['book_id']
            book_type = row['type']
            copies = row['copies']
            title = row['title']
            author = row['author']
            year = row['year']
            keywords = row['keywords']
            
            book = Book(book_id, book_type, copies, title, author, year, keywords)
            books[book_id] = book
    
    return books
