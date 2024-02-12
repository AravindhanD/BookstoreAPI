from django.db import models
"""Author Model
Fields:
id (integer, read-only): The unique identifier for the author.
name (string, required): The name of the author.
email (string, required): The email address of the author.
bio (string): A short biography of the author.
{
  "title": "Example Book",
  "author": 1,
  "published_date": "2022-01-01",
  "price": 10.99
}
"""
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return self.name

"""
Book Model
Fields:
id (integer, read-only): The unique identifier for the book.
title (string, required): The title of the book.
author (integer, required): The ID of the author of the book.
published_date (date, required): The publication date of the book.
price (decimal, required): The price of the book.

{
  "id": 1,
  "title": "Example Book",
  "author": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "bio": "John Doe is a prolific author with several best-selling novels."
  },
  "published_date": "2022-01-01",
  "price": "10.99"
}
"""

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
