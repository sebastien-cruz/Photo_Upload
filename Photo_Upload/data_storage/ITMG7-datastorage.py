import psycopg2

conn = psycopg2.connect(database="virtualcloset-db", user="postgres", host="localhost", password="8600", port=5432)

# Open a cursor
cur = conn.cursor()

#Create users table
cur.execute("""CREATE TABLE users (
		username TEXT,
		first_name TEXT,
        last_name TEXT
		)""")

		
#create closet table
cur.execute("""CREATE TABLE user_closet (
		username TEXT,
		photo BYTEA,
		color TEXT,
		type TEXT,
        size TEXT
		)""")

# Commit all changes to the database
conn.commit()


# Close cursor and communication with the database
cur.close()
conn.close()

print("Data tables created")
