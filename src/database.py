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
        