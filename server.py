from mandelbrot import Mandelbrot
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    # gets json from the post request
    content = request.get_json()

    mandel = Mandelbrot(
            content['realFrom'], content['realTo'], 
            content['imgFrom'], content['imgTo'],
            content['interval'], content['max_iter'],
        )

    # safes the array
    mandel2Darray = mandel.do_the_loop()
    # turn 2D array into 1D array
    mandel1Darray = mandel2Darray.ravel().tolist()

    return jsonify(mandel1Darray)