#%%

import mysql.connector
host = "sql3.freesqldatabase.com"
database_name = "sql3653594"
user = "sql3653594"
password = "7kekrJ16Li"
port = 3306

try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database_name,
        port=port
    )
    if connection.is_connected():
        print("Connected to the database")
except mysql.connector.Error as e:
    print(f"Error connecting to the database: {e}")

cursor = connection.cursor()


#%%

create_table_query = """
CREATE TABLE job_listings (
    listing_id int,
    title varchar(255),
    salary int
);
"""

cursor.execute(create_table_query)
connection.commit()


#%%
query = """
INSERT INTO job_listings (title, salary) 
VALUES ('software engineer', 100000);

"""

cursor.execute(query)
connection.commit()


#%%
# query = """
# SELECT column_name
# FROM information_schema.columns
# WHERE table_name = 'job_listings';
# """
query = """
ALTER TABLE job_listings
ADD COLUMN new_id INT AUTO_INCREMENT PRIMARY KEY;
"""

cursor.execute(query)


#%%
query = """
SELECT * FROM job_listings;
"""
cursor.execute(query)

results = cursor.fetchall()
results


#%%
cursor.close()
connection.close()

