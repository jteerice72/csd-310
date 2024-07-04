#jessica hall
#CSD310


import mysql.connector

# establish connection to SQL db
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0910",
    database="movies"
)


cursor = db_connection.cursor()

try:
    # query 1: select all fields for the studios table
    query = "SELECT * FROM studios;"
    cursor.execute(query)
    studios = cursor.fetchall()

    # display studio records
    print("-- DISPLAYING Studio RECORDS. --")
    for studio in studios:
        print(f"Studio ID: {studio[0]}")
        print(f"Studio Name: {studio[1]}")
    print()

    # query 2: select all fields for the genres table
    query = "SELECT * FROM genres;"
    cursor.execute(query)
    genres = cursor.fetchall()

    # display genre records
    print("= DISPLAYING Genre RECORDS --")
    for genre in genres:
        print(f"Genre ID: {genre[0]}")
        print(f"Genre Name: {genre[1]}")
    print()

    # query 3:select movie names for movies that have a runtime of less than two hours
    query = "SELECT film_name, runtime FROM films WHERE runtime < 120;"
    cursor.execute(query)
    short_films = cursor.fetchall()

    # display short film records
    print("=- DISPLAYING Short Film RECORDS --")
    for film in short_films:
        print(f"Film Name: {film[0]}")
        print(f"Runtime: {film[1]}")
    print()

    # query 4:list of film names and directors grouped by director
    query = "SELECT film_name, director FROM films ORDER BY director;"
    cursor.execute(query)
    director_films = cursor.fetchall()

    # displaying director records in order
    print("DISPLAYING Director RECORDS in Order --")
    current_director = None
    for film in director_films:
        if film[1] != current_director:
            print(f"Director: {film[1]}")
            current_director = film[1]
        print(f"Film Name: {film[0]}")
    print()

except mysql.connector.Error as error:
    print("Error reading data from MySQL table:", error)

finally:
    # closing cursor and database connection
    if db_connection.is_connected():
        cursor.close()
        db_connection.close()
        print("MySQL connection is closed")





# close cursor and connection
cursor.close()
db_connection.close()