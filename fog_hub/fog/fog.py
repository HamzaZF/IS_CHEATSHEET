import connexion
from fog_config import API_SPEC, DB_NAME, TABLE_NAME, FIELD_DEVICE, AGG_FIELD
from fog_utils import read_aggregates

app = connexion.App(__name__, specification_dir='./')
app.add_api(API_SPEC)


def generate_html_table(rows, columns):
    """
    Build an HTML table given:
      - rows:   a list of tuples, each tuple matching the columns order
      - columns: a list of column names (strings) to use as headers
    """
    html = '<table cellspacing="1" cellpadding="3" border="1"><tr>'
    for col in columns:
        html += f'<th>{col.capitalize()}</th>'
    html += '</tr>'

    for row in rows:
        html += '<tr>'
        for cell in row:
            html += f'<td>{cell}</td>'
        html += '</tr>'
    html += '</table>'
    return html

@app.route('/')
def index():
    """
    Render an HTML page showing aggregated sensor data.
    """
    # Fetch aggregated data as list of dicts
    data = read_aggregates()

    # Calculate global average across all devices
    values = [rec[AGG_FIELD] for rec in data]
    global_avg = sum(values) / len(values) if values else 0

    # Define columns and construct rows
    columns = [FIELD_DEVICE, AGG_FIELD]
    rows = [(rec[FIELD_DEVICE], rec[AGG_FIELD]) for rec in data]

    # Build HTML header
    html = (
        '<html><head><title>Fog Processor</title>'
        '<meta http-equiv="refresh" content="10" /></head><body>'
        '<h1>Aggregated Sensor Data</h1>'
    )
    # Insert generated table
    html += generate_html_table(rows, columns)
    html += '</body></html>'
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
