import sqlite3
import logging

def init_db():
    # creating my db if it doesnt exist yet
    conn = sqlite3.connect("sessions.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sessions (session_id TEXT PRIMARY KEY, document_text TEXT)
    """)
    logging.info("table created successfully")
    conn.commit()
    conn.close()

def update_database(session_id, text):
    conn = sqlite3.connect("sessions.db")
    cursor = conn.cursor()

    sql_command = """
        INSERT OR REPLACE INTO sessions (session_id, document_text) VALUES (?, ?)
    """
    cursor.execute(sql_command, (session_id, text))

    conn.commit()
    conn.close()

def get_text_from_session(session_ID):
    conn = sqlite3.connect("sessions.db")
    cursor = conn.cursor()
    try:
        sql_command = """
            SELECT document_text FROM sessions WHERE session_id = ?
        """
        cursor.execute(sql_command, (session_ID,))
        session_text = cursor.fetchone()
        logging.info("Retrieved text successfully")
        conn.close()
    except Exception as e:
        return e

    if session_text is None:
        return None
    else:
        return session_text[0]

def delete_session(session_ID):
    conn = sqlite3.connect("sessions.db")
    cursor = conn.cursor()
    try:
        sql_command = """
            DELETE FROM sessions WHERE session_id = ?
        """
        cursor.execute(sql_command, (session_ID,))
        conn.commit()
        logging.info(f"Session {session_ID} deleted successfully.")
    except Exception as e:
        logging.error(f"Error deleting session {session_ID}: {e}")
    finally:
        conn.close()