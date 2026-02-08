from rest_framework import serializers
from datetime import datetime
from .models import Author, Book

"""
BookSerializer:
- Serializes all fields of the Book model
- Includes custom validation to prevent future publication years
"""
class BookSerializer(serializers.ModelSerializer): # “Serializers are like forms but for APIs, they convert complex data types to JSON and validate input data”
  # ModelSerializer → “DRF, please auto-generate fields from the model”

    class Meta:   #“Meta class is where we specify which model to serialize and which fields to include”
      #Meta is a configuration class--Django looks here for instructions
        model = Book  #“This serializer is for the Book model”
        fields = '__all__'  #“Include ALL model fields”

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


"""
AuthorSerializer:
- Serializes the author's name
- Includes a nested representation of related books
- Uses the related_name 'books' from the Book model
"""
class AuthorSerializer(serializers.ModelSerializer): #Name comes from related_name='books'
    books = BookSerializer(many=True, read_only=True) #Use the book serializer inside the author serializer
    
    # many=True
    # One author → many books
    
    #read_only=True
    #➡️ You can:
    # View books ✔️
    # Not create books through author ✔️
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
