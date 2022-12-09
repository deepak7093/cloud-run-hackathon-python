
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
from flask import Flask, request
import json

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']
hit_moves = ['F', 'L', 'F']


@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"


@app.route("/", methods=['POST'])
def move():
    request.get_data()
    logger.info(request.json)
    data = request.json

    # TODO add your implementation here to replace the random response

    mybot = data['_links']['self']['href']
    botState = {}
    otherBotStates = []
    for player in data['arena']['state'].keys():
        if player == mybot:
            botState = data['arena']['state'][player]
            if botState['wasHit']:
                print("here")
                logger.info(botState['wasHit'])
                if int(botState['x']) < int(data['arena']['dims'][0]) and int(botState['y']) < int(data['arena']['dims'][1]):
                    return random.choice(hit_moves)
                # check hit direction
                # return "HERE"
                return random.choice(hit_moves)
        else:
            otherBotStates.append(data['arena']['state'][player])

    # for player in data['arena']['state'].keys():

    #     # if int(botState['x']) < int(data['arena']['dims'][0]) or int(botState['y']) < int(data['arena']['dims'][1]):
    #     #     return random.choice(hit_moves)
    #     # elif int(botState['x']) == int(data['arena']['dims'][0]) or int(botState['y']) == int(data['arena']['dims'][1]) and botState['direction'] == "N":
    #     #     return  moves[random.randrange(len(moves))]
    #     # elif int(botState['x']) == int(data['arena']['dims'][0]) or int(botState['y']) == int(data['arena']['dims'][1]) and botState['direction'] == "S":
    #     #     return  moves[random.randrange(len(moves))]
    #     # elif int(botState['x']) == int(data['arena']['dims'][0]) or int(botState['y']) == int(data['arena']['dims'][1]) and botState['direction'] == "E":
    #     #     return  moves[random.randrange(len(moves))]
    #     # elif int(botState['x']) == int(data['arena']['dims'][0]) or int(botState['y']) == int(data['arena']['dims'][1]) and botState['direction'] == "W":
    #     #     return  moves[random.randrange(len(moves))]
    #     # TODO : check surrondings

    #     # logger.info(json.dump(data['arena']['state'][player]))

    for item in otherBotStates:
        if botState['direction'] == "E" and int(item['x']) == int(botState['x']) and int(item['y']) > int(botState['y']):
            return moves[1]
        if botState['direction'] == "W" and int(item['x']) == int(botState['x']) and int(item['y']) < int(botState['y']):
            return moves[1]
        if botState['direction'] == "N" and int(item['y']) == int(botState['y']) and int(item['x']) < int(botState['x']):
            return moves[1]
        if botState['direction'] == "S" and int(item['y']) == int(botState['y']) and int(item['x']) > int(botState['x']):
            return moves[1]
        # TODO:  check for nearby bot
        # if item['x'] == int(botState['x'] + 1) and botState['direction'] == "E":
        #     return
        #     return moves['F', 'T']
        # if item['x'] == int(botState['x'] + 1) and botState['direction'] == "W":
        #     return moves['R', 'R', 'F', 'T']
        # if item['x'] == int(botState['x'] + 1) and botState['direction'] == "N":
        #     return moves['R', 'F', 'T']
        # if item['x'] == int(botState['x'] + 1) and botState['direction'] == "S":
        #     return moves['L', 'F', 'T']

    return moves[1]


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
