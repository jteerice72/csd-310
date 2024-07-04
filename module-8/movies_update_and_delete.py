#jessica hall
#csd310

import mysql.connector

def display_films(cursor, title=""):
    try:
        # Query to select films with joined genre and studio names
        select_query = """
        SELECT f.film_name, f.director, g.genre_name AS genre, s.studio_name AS studio
        FROM films f
        INNER JOIN genres g ON f.genre_id = g.genre_id
        INNER JOIN studios s ON f.studio_id = s.studio_id
        ORDER BY f.film_name
        """

        # Execute the select query
        cursor.execute(select_query)

        # Fetch all rows
        films = cursor.fetchall()

        # Display output for films
        print(f"-- DISPLAYING FILMS {title} --")
        for film in films:
            print(f"Film Name: {film[0]}")
            print(f"Director: {film[1]}")
            print(f"Genre Name: {film[2]}")
            print(f"Studio Name: {film[3]}")
            print()  # Blank line for separation

    except mysql.connector.Error as error:
        print(f"Error fetching films: {error}")

def insert_film(cursor, film_name, director, genre_id, studio_id):
    try:
        # Insert film into films table
        insert_query = """
        INSERT INTO films (film_name, director, genre_id, studio_id)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (film_name, director, genre_id, studio_id))
        print(f"Successfully inserted film: {film_name}")

        # Display films after insert
        display_films(cursor, "AFTER INSERT")

    except mysql.connector.Error as error:
        print(f"Error inserting film: {error}")

def delete_film(cursor, film_name, director):
    try:
        # Delete film from films table
        delete_query = """
        DELETE FROM films
        WHERE film_name = %s AND director = %s
        """
        cursor.execute(delete_query, (film_name, director))
        print(f"Successfully deleted film: {film_name}")

        # Display films after delete
        display_films(cursor, "AFTER DELETE")

    except mysql.connector.Error as error:
        print(f"Error deleting film: {error}")

if __name__ == "__main__":
    try:
        # Establish connection to MySQL database
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="0910",
            database="movies"
        )

        # Create a cursor object using the cursor() method
        cursor = db_connection.cursor()

        # Display films before any operations
        display_films(cursor)


        # Delete a film (example)
        delete_film(cursor, "Gladiator", "Ridley Scott")

        # Commit changes to the database
        db_connection.commit()

    except mysql.connector.Error as error:
        print(f"Error connecting to MySQL: {error}")

    finally:
        # Close cursor and database connection
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'db_connection' in locals() and db_connection and db_connection.is_connected():
            db_connection.close()
            print("MySQL connection is closed")
