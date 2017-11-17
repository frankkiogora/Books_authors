from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class BlogManager(models.Manager):
#     def basic_validatot(self,postData):
#         errors ={}
#         if len(postData['name']) < 5:
#             errors['name'] = 'Blog name should be more than 5 characters'
#         if len(postData['desc']) < 10:
#             errors['desc'] ='Blog should be more than 10 characters'
#         return errors

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField()
    books = models.ManyToManyField(Book, related_name="authors")

# # Create 5 books with the following names: C sharp, Java, Python, PHP, Ruby

# Book.objects.create(name ='C sharp', desc = 'This is a c sharp book')
# Book.objects.create(name ='Java', desc = 'This is a Java book book')
# Book.objects.create(name ='Python', desc = 'This is a Python book')
# Book.objects.create(name ='PHP', desc = 'This is a PHP book')
# Book.objects.create(name ='Ruby', desc = 'This is a Ruby book')

# # Create 5 different authors: Mike, Speros, John, Jadee, Jay

# Author.objects.create(first_name='Mike')
# Author.objects.create(first_name='Speros')
# Author.objects.create(first_name='John')
# Author.objects.create(first_name='Jay')

# # Change the name of the 5th book to C#

# b=Book.objects.get(id =5)
# b.name = 'C#'
# b.save()

# # Change the first_name of the 4th author to Ketul

# c = Author.objects.get(id=5)
# c.first_name = "ketul"
# c.save()



# author1 = Author.objects.get(id=1)
# author2 = Author.objects.get(id=2)
# author3 = Author.objects.get(id=3)
# author4 = Author.objects.get(id=4)
# author5 = Author.objects.get(id=5)

# book1 = Book.objects.get(id=1)
# book2 = Book.objects.get(id=2)
# book3 = Book.objects.get(id=3)
# book4 = Book.objects.get(id=4)
# book5 = Book.objects.get(id=5)
# # Assign the first author to the first 2 books

# book1.authors.add(author1)
# book2.authors.add(author1)

# # Assign the second author to the first 3 books

# book1 = Book.objects.get(id=1)
# book2 = Book.objects.get(id=2)
# book3 = Book.objects.get(id=3)

# book1.authors.add(author2)
# book2.authors.add(author2)
# book3.authors.add(author2)

# # Assign the third author to the first 4 books

# author3 = Author.objects.get(id=3)
# book1 = Book.objects.get(id=1)
# book2 = Book.objects.get(id=2)
# book3 = Book.objects.get(id=3)
# book4 = Book.objects.get(id=4)
# book1.authors.add(author3)
# book2.authors.add(author3)
# book3.authors.add(author3)
# book4.authors.add(author3)

# # Assign the fourth author to the first 5 books (or in other words, all the books)
# book1.authors.add(author2)
# author2.books.add(book1)

# # For the 3rd book, retrieve all the authors
# book3.authors.all()

# # For the 3rd book, remove the first author
# book3.authors.remove(author1)


# # For the 2nd book, add the 5th author as one of the authors
# book2.authors.add(author5)

# # Find all the books that the 3rd author is part of
# author3.books.all()

# # Find all the books that the 2nd author is part of
# author2.books.all()







