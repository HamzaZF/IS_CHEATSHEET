# Cloud service configuration

# SQLite database settings
DB_NAME        = 'light.db'      # e.g. 'sensor.db' or 'light.db'
TABLE_NAME     = 'light'         # name of the table storing readings
FIELD_DEVICE   = 'devicename'
FIELD_SENSOR   = 'light'         # e.g. 'light', 'temperature', etc.
FIELD_TIMESTAMP= 'timestamp'
FIELD_TOCLOUD  = 'tocloud'

# REST API base path (Connexion will read cloud.yml)
API_SPEC       = 'cloud.yml'
API_BASE_PATH  = '/api'

# Clustering model path
CLUSTER_MODEL  = 'lightcluster.joblib'  # filename of pre-trained model
