import numpy as np
import random
from os import path
import wandb
from keras.models import Sequential,load_model
from keras.layers import Dense, Flatten, Conv1D, Reshape

class agentNN:

    def __init__(self,config):
        self.discount = config['discount']
        self.exploration_rate = config['exploration_rate']
        self.exploration_rate_constant = config['exploration_rate']
        self.decay_factor = config['decay_factor']
        self.learning_rate = config['learning_rate']
        self.config = config
        
        wandb.config.update({'model_name':self._getModelFilename()})
        if(path.exists(self._getModelFilename())):
            self.model = load_model(self._getModelFilename())
        else:
            self.model = Sequential()
            self.model.add(Conv1D(3, (2), padding='same', input_shape = (self.config['chances'], 3), activation = 'relu'))
            self.model.add(Flatten())
            self.model.add(Dense(24,activation="relu"))
            self.model.add(Reshape((self.config['digits'],self.config['peg_count'])))
            self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def _getModelFilename(self, file="policy"):
        return "%s_%d_%d_%d.h5"%(file,self.config['digits'],self.config['chances'],self.config['peg_count'])

    def save(self, file="policy"):
        self.model.save(self._getModelFilename(file))
        wandb.save(self._getModelFilename(file))

    def get_next_action(self, state):
        if random.random() < self.exploration_rate: # Explore (gamble) or exploit (greedy)
            return self.random_action()
        else:
            return self.greedy_action(state)

    def greedy_action(self, state):
        prediction = self.getQ(state)
        generated_code = [0 for i in range(self.config['digits'])]
        for d in range(self.config['digits']):
             generated_code[d] = np.argmax(prediction[0,d])+1
        return int("".join([str(i) for i in generated_code]))
    
    def random_action(self):
        generated_code = []
        for _ in range(1,self.config['digits']+1):
            generated_code.append(random.choice(self.config['peg_space']))
        return int("".join([str(i) for i in generated_code]))

    def getQ(self,state):
        state_to_predict = np.expand_dims(state,0)
        prediction = self.model.predict(state_to_predict)
        return prediction


    def train(self, old_state, new_state, action, reward):
        
        action_as_list = [int(i) for i in str(action)]
        new_reward = reward.copy()
        
        old_state_prediction = self.getQ(old_state)
        new_state_prediction = self.getQ(new_state)

        for (i,v) in enumerate(action_as_list):
            new_reward[i] = old_state_prediction[0,i,v-1] = ((1-self.learning_rate) * old_state_prediction[0,i,v-1]) + (self.learning_rate * (reward[i] + self.discount * np.amax(new_state_prediction[0][i])))

        x = np.expand_dims(old_state,0)
        self.model.fit(x,old_state_prediction,verbose=0)

        return new_reward

    def update(self, actions_played, reward):
        reward_as_list = [reward for i in range(self.config['digits'])]
        for old_state,new_state,action in reversed(actions_played):
            new_reward = self.train(old_state, new_state, action, reward_as_list)
            reward_as_list = new_reward
        self.exploration_rate *= self.decay_factor
        if self.exploration_rate < 0.01:
            self.exploration_rate = self.exploration_rate_constant
