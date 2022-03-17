import sqlite3

data = []
con = sqlite3.connect('db.sqlite3')
cursor = con.cursor()

result = cursor.execute('SELECT * FROM book_book join book_author on book_book.author_id = book_author.id WHERE author_id =2')
for row in result:
    print(row)
    data.append(row)
con.close()

print(result)
print(data)
