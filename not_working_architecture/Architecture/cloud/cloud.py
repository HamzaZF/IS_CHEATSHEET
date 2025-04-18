import connexion
import sqlite3
from cloud_config import DB_NAME, TABLE_NAME, FIELD_DEVICE, FIELD_SENSOR, FIELD_TIMESTAMP

app = connexion.App(__name__, specification_dir='./')
app.add_api('cloud.yml')

def generate_html_table(rows, columns):
    """
    Build an HTML table given:
      - rows:   a list of tuples, each tuple matching the columns order
      - columns: a list of column names (strings) to use as headers
    """
    # table header
    html = '<table cellspacing="1" cellpadding="3" border="1"><tr>'
    for col in columns:
        html += f'<th>{col.capitalize()}</th>'
    html += '</tr>'

    # table body
    for row in rows:
        html += '<tr>'
        for cell in row:
            html += f'<td>{cell}</td>'
        html += '</tr>'
    html += '</table>'
    return html

@app.route('/')
def index():
    # define which columns to select and display
    columns = ['id', FIELD_DEVICE, FIELD_SENSOR, FIELD_TIMESTAMP]
    cols_sql = ', '.join(columns)

    # fetch data
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(f"SELECT {cols_sql} FROM {TABLE_NAME} ORDER BY id DESC")
    results = c.fetchall()
    conn.close()

    # build full HTML
    html = (
        '<html><head><title>Cloud Server</title>'
        '<meta http-equiv="refresh" content="5" /></head><body>'
        '<h1>Global Sensor Data</h1>'
    )
    html += generate_html_table(results, columns)
    html += '</body></html>'

    return html

# Stand‑alone run
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
