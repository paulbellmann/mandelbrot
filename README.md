## Mandelbrot Set

![screenshot](./screenshot.png)

---

This is a simple Mandelbrot Python backend. It can calculate any given area and returns its values
in an array.

### How to run the development server on your system: 

1. `$ pip install -r requirements.txt`
2. `$ export FLASK_APP=src/server.py`
3. `$ flask run`

### How to test the server:

```
$ curl --header "Content-Type: application/json" \
       --request POST \
       --data '{"realFrom":-2, "realTo":1, "imgFrom": -1, "imgTo":1, "interval": 0.01, "max_iter": 100}' \
       http://localhost:5000
```

### How to test the Mandelbrot Class:

1. `$ python src/test_plot.py`
2. watch the plot
3. change constructor params in `test_plot.py`
4. repeat steps 1+2