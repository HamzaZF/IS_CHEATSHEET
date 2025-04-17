import sqlite3
from datetime import datetime

def get_connection():
    return sqlite3.connect("example.db")

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS temperature (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            devicename TEXT NOT NULL,
            temp REAL NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    print("✅ Table 'temperature' created (if not exists).")

def insert_single(conn, devicename, temp):
    cursor = conn.cursor()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("""
        INSERT INTO temperature (devicename, temp, timestamp)
        VALUES (?, ?, ?)
    """, (devicename, temp, timestamp))
    conn.commit()
    print(f"✅ Inserted {devicename} with temp {temp}°C")

def insert_multiple(conn, data_list):
    cursor = conn.cursor()
    formatted_data = [(d[0], d[1], datetime.now().strftime('%Y-%m-%d %H:%M:%S')) for d in data_list]
    cursor.executemany("""
        INSERT INTO temperature (devicename, temp, timestamp)
        VALUES (?, ?, ?)
    """, formatted_data)
    conn.commit()
    print(f"✅ Inserted {len(data_list)} records.")

def select_all(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM temperature")
    rows = cursor.fetchall()
    print("📋 All records:")
    for row in rows:
        print(row)

def select_filtered(conn, min_temp):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM temperature WHERE temp > ? ORDER BY temp DESC", (min_temp,))
    rows = cursor.fetchall()
    print(f"📋 Devices with temp > {min_temp}°C:")
    for row in rows:
        print(row)

def count_records(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM temperature")
    count = cursor.fetchone()[0]
    print(f"🔢 Total records: {count}")

def update_temp(conn, devicename, new_temp):
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE temperature SET temp = ?, timestamp = ?
        WHERE devicename = ?
    """, (new_temp, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), devicename))
    conn.commit()
    print(f"🔄 Updated {devicename} to {new_temp}°C")

def delete_device(conn, devicename):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM temperature WHERE devicename = ?", (devicename,))
    conn.commit()
    print(f"❌ Deleted entries for {devicename}")

def clear_table(conn):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM temperature")
    conn.commit()
    print("🧹 Table cleared (all rows deleted).")

def show_latest(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM temperature ORDER BY timestamp DESC LIMIT 1")
    row = cursor.fetchone()
    print("🕒 Most recent record:")
    print(row)

def main():
    conn = get_connection()

    create_table(conn)

    # Insert examples
    insert_single(conn, "mb1", 23.4)
    insert_multiple(conn, [("mb2", 25.6), ("mb3", 21.9)])

    # Select examples
    select_all(conn)
    select_filtered(conn, 22)
    show_latest(conn)

    # Utility examples
    count_records(conn)

    # Update and delete
    update_temp(conn, "mb2", 26.5)
    delete_device(conn, "mb3")

    # Final view
    select_all(conn)

    conn.close()
    print("✅ Connection closed.")

if __name__ == "__main__":
    main()
