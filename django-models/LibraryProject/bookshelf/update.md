
3️⃣ **`update.md`**
```markdown
# Update Operation

**Command used:**
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title
**expected output**
'Nineteen Eighty-Four'
