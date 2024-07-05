# from flask_ngrok import run_with_ngrok
from flask import Flask
from flask import Flask, app, request

from flask_cors import CORS
import requests

app = Flask(__name__)
cors = CORS(app)
@app.route('/revenue', methods=['GET','POST'])
def a():
    # img = request.values.get('uri')
    # print(img)
    img = request.json['uri']
    # x = [str(i) for i in img]
    # img = ','.join(x)
    # print(img, type(img))
    r = requests.post("http://2bb7-34-125-176-65.ngrok-free.app/revenue", data={'uri':img})
    return r.json()
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)