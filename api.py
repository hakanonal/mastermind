from flask import Flask
from flask_cors import CORS
from ai.environment import environment
from waitress import serve

app = Flask(__name__)
CORS(app)

config = {
    'discount': 0.95,
    'exploration_rate':0.9,
    'decay_factor':0.99,
    'learning_rate':0.001,
    'episode':100,
    'debug' : 0,
    'chances' : 12,
    'digits' : 4,
    'peg_count': 6,
    'mode' : 'user' # ai | user
}

import os
os.environ['WANDB_MODE'] = 'dryrun'

e = environment(config=config)

def response():
    return {
        'state' : e.state,
        'end' : e.isEnded(e.state) is not None,
        'generated_code' : e.generated_code,
        'chance' : e.chance()
    }

@app.route('/', methods=['GET'])
def get():
    return response(),200    

@app.route('/reset', methods=['GET'])
def reset():
    e.initGame()
    return response(),200    

@app.route('/play/<code>', methods=['GET'])
def play(code):
    result,message = e.validateUserInput(code)
    if(not result):
        return {'state': e.state,'message':message}, 400

    if(e.isEnded(e.state) is None):
        action_to_play = int("".join([str(i) for i in code]))
        new_state = e.play(e.chance(),action_to_play)
        e.state = new_state

    return response(),200



@app.errorhandler(404)
def not_found(_):
    return response(),404

if __name__ == "__main__":
    port = os.environ.get('PORT')
    if(port is None):
        port = 5000

    app.run(host='0.0.0.0',port=port,ssl_context='adhoc')
    #serve(app, host='0.0.0.0', port=port)