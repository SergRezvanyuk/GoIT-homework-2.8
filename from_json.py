from mongoengine import connect
import json
from mongoengine import Document, StringField, ListField, ReferenceField



connect(db='GoIT8', host="mongodb+srv://rezvaserg:****@cluster0.5izpshs.mongodb.net/GoIT8?retryWrites=true&w=majority")



class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField()





with open('authors.json', 'r', encoding='utf-8') as authors_file:
    authors_data = json.load(authors_file)

with open('quotes.json', 'r', encoding='utf-8') as quotes_file:
    quotes_data = json.load(quotes_file)

for author_data in authors_data:
    author = Author(**author_data)
    author.save()



for quote_data in quotes_data:
    author_name = quote_data['author']
    author = Author.objects(fullname=author_name).first()
    if author:
        quote_data['author'] = author
        quote = Quote(**quote_data)
        quote.save()

