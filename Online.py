import sqlite3
import requests
from colorama import Fore,Style

def visulize():
    cursor.execute("SELECT * FROM Movies")
    dataList = cursor.fetchall()
    print("Movie title                             | Release year | Genre                                   | Rating | Personal-rating ")
    print("----------------------------------------------------------------------------------------------------------------------------")
    for i in dataList:
        print("%-40s%-1s%-13s%-1s%-40s%-1s%-7s%-1s%-8s" % (i[0], "| ", i[1], "| ", i[2], "| ", i[3], "| ", i[4]))

def addToDb():
    """add a movie to the data base in a local way
    None(0 parameters) -> None"""
    movieName = input("enter the movies\'s name: ")
    releaseYear = input("enter the year the movies where published: ")
    movieGenre = input("enter the movies\'s genre: ")
    movieRating = input("enter the movies\'s rating (0.0 -> 10.0): ")
    persoanlRating = input("enter your personal rating (0.0 -> 10.0): ")

    cursor.execute("INSERT INTO Movies VALUES (\'"+ movieName +"\', \'"+ releaseYear +"\', \'"+ movieGenre +"\', \'"+ movieRating +"\', \'"+ persoanlRating +"\')")

def PickMovie():
    """add a movie to the data base in an online way
    None(0 parameters) -> None"""
    search = input("Movie search: ")
    token = input("input your programmer token: ")#if yo don't have one get if from https://www.themoviedb.org/
    r = requests.get("https://api.themoviedb.org/3/search/movie?api_key="+token+"&language=en-US&query=" + search + "&page=1&include_adult=false")
    # check if there are results
    if r.json()['results'] == []:
        print(Fore.RED + "THERE ARE NO RESULTS,try again !! ")

    # print results (from page 1) one by one
    else:
        print(Fore.RED +   "id     | Title                                                                                              | Release Date  | Rating | Genre")
        print(Fore.WHITE + "-------------------------------------------------------------------------------------------------------------------------------------------------")
        for result in r.json()['results']:
            print("%-7s%-1s%-100s%-1s%-15s%-1s%-10s%-1s%-1s" % (result["id"], "|", result["original_title"], "|", result["release_date"], "|", result["vote_average"], "|", GetGenre(result["genre_ids"])))

    choosenId = input("write down the id of the movie you want to add: ")
    for result in r.json()['results']:
        if result["id"] == int(choosenId):
            movieName = result["original_title"]
            if result["release_date"] != "":
                releaseYear = int(result["release_date"][:4])
            else:
                releaseYear = -1
            if result["genre_ids"] != []:
                movieGenre = GetGenre(result["genre_ids"])
            else:
                movieGenre = "None"

            movieRating = result["vote_average"]
            persoanlRating = input("enter your personal rating (0.0 -> 10.0): ")
            cursor.execute("INSERT INTO Movies VALUES (\'" + movieName + "\', \'" + str(releaseYear) + "\', \'" + movieGenre + "\', \'" + str(movieRating) + "\', \'" + str(persoanlRating) + "\')")

def GetGenre(list):
    """transform genre id  into genre in str
        list(1 parameters) -> str"""
    strForm = ""
    Genres = {28:"Action",12:"Adventure",16:"Animation",35:"Comedy",80:"Crime",99:"Documentary",18:"Drama",10751:"Family"
        ,14:"Fantasy",36:"History",27:"Horror",10402:"Music",9648:"Mystery",10749:"Romance",878:"Science-Fiction"
        ,10770:"TV Movie",53:"Thriller",10752:"War",37:"Western"}
    for genreId in list:
        if genreId in Genres.keys():
            strForm = strForm + Genres[genreId] + " "
    return strForm


#-------------------------------------------------MAIN PROGRAMM-----------------------------------------------
#connect to database (create if it dosen't exist yet/ get in if it's already there )
conn = sqlite3.connect("NewDataBase.db")
#Create a cursor
cursor = conn.cursor()
#-------------------------------------------------------------------------------------------------------------
#get user's goal:
userGoal = input("""*please enter 1 if you want to visualize the database content
*please enter 2 if you want to add a movie 
*please enter 3 if you want to add a movie from an online database
 ---> """)

# OPTION 1: Show database content
if userGoal == "1":
    visulize()
#OPTION 2: Add a movie to the table
elif userGoal == "2":
    addToDb()
#OPTION 3: add a movie from an online database
elif userGoal == "3":
    PickMovie()
#OPTION 4: The input is wrong -> return an error message.
else:
    print("Wrong input !!!")

#-------------------------------------------------------------------------------------------------------------
#Commit commands(data insertion)
conn.commit()
#close connection
conn.close()
