import numpy as np
import random
import pickle
import wandb

class agent:

    def __init__(self,config):
        self.discount = config['discount']
        self.exploration_rate = config['exploration_rate']
        self.exploration_rate_constant = config['exploration_rate']
        self.decay_factor = config['decay_factor']
        self.learning_rate = config['learning_rate']
        self.config = config
        self.q_table = {}
        self.action_space_count = int("".join([str(self.config['peg_count']) for i in range(self.config['digits'])]))+1
        self.min_action = int("".join([str(1) for i in range(self.config['digits'])]))
        

    def get_next_action(self, state):
        if random.random() < self.exploration_rate: # Explore (gamble) or exploit (greedy)
            return self.random_action()
        else:
            return self.greedy_action(state)

    def greedy_action(self, state):
        return np.argmax(self.getQ(state))
    
    def random_action(self):
        generated_code = []
        for _ in range(1,self.config['digits']+1):
            generated_code.append(random.choice(self.config['peg_space']))
        return int("".join([str(i) for i in generated_code]))

    def getQ(self,state):
        state_hash = str(state)
        if state_hash not in self.q_table:
            self.q_table[state_hash] = np.zeros(self.action_space_count,dtype=int)
            for i in range(self.min_action):
                self.q_table[state_hash][i] = -999999
        return self.q_table[state_hash]

    def train(self, old_state, new_state, action, reward):
        
        old_state_prediction = self.getQ(old_state)[action]
        new_state_prediction = self.getQ(new_state)

        old_state_prediction = ((1-self.learning_rate) * old_state_prediction) + (self.learning_rate * (reward + self.discount * np.amax(new_state_prediction)))

        self.getQ(old_state)[action] = old_state_prediction
        return old_state_prediction

    def update(self, actions_played, reward):
        for old_state,new_state,action in reversed(actions_played):
            new_reward = self.train(old_state, new_state, action, reward)
            reward = new_reward
        self.exploration_rate *= self.decay_factor
        if self.exploration_rate < 0.01:
            self.exploration_rate = self.exploration_rate_constant

    def save(self, file="policy"):
        filename = "%s_%d_%d"%(file,self.config['digits'],self.config['peg_count'])
        fw = open(filename, 'wb')
        pickle.dump(self.q_table, fw)
        fw.close()
        wandb.save(file)

    def load(self, file="policy"):
        filename = "%s_%d_%d"%(file,self.config['digits'],self.config['peg_count'])
        fr = open(filename, 'rb')
        self.q_table = pickle.load(fr)
        fr.close()  
