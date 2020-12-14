from ai.environment import environment


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
    'mode' : 'ai' # ai | user
}

import os
os.environ['WANDB_MODE'] = 'dryrun'

e = environment(config=config)

e.start()
e.save() 
