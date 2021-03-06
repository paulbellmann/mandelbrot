from mandelbrot import Mandelbrot
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.debug = True

@app.route("/", methods=['POST'])
def api():
    # gets json from the post request
    content = request.get_json()

    mandel = Mandelbrot(
            content['RealFrom'], content['RealTo'], 
            content['ImaginaryFrom'], content['ImaginaryTo'],
            content['Intervall'], content['MaxIteration'],
        )

    # safes the array
    mandel2Darray = mandel.do_the_loop()
    # turn 2D array into 1D array
    mandel1Darray = mandel2Darray.ravel().tolist()

    return jsonify(mandel1Darray)


@app.route('/client')
def client():
    return render_template('client.html')