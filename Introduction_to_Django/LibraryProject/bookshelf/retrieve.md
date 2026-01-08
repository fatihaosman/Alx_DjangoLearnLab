
2️⃣ **`retrieve.md`**
```markdown
# Retrieve Operation

**Command used:**
```python
book = Book.objects.get(title="1984")
book.title
book.author
book.publication_year

**expected output**
'1984' 
'George Orwell'
1949
