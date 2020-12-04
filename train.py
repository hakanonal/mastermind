from environment import environment
import wandb

def train():
    e = environment()
    e.start()
    e.save() 


wandb.agent('hakanonal/mastermind/xxx',function=train)
