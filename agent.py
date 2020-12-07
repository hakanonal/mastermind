import numpy as np
import random
import pickle
import wandb

class agent:

    def __init__(self,discount,exploration_rate,decay_factor, learning_rate):
        self.discount = discount 
        self.exploration_rate = exploration_rate
        self.exploration_rate_constant = exploration_rate
        self.decay_factor = decay_factor
        self.learning_rate = learning_rate
        self.q_table = {}
        

    def get_next_action(self, state):
        if random.random() < self.exploration_rate: # Explore (gamble) or exploit (greedy)
            return self.random_action(state)
        else:
            return self.greedy_action(state)

    #!!!! these action are wrong they need to give valid actions. It should be between 0 and 8 and also the action position has to be empty on the state.
    def actionSpaceOfState(self,state):
        return [pos for pos, char in enumerate(state) if char == " "]
    def greedy_action(self, state):
        action_space = self.actionSpaceOfState(state)
        filtered_q_table = []
        q_table_state = self.getQ(state)
        for i in range(9):
            if i in action_space:
                filtered_q_table.append(q_table_state[i])
            else:
                filtered_q_table.append(-999999999999)
        return np.argmax(filtered_q_table)
    def random_action(self,state):
        return random.choice(self.actionSpaceOfState(state))
    #!!!!!!!

    def getQ(self,state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(9)
        return self.q_table[state]

    def train(self, old_state, new_state, action, reward):
        
        old_state_prediction = self.getQ(old_state)[action]
        new_state_prediction = self.getQ(new_state)

        old_state_prediction = ((1-self.learning_rate) * old_state_prediction) + (self.learning_rate * (reward + self.discount * np.amax(new_state_prediction)))

        self.q_table[old_state][action] = old_state_prediction
        return old_state_prediction

    def update(self, actions_played, reward):
        for old_state,new_state,action in reversed(actions_played):
            new_reward = self.train(old_state, new_state, action, reward)
            reward = new_reward
        self.exploration_rate *= self.decay_factor
        if self.exploration_rate < 0.01:
            self.exploration_rate = self.exploration_rate_constant

    def save(self, file="policy"):
        fw = open(file, 'wb')
        pickle.dump(self.q_table, fw)
        fw.close()
        wandb.save(file)

    def load(self, file="policy"):
        fr = open(file, 'rb')
        self.q_table = pickle.load(fr)
        fr.close()  
