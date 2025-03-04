import mysql.connector
import itertools
import random
from settings.config import USER, PASSWORD, HOST, DATABASE


class DbConnectionError(Exception):
    pass


def _connect_to_db():
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        auth_plugin='mysql_native_password'
    )
    return cnx


# Function to get all space facts from the database
def get_all_facts():
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print(f"Connected to DB: {DATABASE}")

        query = "SELECT * FROM facts"
        cur.execute(query)
        result = cur.fetchall()  # List of tuples with fact_id and fact

        cur.close()
        return result

    except Exception:
        raise DbConnectionError(f"Failed to fetch facts from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# Function to add a new fact to the database
def add_fact(new_fact):
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        print("ADDING THIS FACT TO THE DB:", new_fact)

        query = """
        INSERT INTO facts (fact) 
        VALUES (%s)
        """
        cur.execute(query)  # Parameterized query with %s

        db_connection.commit()
        print("Fact added successfully.")

        query = """SELECT * FROM facts"""
        cur.execute(query)
        result = cur.fetchall()

        cur.close()
        return result

    except Exception:
        raise DbConnectionError(f"Failed to add fact. ")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# Preparing facts for game use
facts = get_all_facts()
facts_list = [fact[1] for fact in facts]
random.shuffle(facts_list)
fact_data = itertools.cycle(facts_list)

