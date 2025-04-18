import sqlite3
from flask import make_response, abort
from joblib import load

from cloud_config import DB_NAME, TABLE_NAME, FIELD_DEVICE, FIELD_SENSOR, FIELD_TIMESTAMP, CLUSTER_MODEL


def read_records():
    """
    Retrieve all sensor records from the database
    """
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        f"SELECT id, {FIELD_DEVICE}, {FIELD_SENSOR}, {FIELD_TIMESTAMP} "
        f"FROM {TABLE_NAME} ORDER BY id ASC"
    )
    rows = c.fetchall()
    conn.close()

    # Build list of dicts
    return [
        {
            'id': row[0],
            FIELD_DEVICE: row[1],
            FIELD_SENSOR: row[2],
            FIELD_TIMESTAMP: row[3]
        }
        for row in rows
    ]


def create_record(data):
    """
    Insert a new sensor record into the database
    """
    dev = data.get(FIELD_DEVICE)
    val = data.get(FIELD_SENSOR)
    ts  = data.get(FIELD_TIMESTAMP)

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # Professors' inline SQL, adapted with config
    sql = (
        f"INSERT INTO {TABLE_NAME} "
        f"({FIELD_DEVICE}, {FIELD_SENSOR}, {FIELD_TIMESTAMP}) "
        f"VALUES('{dev}', {val}, '{ts}')"
    )
    print(sql)
    c.execute(sql)
    conn.commit()
    conn.close()

    return make_response('Record successfully created', 200)


def cluster_value(value):
    """
    Predict cluster label for a new sensor value
    """
    try:
        model = load(CLUSTER_MODEL)
        label = model.predict([[value]])[0]
        print(f'Cluster: value={value}; label={label}')
        return str(label)
    except Exception as e:
        print(f'Error: {e}')
        abort(500, 'Clustering error')
