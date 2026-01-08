
4️⃣ **`delete.md`**
```markdown
# Delete Operation

**Command used:**
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()

**expected output**
(1, {'bookshelf.Book': 1})
<QuerySet []>
