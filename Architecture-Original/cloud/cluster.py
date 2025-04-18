import json as json

from flask import jsonify


def analyze(brightness):
    ret = int(brightness)%2
    #json

    # json = json.dumps(ret)

    #ret = json.dumps({"result": ret})
    
    return jsonify(result=ret)