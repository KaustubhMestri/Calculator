from flask import Flask, request

app = Flask("Demo Website")

@app.route("/")
def hello_world():
    return "<h1>Hello World</h1>"

@app.route("/about")
def about():
    return "This is About Page"

@app.route("/test")
def test():
    return 'test test test'

@app.route("/test2")
def test2():
    data = request.args.get('x')
    return "this is user input {}".format(data)
if __name__=="__main__":
    app.run(host = '0.0.0.0')