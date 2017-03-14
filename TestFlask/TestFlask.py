from flask import Flask
import json
import random

app = Flask(__name__)


@app.route('/index/<user>', methods=['GET','POST','PUT','DELETE'])


def hello_world(user):

    index = random.randint(1, 5)

    if index == 0:
        ad = 'One'
    elif index == 1:
        ad = 'Two'
    elif index == 2:
        ad = 'three'
    else: ad = 'other'


    obj = [[1, 2, 3], 123, 123.123,'random:'+ad,'abc', {'key1': user, 'key2': (4, 5, 6)}]
    encodedjson = json.dumps(obj)

    return  encodedjson


if __name__ == '__main__':
    app.run(debug=True)


