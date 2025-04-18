import sqlite3

from hub_config import DB_NAME, TABLE_NAME, SENSOR_FIELD, SQL


def insert_reading(device: str, value: str):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        SQL['insert'].format(table=TABLE_NAME, field=SENSOR_FIELD),
        (device, value)
    )
    conn.commit()
    conn.close()


def get_unsent() -> list:
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        SQL['retrieve'].format(table=TABLE_NAME, field=SENSOR_FIELD)
    )
    rows = c.fetchall()
    conn.close()
    return rows


def mark_sent(row_id: int):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        SQL['mark_sent'].format(table=TABLE_NAME),
        (row_id,)
    )
    conn.commit()
    conn.close()
