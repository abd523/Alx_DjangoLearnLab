# Create Operation

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()
```

**Expected Output:**
# The book is created successfully. No direct output is shown in the shell, but the object is saved to the database.
