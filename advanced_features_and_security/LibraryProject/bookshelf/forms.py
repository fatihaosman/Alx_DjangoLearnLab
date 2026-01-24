<!-- bookshelf/templates/bookshelf/form_example.html -->
<form method="post">
    {% csrf_token %}
    <label for="title">Book Title:</label>
    <input type="text" name="title" id="title">
    <button type="submit">Search</button>
</form>
