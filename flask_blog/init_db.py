# import sqlite3
import os
import psycopg2

connection = psycopg2.connect(
    host='postgres',
    database='flaskblog',
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'])

cur = connection.cursor()

cur.execute('DROP TABLE IF EXISTS posts;')
cur.execute('CREATE TABLE posts (id SERIAL PRIMARY KEY,'
            'created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,'
            'title TEXT NOT NULL,'
            'content TEXT NOT NULL);'
            )

cur.execute("INSERT INTO posts (title, content) VALUES (%s, %s)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (%s, %s)",
            ('Second Post', 'Content for the second post')
            )

connection.commit()
connection.close()
cur.close()
