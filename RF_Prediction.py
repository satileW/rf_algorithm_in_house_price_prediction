import sys
from flask import Flask, jsonify, json, request

from pyspark import SparkConf, SparkContext
'''Random Forest'''
from pyspark.mllib.tree import RandomForestModel
from pyspark.mllib.util import MLUtils

app = Flask(__name__)
APP_NAME = "good_apt"
def prediction(parameter_list):
    #function
    sameModel = RandomForestModel.load(sc, filename)#"path/myrfModel"
    print "read model success"
    prediction = sameModel.predict(parameter_list)
    #example
    #[60.0,37.307741,-121.89593,17108.0,0.0,8400.0,0.0,1938.0,1320.0,6.0,2.0,1.0,95125.0,713.0,753543.2])
    return prediction

@app.route("/spark_rf", methods = ["POST"])
def rest_prediction():
    req_post = json.loads(request.data)
    parameter_list = []
    parameter_list.append(req_post['_c0'])
    parameter_list.append(req_post['Lat'])
    parameter_list.append(req_post['Lng'])
    parameter_list.append(req_post['Tax rate area'])
    parameter_list.append(req_post['Neighborhood'])
    parameter_list.append(req_post['Lot sq. ft.'])
    parameter_list.append(req_post['Property class'])
    parameter_list.append(req_post['Year built'])
    parameter_list.append(req_post['Square feet'])
    parameter_list.append(req_post['Rooms'])
    parameter_list.append(req_post['Bedrooms'])
    parameter_list.append(req_post['Bathrooms'])
    parameter_list.append(req_post['ZIP code'])
    parameter_list.append(req_post['Median Price(2017)'])
    parameter_list.append(req_post['Median $ per Sq. Ft.(2017)'])
    # parameter_list.append(req_post['Value at Median $ per Sq. Ft.(2017)'])
    
    resp = dict()
    resp['prediction'] = prediction(parameter_list)
    return jsonify(resp), 200


if __name__ == '__main__':
    conf = SparkConf().setAppName(APP_NAME)
    conf = conf.setMaster("local[*]")
    global sc 
    sc = SparkContext(conf=conf)
    filename = sys.argv[1]#this is model path
    app.run(host='0.0.0.0', port=6666)

    