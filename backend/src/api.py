from logging import log
import os
import pickle
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import numpy as np

from loguru import logger

app = Flask(__name__)
CORS(app)

model_path = r"../models/model.pkl"

random_list = ["Apple", "Banana", "Pear"]

if os.path.isfile(model_path):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
else:
  raise FileNotFoundError



from flask import Flask, request,jsonify,json
@app.route("/image", methods=["POST","GET"])
def submitData():
    response_object = {'status':'success'}

    print(request)

    if request.method == "POST":
        post_data = request.get_json()
        
        print(">"*50)
        print((post_data["up_img"]))


        import urllib
        link = post_data["up_img"][5:]     
        print(link)
        
        f = urllib.request.urlopen(link)

        my_file = f.read()



        # X = (
        #   np.array(
        #     [
        #       post_data["sepal_length"],
        #       post_data["sepal_width"],
        #       post_data["petal_length"],
        #       post_data["petal_width"]
        #     ]
        #   ).astype(np.float64).reshape(1, -1)
        # )
    

        # print(X[0])
        
        # prediction = model.predict(X)

        # print(type(prediction))

        # print(prediction[0])

        # label = random_list[prediction[0]]


        # print(label)

        response_object['message'] ='Data added!'
        return jsonify(response_object)
        # return {"class": label}



if __name__ == "__main__":
  app.run(debug=True)