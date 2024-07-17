import psycopg2
from psycopg2 import sql
from datetime import datetime

def insert_log_into_db(ip, status, timestamp):
    try:
        connection = psycopg2.connect(
            dbname:"",
            user:"",
            password:"",
            host:"",
            port:""
        )
        cursor = connection.cursor()
        insert_query = sql.SQL("""
            INSERT INTO logs (ip, status, timestamp)
            VALUES (%s, %s, %s)
        """)
        cursor.execute(insert_query, (ip, status, datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')))
        connection.commit()
        cursor.close()
        connection.close()
        print(f"Inserted into db: {ip}, {status}, {timestamp}")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")