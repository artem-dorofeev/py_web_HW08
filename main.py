from models import Quote, Author
import connect

def print_help():
    print('Help about command:')
    print('name <Name Author>- search about name')
    print('tag <tag>- search about tag')
    print('tags <tag>,<tag>- search about tags')
    print('exit - exit without app')

def get_quots_by_tags(value):
    tags = value.split(",")
    print (tags)
    for tag in tags:
        quotes = Quote.objects(tags=tag.strip())
        if quotes:
            for quote in quotes:
                print(f'{quote.author.fullname}: {quote.quote}')
        else:
            print(f"Sorry, tag's '{tag}' not found")


def get_quots_by_tag(value):
    quotes = Quote.objects(tags=value.strip())
    if quotes:
        for quote in quotes:
            print(f'{quote.author.fullname}: {quote.quote}')
    else:
        print(f"Sorry, tag '{value}' not found")


def get_quots_by_name(value):
    author = Author.objects(fullname=value.strip()).first()
    if author:
        quotes = Quote.objects(author=author)
        for quote in quotes:
            print(f'{author.fullname}: {quote.quote}')
    else:
        print(f'Sorry, author: {author} not found')


def main():
    print_help()
    while True:

        command = input("Input command: ")
        if command.strip() == 'exit':
            print("The end")
            break

        if command.strip().startswith("name"):
            author_name = command.split("name")[1].strip()
            get_quots_by_name(author_name)
        elif command.strip().startswith("tags"):
            value = command.split("tags")[1].strip()
            get_quots_by_tags(value)
        elif command.strip().startswith("tag"):
            value = command.split("tag")[1].strip()
            get_quots_by_tag(value)
        
        else:
            print (f"Unknow command - {command}")
    
if __name__ == "__main__":
    main()
