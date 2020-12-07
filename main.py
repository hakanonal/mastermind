from environment import environment
import os

config = {
    'discount': 0.95,
    'exploration_rate':1,
    'decay_factor':1,
    'learning_rate':0.01,
    'episode':1000,
    'debug' : 0,
    'chances' : 12,
    'digits' : 4,
    'peg_count': 6,
    'mode' : 'ai' # ai | user
}
os.environ['WANDB_MODE'] = 'dryrun'

e = environment(config=config)

e.start()
e.save() 
