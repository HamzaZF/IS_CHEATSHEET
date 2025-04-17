import sqlite3
from cloud_config import DB_NAME, TABLE_NAME, FIELD_DEVICE, FIELD_SENSOR, FIELD_TIMESTAMP, FIELD_TOCLOUD

def init_db():
    """
    Creates the sensor table in the cloud database if it doesn't exist.
    """
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # Build CREATE TABLE statement dynamically
    c.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            {FIELD_DEVICE} CHARACTER(5) NOT NULL,
            {FIELD_SENSOR} INTEGER NOT NULL,
            {FIELD_TIMESTAMP} DATETIME DEFAULT CURRENT_TIMESTAMP,
            {FIELD_TOCLOUD} BOOLEAN DEFAULT 0 NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print(f"Ensured table '{TABLE_NAME}' exists in database '{DB_NAME}'")
