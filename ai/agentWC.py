import numpy as np
import random
import pickle
import wandb

class agentWC:

    def __init__(self,config,env):
        self.config = config
        self.exploration_rate = self.config['exploration_rate']
        self.peg_set = set([str(i) for i in range(1,self.config['peg_count']+1)])
        self.all_digits_set = set([str(i) for i in range(10)])
        self.invalid_digit_set = self.all_digits_set-self.peg_set
        self.minimum_code = int("".join([str(1) for i in range(self.config['digits'])]))
        self.maximum_code = int("".join([str(len(self.peg_set)) for i in range(self.config['digits'])]))
        
        self._initSet()

        wandb.config.update({'model_name':'worst_case'})

    def _initSet(self):
        self.action_space = set(range(self.minimum_code,self.maximum_code+1))
        invalid_digit_included_codes = []
        for v in self.action_space:
            vs = str(v)
            for invalid_digit in self.invalid_digit_set:
                if(invalid_digit in vs):
                    invalid_digit_included_codes.append(v)
        self.action_space = list(self.action_space - set(invalid_digit_included_codes))

    def initGame(self):
        self._initSet()

    def get_next_action(self, state):
        return self.greedy_action(state)

    def greedy_action(self, state):
        return self.action_space[0]
    
    def getQ(self,state):
        return True

    def train(self, old_state, new_state, action, reward):
        return True

    def update(self, actions_played, reward):
        return True

    def save(self, file="policy"):
        return True

    def load(self, file="policy"):
        return True
