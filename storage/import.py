import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#Creating the connection
engine = create_engine("postgres://rrcgpldedfwzsy:a327a7d195c293981f53baa91a8af5045c10ce642fd44b61ed87f2c77723e013@ec2-52-44-55-63.compute-1.amazonaws.com:5432/dc1scm7s3mgdqv")
db = scoped_session(sessionmaker(bind=engine))



#db.execute("INSERT INTO usuario(id, usuario, password) VALUES (1, 'asd', 'asd')")
#db.commit()
#usuario = db.execute("SELECT * FROM usuario")
#print(usuario.fetchall())



def main():
    f = open("books.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
    
        db.execute("INSERT INTO book (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                    {"isbn": isbn, "title": title, "author": author, "year": year})
    db.commit()
    print("Proccess successful.")
if __name__ == "__main__":
    main()
