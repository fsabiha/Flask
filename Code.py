from flask import Flask

app = Flask(__name__) # name of the application
print(__name__) 

@app.route("/") # where we find the end point
def hello_world():
    return "<p>Hello, World!</p>"