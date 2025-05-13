from flask import Flask, request
from flask_cors import CORS
import getInput
import astar
import astar_flood
import astar_traffic
import helper
import json
app = Flask(__name__)
CORS(app)

@app.route('/calculate_flood', methods=['GET'])
def calculate_flood():
    raw_input = request.args.get('pntdata').split(',')
    mappedSourceLoc = getInput.getNearestPoint(raw_input[0], raw_input[1])
    mappedDestLoc = getInput.getNearestPoint(raw_input[2], raw_input[3])
    print("Location of the first point " + raw_input[0] + " " + raw_input[1])
    print("Location of the second point " + raw_input[2] + " " + raw_input[3])
    print("nearest of the first point " + str(mappedSourceLoc[0]) + " " + str(mappedSourceLoc[1]))
    print("nearest of the second point " + str(mappedDestLoc[0]) + " " + str(mappedDestLoc[1]))
    start = helper.getOSMId(mappedSourceLoc[0], mappedSourceLoc[1])
    print("Start Id: " + start)
    end = helper.getOSMId(mappedDestLoc[0], mappedDestLoc[1])
    print("End Id: " + end)
    pathDict, finalDistance = astar_flood.astar_flood(start, end)
    print("Shortest distance: " + str(finalDistance))
    response = helper.getResponseLeafLet(pathDict, end)
    return json.dumps(response)
@app.route('/calculate', methods=['GET'])
def calculate():
    raw_input = request.args.get('pntdata').split(',')
    mappedSourceLoc = getInput.getNearestPoint(raw_input[0], raw_input[1])
    mappedDestLoc = getInput.getNearestPoint(raw_input[2], raw_input[3])
    print("Location of the first point " + raw_input[0] + " " + raw_input[1])
    print("Location of the second point " + raw_input[2] + " " + raw_input[3])
    print("nearest of the first point " + str(mappedSourceLoc[0]) + " " + str(mappedSourceLoc[1]))
    print("nearest of the second point " + str(mappedDestLoc[0]) + " " + str(mappedDestLoc[1]))
    start = helper.getOSMId(mappedSourceLoc[0], mappedSourceLoc[1])
    print("Start Id: " + start)
    end = helper.getOSMId(mappedDestLoc[0], mappedDestLoc[1])
    print("End Id: " + end)
    pathDict, finalDistance = astar.astar(start, end)
    print("Shortest distance: " + str(finalDistance))
    response = helper.getResponseLeafLet(pathDict, end)
    return json.dumps(response)
@app.route('/calculate_traffic', methods=['GET'])
def calculate_traffic():
    raw_input = request.args.get('pntdata').split(',')
    mappedSourceLoc = getInput.getNearestPoint(raw_input[0], raw_input[1])
    mappedDestLoc = getInput.getNearestPoint(raw_input[2], raw_input[3])
    print("Location of the first point " + raw_input[0] + " " + raw_input[1])
    print("Location of the second point " + raw_input[2] + " " + raw_input[3])
    print("nearest of the first point " + str(mappedSourceLoc[0]) + " " + str(mappedSourceLoc[1]))
    print("nearest of the second point " + str(mappedDestLoc[0]) + " " + str(mappedDestLoc[1]))
    start = helper.getOSMId(mappedSourceLoc[0], mappedSourceLoc[1])
    print("Start Id: " + start)
    end = helper.getOSMId(mappedDestLoc[0], mappedDestLoc[1])
    print("End Id: " + end)
    pathDict, finalDistance = astar_traffic.astar_traffic(start, end)
    print("Shortest distance: " + str(finalDistance))
    response = helper.getResponseLeafLet(pathDict, end)
    return json.dumps(response)
if __name__ == "__main__":
    app.run(host='0.0.0.0')
