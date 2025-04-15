import psycopg2
from sqlalchemy.dialects.postgresql import psycopg2
import psycopg2.extras
from .conn.get_connection import get_connection
from ..models.Ticket import Ticket


def insert_new_ticket(ticket: Ticket):
    connection = None
    try:
        connection = get_connection()
        with connection:
            with connection.cursor() as cur:
                cur.execute(
                    "INSERT INTO tickets (title, description, estimation, priority, status, board_id) VALUES (%s, %s, %s, %s, %s, %s)",
                    (ticket.title, ticket.description, ticket.estimation, ticket.priority, ticket.status, ticket.board_id, )
                )

                return True
    except psycopg2.Error as e:
        print("Database error:", e)
        return False
    finally:
        if connection:
            connection.close()

def get_project_owner(id: int):
    connection = None
    try:
        connection = get_connection()
        with connection:
            with connection.cursor() as cur:
                cur.execute(
                    "SELECT user_id FROM projects WHERE id = %s",
                    (id,)
                )
                result = cur.fetchone()
                return result[0]
    except psycopg2.Error as e:
        print("Database error:", e)
        return False
    finally:
        if connection:
            connection.close()


def delete_project_board_ticket(id: int):
    connection = None
    try:
        connection = get_connection()
        with connection:
            with connection.cursor() as cur:
                cur.execute(
                    "DELETE FROM tickets WHERE id = %s",
                    (id,)
                )
                return True

    except psycopg2.Error as e:
        print("Database error:", e)
        return False
    finally:
        if connection:
            connection.close()


def get_ticket_owner(id: int):
    connection = None
    try:
        connection = get_connection()
        with connection:
            with connection.cursor() as cur:
                cur.execute(
                    "SELECT p.user_id FROM tickets as t INNER JOIN boards as b ON t.board_id = b.id INNER JOIN projects as p ON b.project_id = p.id WHERE t.id = %s",
                    (id,)
                )
                result = cur.fetchone()

                if not result:
                    return None
                return result[0]
    except Exception as e:
        print("Database error:", e)
        return None
    finally:
        if connection:
            connection.close()


def get_ticket_details(id: int):
    connection = None
    try:
        connection = get_connection()
        with connection:
            with connection.cursor() as cur:
                cur.execute(
                    "SELECT * FROM tickets WHERE id = %s",
                    (id,)
                )
                columns = [col[0] for col in cur.description]
                rows = cur.fetchall()
                results = [dict(zip(columns, row)) for row in rows]
                ticket = [Ticket(**result) for result in results]

                if not results:
                    return None
                return ticket[0]
    except Exception as e:
        print("Database error:", e)
        return None
    finally:
        if connection:
            connection.close()


def get_ticket_by_id(ticket_id: int):
    connection = None
    try:
        connection = get_connection()
        with connection:

            with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute(
                    "SELECT * FROM tickets WHERE id = %s",
                    (ticket_id,)
                )
                ticket = cur.fetchone()
                return ticket
    except Exception as e:
        print("Database error:", e)
        return None
    finally:
        if connection:
            connection.close()


def update_ticket(ticket_id: int, data: dict):
    connection = None
    try:
        connection = get_connection()
        with connection:
            with connection.cursor() as cur:
                cur.execute(
                    """
                    UPDATE tickets
                    SET title = %s, description = %s, estimation = %s, priority = %s, status = %s
                    WHERE id = %s
                    """,
                    (
                        data["title"],
                        data["description"],
                        data["estimation"],
                        data["priority"],
                        data["status"],
                        ticket_id,
                    )
                )
                return True
    except Exception as e:
        print("Database error:", e)
        return False
    finally:
        if connection:
            connection.close()

