import sqlite3
from flask import make_response, abort

from joblib import dump, load



def read():
    
    temperatures = []
    
    conn = sqlite3.connect('temperature.db')
    
    c = conn.cursor()
    c.execute('SELECT id, devicename, temperature, timestamp FROM temperature ORDER BY id ASC')
    results = c.fetchall()
    
    for result in results:
                
        temperatures.append({'id':result[0],'devicename':result[1],'temperature':result[2],'timestamp':result[3]})
    
    conn.close()
    
    return temperatures



def create(globaltemperature):
    '''
    This function creates a new temperature record in the database
    based on the passed in temperature data
    :param globaltemperature:  Global temperature record to create in the database
    :return:        200 on success
    '''
    devicename = globaltemperature.get('devicename', None)
    temperature = globaltemperature.get('temperature', None)
    timestamp = globaltemperature.get('timestamp', None)
    
    conn = sqlite3.connect('temperature.db')
    
    c = conn.cursor()    
    sql = "INSERT INTO temperature (devicename, temperature, timestamp) VALUES('" + devicename + "', " + str(temperature) + ", '" + timestamp + "')"
    print(sql)
    c.execute(sql)
    conn.commit()
    conn.close()
    
    return make_response('Global temperature record successfully created', 200)



def cluster(light):
    
    try:
        
        # predict new temperature and humidity observation
        kmeans = load('lightcluster.joblib')
        
        # temperature, humidity
        newX = [[light]]
        result = kmeans.predict(newX)
        
        print('Cluster Light: light={}; cluster={}'.format(light, result[0]))

        return str(result[0])
        
    except Exception as error:

        print('Error: {}'.format(error.args[0]))

        return 'Unknown'
