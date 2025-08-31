# CRUD Operations for Book Model

## Create Operation
**Command:**
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()
```

**Expected Output:**
# The book is created successfully. No direct output is shown in the shell, but the object is saved to the database.

## Retrieve Operation
**Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
```

**Expected Output:**
# 1984 George Orwell 1949

## Update Operation
**Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
```

**Expected Output:**
# Nineteen Eighty-Four

## Delete Operation
**Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())
```

**Expected Output:**
# <QuerySet []>
