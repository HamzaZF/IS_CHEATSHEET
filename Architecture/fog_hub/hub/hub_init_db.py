import sqlite3
from hub_config import DB_NAME, TABLE_NAME, SENSOR_FIELD

def init_db():
    """
    Create the sensor data table if it does not exist.
    """
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # Define schema matching hub code expectations
    c.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            devicename CHARACTER(5) NOT NULL,
            {SENSOR_FIELD} INTEGER NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            tocloud BOOLEAN DEFAULT 0 NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print(f"Ensured table '{TABLE_NAME}' exists in database '{DB_NAME}'")
