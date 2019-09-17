import argparse
import sys

from flask import Flask, render_template, request

parser = argparse.ArgumentParser(description='Script to generate website based on bus data')
parser.add_argument('-p','--postcode', help='Valid UK postcode', required=True)
args = parser.parse_args()
postcode=args.postcode
print("In web script")
print(postcode)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/busInfo")
def busInfo():
    #postcode = request.args.get('postcode')
    return render_template('info.html', postcode=postcode)

if __name__ == "__main__": app.run()