import pymongo

from mongoengine import connect
from models import Author, Quote


connect(db='GoIT8', host="mongodb+srv://rezvaserg:****@cluster0.5izpshs.mongodb.net/GoIT8?retryWrites=true&w=majority")



try:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client.test_database  
    print("З'єднання успішно встановлено!")
except pymongo.errors.ConnectionFailure as e:
    print("Помилка під час встановлення з'єднання з MongoDB:", e)

while True:
    command = input("Команда: ")

    if command.startswith("name:"):
        author_name = command.split(":")[1].strip()
        author = Author.objects(fullname=author_name).first()
        if author:
            quotes = Quote.objects(author=author)
            for quote in quotes:
                print(quote.quote)
        else:
            print(f"Автор {author_name} не знайдений.")
    
    elif command.startswith("tag:"):
        tag = command.split(":")[1].strip()
        quotes = Quote.objects(tags=tag)
        for quote in quotes:
            print(quote.quote)
    
    elif command.startswith("tags:"):
        tags = command.split(":")[1].strip().split(",")
        quotes = Quote.objects(tags__in=tags)
        for quote in quotes:
            print(quote.quote)
    
    elif command == "exit":
        break

    else:
        print("Невідома команда. Спробуйте ще раз.")
