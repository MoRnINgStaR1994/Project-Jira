from sqlalchemy.dialects.postgresql import psycopg2

from .conn.get_connection import get_connection
from ..utils import hash_password


def create_user(username, password, email, is_verified=False):
    connection = None
    try:
        connection = get_connection()
        with connection:
            with connection.cursor() as cur:
                cur.execute("SELECT 1 FROM persons WHERE email = %s;", (email,))
                if cur.fetchone():
                    print(f"User with email '{email}' already exists.")
                    return False

                hashed_password = hash_password(password)
                cur.execute(
                    """
                    INSERT INTO persons (username, password, email, is_verified) 
                    VALUES (%s, %s, %s, %s);
                    """,
                    (username, hashed_password, email, is_verified)
                )
                return True
    except:
        print("Database error during registration:")
        return False
    finally:
        if (connection):
            connection.close()


def authenticate_user(email, password):
    connection = None
    try:
        connection = get_connection()
        with connection:
            with connection.cursor() as cur:
                cur.execute(
                    "SELECT id, email FROM persons WHERE email = %s AND password = %s AND is_verified = true;",
                    (email, hash_password(password))
                )
                result = cur.fetchone()
                return result
    except psycopg2.Error as e:
        print("Database error:", e)
        return False
    finally:
        if (connection):
            connection.close()

