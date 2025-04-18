import connexion
import sqlite3



app = connexion.App(__name__, specification_dir='./')
app.add_api('cloud.yml')



@app.route('/')
def index():

	conn = sqlite3.connect('temperature.db')
	
	c = conn.cursor()
	c.execute('SELECT id, devicename, temperature, timestamp FROM temperature ORDER BY id DESC')
	results = c.fetchall()
	
	html = '<html><head><title>Cloud Server</title><meta http-equiv="refresh" content="5" /></head><body><h1>Global temperatures</h1><table cellspacing="1" cellpadding="3" border="1"><tr><th>ID</th><th>Device Name</th><th>temperature</th><th>Timestamp</th></tr>'
	for result in results:
				
		html += '<tr><td>' + str(result[0]) + '</td><td>' + str(result[1]) + '</td><td>' + str(result[2]) + '</td><td>' + str(result[3]) + '</td></tr>'
	
	html += '</body></html>'
	
	conn.close()
	
	return html

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
