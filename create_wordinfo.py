import sqlite3
from collections import Counter

def insert_words(filename, db_file):
    """Inserts words from a text file into a SQLite database.

    Args:
        filename: The name of the text file containing words.
        db_file: The name of the SQLite database file.
    """

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS words (
            word TEXT PRIMARY KEY,
            length INTEGER,
            letters TEXT,
            a INTEGER,
            b INTEGER,
            c INTEGER,
            d INTEGER,
            e INTEGER,
            f INTEGER,
            g INTEGER,
            h INTEGER,
            i INTEGER,
            j INTEGER,
            k INTEGER,
            l INTEGER,
            m INTEGER,
            n INTEGER,
            o INTEGER,
            p INTEGER,
            q INTEGER,
            r INTEGER,
            s INTEGER,
            t INTEGER,
            u INTEGER,
            v INTEGER,
            w INTEGER,
            x INTEGER,
            y INTEGER,
            z INTEGER
        )
    ''')

    # Insert words from the file
    with open(filename, 'r') as f:
        for word in f:
            word = word.strip().lower()
            length = len(word)
            letters = ''.join(sorted(word))
            letter_counts = Counter(word)


            values = [word, letters, length]  # Start with word and letters
            values.extend(letter_counts[chr(ord('a') + i)] for i in range(26))

            sql_query = f"INSERT INTO words (word, letters, length, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(sql_query, values)

    # Create an index on the first two letters of the word
    # Create indexes
    cursor.execute('CREATE INDEX IF NOT EXISTS word_length_index ON words(length)')
    cursor.execute('CREATE INDEX IF NOT EXISTS word_letters_index ON words(letters COLLATE NOCASE)')

    # Create indexes for each letter count
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        cursor.execute(f'CREATE INDEX IF NOT EXISTS word_{letter}_index ON words({letter})')


    conn.commit()
    conn.close()

# Example usage:
filename = 'wordlist.txt'
db_file = 'wordinfo.db'
insert_words(filename, db_file)