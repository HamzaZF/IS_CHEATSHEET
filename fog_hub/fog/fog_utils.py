import sqlite3
from fog_config import DB_NAME, TABLE_NAME, FIELD_DEVICE, FIELD_SENSOR, AGG_FUNCTION, AGG_FIELD


def read_aggregates():
    """
    Compute aggregated sensor values per device.
    Returns a list of dicts: {FIELD_DEVICE: device, AGG_FIELD: aggregated_value}
    """
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    sql = (
        f"SELECT {FIELD_DEVICE}, {AGG_FUNCTION}({FIELD_SENSOR}) AS {AGG_FIELD} "
        f"FROM {TABLE_NAME} "
        f"GROUP BY {FIELD_DEVICE} ORDER BY {FIELD_DEVICE} ASC"
    )
    c.execute(sql)
    rows = c.fetchall()
    conn.close()

    return [
        {FIELD_DEVICE: row[0], AGG_FIELD: row[1]}
        for row in rows
    ]
