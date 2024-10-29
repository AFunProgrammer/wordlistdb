# !important - each file has been parsed in to A.txt B.txt C.txt ... Z.txt
#              the output file is named wordlist.db with a table for each
#              letter.


import sqlite3

def create_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create a table for each letter of the alphabet
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        cursor.execute(f"CREATE TABLE {letter} (word TEXT)")

    conn.commit()
    conn.close()

def import_data(db_name, file_prefix):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        filename = f"{letter}.txt"
        with open(filename, 'r') as f:
            for word in f:
                word = word.strip().lower()  # Convert word to lowercase
                cursor.execute(f"INSERT INTO {letter} (word) VALUES (?)", (word.strip(),))

    conn.commit()
    conn.close()

# Replace 'my_database.db' with your desired database name
database_name = 'wordlist.db'
file_prefix = ''  # Assuming files are in the same directory

create_database(database_name)
import_data(database_name, file_prefix)

