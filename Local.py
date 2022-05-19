import sqlite3

#connect to database (create if it dosen't exist yet/ get in if it's already there )
conn = sqlite3.connect("NewDataBase.db")

#Create a cursor
cursor = conn.cursor()

#get user's goal:
userGoal = input("""*please enter 1 if you want to visualize the database content
*please enter 2 if you want to add a movie to the database ---> """)

#-------------------------------------------------------------------------------------------------------------
# OPTION 1: Show database content
if userGoal == "1":
    cursor.execute("SELECT * FROM movies")
    dataList = cursor.fetchall()
    print(" movie | director | year | genre | rating ")
    for i in dataList:
        print(i)

#OPTION 2: Add a movie to the table
elif userGoal == "2":

    movieName = input("enter the movies\'s name: ")
    directorName = input("enter the movies\'s director\'s name: ")
    releaseYear = input("enter the year the movies where published: ")
    movieGenre = input("enter the movies\'s genre: ")
    movieRating = input("enter the movies\'s rating (0.0 -> 10.0): ")

    cursor.execute("INSERT INTO movies VALUES (\'"+ movieName +"\', \'"+directorName+"\', \'"+ releaseYear +"\', \'"+ movieGenre +"\', \'"+ movieRating +"\')")

#OPTION 3: The input is wrong -> return an error message.
else:
    print("Wrong input !!!")

#Commit commands(data insertion)
conn.commit()

#close connection
conn.close()
