#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple example of composisiton.

"""

class Book():
    def __init__(self,t,a):
        self.title=t
        self.author=a
    def __str__(self):
        return "{} is the Title, {} is the Author.".format(self.title, self.author)
        
class EBook(Book):
    
    def __init__(self, t, a, s):
        #remember to pass the self to constructor of the superclass
        Book.__init__(self,t,a)
        self.size=s
        
class normalBook(Book):
    def __init__(self, t, a, p):
        Book.__init__(self, t,a)
        self.pages=p
class Library:
    def __init__(self):
        self.books=[]
    def add_Book(self, book):
        #Composisiton occurs. We use objects of a differente class
        #(Book) and we store them as an attribute of another class
        #(as a list of *objects* in Library)
        self.books.append(book)
        
ebook1=EBook("Odissey", "Homer", 100)
normalBook1=EBook("El Quixote", "Cervantes", 1078)
print(ebook1)
print(normalBook1)
library=Library()
library.add_Book(ebook1)
library.add_Book(normalBook1)

#Accesing the first book in the library. note that we can 
#the instace variables of a book as we are actually accesing one
#by accesing library.book[0] -returns a book.
print(library.books[0].title)
print(library.books[1].pages)
