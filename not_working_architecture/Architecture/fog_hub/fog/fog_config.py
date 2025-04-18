# Fog configuration constants
DB_NAME         = '../temperature.db'   # e.g. 'sensor.db' or 'temperature.db'
TABLE_NAME      = 'temperature'      # e.g. 'sensor', 'temperature'
FIELD_DEVICE    = 'devicename'       # device identifier column
FIELD_SENSOR    = 'temp'             # sensor value column
FIELD_TIMESTAMP = 'timestamp'        # timestamp column

# Aggregation settings
AGG_FUNCTION    = 'AVG'               # aggregation SQL function, e.g. AVG, MAX, MIN
AGG_FIELD       = 'averagetemp'      # alias for aggregated value

# API spec filename for Connexion\API
API_SPEC        = 'fog.yml'
API_BASE_PATH   = '/api'
