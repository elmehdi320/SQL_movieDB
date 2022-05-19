import sqlite3

#connect to database (create if it dosen't exist yet/ get in if it's already there )
conn = sqlite3.connect("NewDataBase.db")

#Create a cursor
cursor = conn.cursor()

#Create a table

#Data types in SQlite:
#NULL(null if it doesn't exist)/INTEGER(int)/REAL(float)/TEXT(str)/BLOB(data)
cursor.execute(""" CREATE TABLE Movies (
        movieName TEXT,
        releaseYear INTEGER,
        movieGenre TEXT,
        Rating REAL,
        personalRating REAL
    )""")

#Commit commands(table creation)
conn.commit()

#close connection
conn.close()
