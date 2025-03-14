import json

from sqlalchemy.dialects.postgresql import psycopg2
from .conn.get_connection import get_connection
from ..models.Project import Project
from ..models.Board import Board
from psycopg2.extras import RealDictCursor


def insert_new_project(project: Project):
    connection = None
    try:
        connection = get_connection()
        with connection:
            with connection.cursor() as cur:
                cur.execute(
                    "INSERT INTO projects (name, user_id, description, is_active) VALUES (%s, %s, %s, true)",
                    (project.name, project.user_id, project.description)
                )

                return True
    except psycopg2.Error as e:
        print("Database error:", e)
        return False
    finally:
        if connection:
            connection.close()


def list_user_projects(id: int):
    connection = None
    try:
        connection = get_connection()
        with connection:
            with connection.cursor() as cur:
                cur.execute(
                    "SELECT * FROM projects WHERE user_id = %s",
                    (id,)
                )

                columns = [col[0] for col in cur.description]
                rows = cur.fetchall()
                results = [dict(zip(columns, row)) for row in rows]
                projects = [Project(**result) for result in results]

                return projects
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
                if not result:
                    return None
                return result[0]
    except Exception as e:
        print("Database error:", e)
        return None
    finally:
        if connection:
            connection.close()

def delete_user_project(id: int):
    connection = None
    try:
        connection = get_connection()
        with connection:
            with connection.cursor() as cur:
                cur.execute(
                    "DELETE FROM projects WHERE id = %s",
                    (id,)
                )
                return True
    except Exception as e:
        print("Database error:", e)
        return None
    finally:
        if connection:
            connection.close()


def create_project_board(board: Board):
    connection = None
    try:
        connection = get_connection()
        with connection:
            with connection.cursor() as cur:
                cur.execute(
                    "INSERT INTO boards (name, project_id, board_columns) VALUES (%s, %s, %s)",
                    (board.name, board.project_id, board.board_columns)
                )

                return True
    except Exception as e:
        print("Database error:", e)
        return None
    finally:
        if connection:
            connection.close()



def delete_project_board(id:int):
    connection = None
    try:
        connection = get_connection()
        with connection:
            with connection.cursor() as cur:
                cur.execute(
                    "DELETE FROM boards WHERE id = %s",
                    (id,)
                )
                return True
    except Exception as e:
        print("Database error:", e)
        return None
    finally:
        if connection:
            connection.close()


def get_project_id(id: int):
    connection = None
    try:
        connection = get_connection()
        with connection:
            with connection.cursor() as cur:
                cur.execute(
                    "SELECT project_id FROM boards WHERE id = %s",
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


def get_project_details(id: int, user_id: int):
    connection = None
    try:
        connection = get_connection()
        with connection:
            with connection.cursor() as cur:
                cur.execute(
                    "SELECT * FROM projects WHERE user_id = %s AND id = %s",
                    (user_id, id,)
                )
                columns = [col[0] for col in cur.description]
                rows = cur.fetchall()
                results = [dict(zip(columns, row)) for row in rows]
                if not results:
                    return None
                return results[0]
    except Exception as e:
        print("Database error:", e)
        return None
    finally:
        if connection:
            connection.close()

def list_boards(id: int):
    connection = None
    try:
        connection = get_connection()
        with connection:
            with connection.cursor() as cur:
                cur.execute(
                    "SELECT * FROM boards WHERE project_id = %s",
                    (id,)
                )

                columns = [col[0] for col in cur.description]
                rows = cur.fetchall()
                results = [dict(zip(columns, row)) for row in rows]
                boards = [Board(**result) for result in results]

                return boards
    except Exception as e:
        print("Database error:", e)
        return None
    finally:
        if connection:
            connection.close()


def get_board_details(id: int):
    connection = None
    try:
        connection = get_connection()
        with connection:
            with connection.cursor() as cur:
                cur.execute(
                    "SELECT * FROM boards WHERE id = %s",
                    (id,)
                )
                columns = [col[0] for col in cur.description]
                rows = cur.fetchall()
                results = [dict(zip(columns, row)) for row in rows]

                if not results:
                    return None
                return results[0]

    finally:
        if connection:
            connection.close()


def get_board_tickets(id: int):
    connection = None
    try:
        connection = get_connection()
        with connection:
            with connection.cursor() as cur:
                cur.execute(
                    "SELECT * FROM tickets WHERE board_id = %s",
                    (id,)
                )
                columns = [col[0] for col in cur.description]
                rows = cur.fetchall()
                results = [dict(zip(columns, row)) for row in rows]

                if not results:
                    return None
                return results
    except Exception as e:
        print("Database error:", e)
        return None
    finally:
        if connection:
            connection.close()


def update_project(data: dict, id):
    connection = None
    print(data)
    try:
        connection = get_connection()
        with connection:
            with connection.cursor() as cur:
                cur.execute(
                    "UPDATE projects SET name = %s, description = %s, is_active = %s WHERE id = %s",
                    (data.name, data.description, data.is_active, id)
                )
                return True
    except Exception as e:
        print("Database error:", e)
        return False
    finally:
        if connection:
            connection.close()


def get_project_by_id(project_id: int):
    connection = None
    try:
        connection = get_connection()
        with connection:
            with connection.cursor(dictionary=True) as cur:
                cur.execute("SELECT * FROM projects WHERE id = %s", (project_id,))
                result = cur.fetchone()

                if result is None:
                    raise Exception("Project not found or not accessible")

                return result
    except Exception as e:
        print(f"Error fetching project: {e}")
        return None
    finally:
        if connection:
            connection.close()


def get_board_by_id(board_id: int):
    connection = None
    try:
        connection = get_connection()
        with connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    "SELECT * FROM boards WHERE id = %s",
                    (board_id,)
                )
                result = cur.fetchone()
                return result
    except Exception as e:
        print("Database error:", e)
        return None
    finally:
        if connection:
            connection.close()


def update_board(board_id: int, data: dict) -> bool:
    connection = None
    try:
        connection = get_connection()
        with connection:
            with connection.cursor() as cur:
                cur.execute(
                    """
                    UPDATE boards
                    SET name = %s, board_columns = %s
                    WHERE id = %s
                    """,
                    (data["name"], json.dumps(data["board_columns"]), board_id)
                )
                return True
    finally:
        if connection:
            connection.close()

