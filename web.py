import os
import sys

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/busInfo")
def busInfo():
    postcode = request.args.get('postcode')
    postcode = postcode.replace(" ", "")
    os.system("python main.py -p " + str(postcode))
    infile = postcode + ".txt"
    with open(infile, 'r') as bus_times:
        contents = bus_times.readlines()
    bus_times.close()
    indices = [i for i, item in enumerate(contents) if '*' in item]
    print(contents)
    print(indices)
    return render_template('info.html', postcode=postcode, data=contents)

if __name__ == "__main__": app.run()