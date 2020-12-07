from agent import agent
import wandb
import random
import numpy as np

class environment:

    def __init__(self, config=None):

        if(config is None):
            wandb.init(project="mastermind")
            self.config = wandb.config
        else:
            wandb.init(project="mastermind",config=config)
            self.config = config
        self.agent7 = agent(
            discount=self.config['discount'],
            exploration_rate=self.config['exploration_rate'],
            decay_factor=self.config['decay_factor'],
            learning_rate=self.config['learning_rate'],
            )
        self.config['peg_space'] = list(range(1,self.config['peg_count']+1))
        self.initGame()
        self.metrics = {
            'tot_win' : 0,
            'tot_reward' : 0,
            'exploration_rate' : self.agent7.exploration_rate,
        }

    def initGame(self):
        self.state = np.zeros((self.config['chances'],3))
        self.generated_code = self.generateCode()
        if(self.config['debug']):
            print("Generated Code: %s"%self.generated_code)
        self.actions_played = []
    
    def generateCode(self):
        generated_code = []
        for _ in range(1,self.config['digits']+1):
            generated_code.append(random.choice(self.config['peg_space']))
        return ''.join(str(generated_code))

    def _validateUserInput(self,guessed_code):
        if(len(guessed_code) != self.config['digits']):
            print("Invalid digit count")
            return False
        for peg in guessed_code:
            if(peg not in self.config['peg_space']):
                print("Invalid Code! Avaible optipons %s"%self.config['peg_space'])
                return False
        return True
    
    def askActionToPlay(self):
        while True:
            guessed_code = input("Guess (%s digits): " % self.config['digits'])
            guessed_code = list(guessed_code)
            if(self._validateUserInput(guessed_code)):
                break
        return ''.join(str(guessed_code))
        

    def start(self):
        for episode in range(1,self.config['episode']+1):
            self.initGame()
            #game phase
            for chance in range(1,self.config['chances']+1):
                
                if(self.config['mode'] == 'user'):
                    action_to_play = self.askActionToPlay()
                else:
                    action_to_play = self.agent7.get_next_action(self.state)

                new_state = self.play(chance,action_to_play)

                self.debug1(episode,self.state,new_state,action_to_play)
                self.actions_played.append((self.state,new_state,action_to_play))
                self.state = new_state
                if(self.config['mode'] == 'user'):
                    self.printState(self.state)
                reward = self.isEnded(self.state)
                if reward is not None:
                    break


            #q-tatble update backpropogation phase
            if reward > 0:
                self.metrics['tot_win'] += 1
                self.metrics['avg_win'] = self.metrics['tot_win'] / episode
                self.metrics['tot_reward'] += reward
                self.metrics['avg_reward'] = self.metrics['tot_reward'] / episode
            if(self.config['mode'] == 'ai'):
                self.agent7.update(self.actions_played,reward)

            self.metrics['exploration_rate'] = self.agent7.exploration_rate
            wandb.log(self.metrics,step=episode)


    def play(self,chance,action_to_play):
        new_state = self.state.copy()
        red,white = self.provideFeedback(self.generated_code,action_to_play)
        new_state[chance-1] = (red,white,action_to_play)
        return new_state

    def provideFeedback(self, guessToCopy, codeToCopy):
        red = 0
        white = 0
        code = list(codeToCopy)
        guess = list(guessToCopy)
        for i in range(0, self.config['digits']):
            if guess[i] == code[i]:
                code[i] = '-'
                guess[i] = ''
                red =+ 1
        for i in range(0, self.config['digits']):
            if guess[i] in code:
                code[code.index(guess[i])] = '-'
                guess[i] = ''
                white =+ 1
        return red,white
            
    def printState(self,state):
        for i in range(self.config['chances']):
            print("| %s | %s+%s",(state[i,2],state[i,0],state[i,1]))

    def isEnded(self,state):
        for i in range(self.config['chances']):
            if(state[i,0] == self.config['digit']):
                return self.config['chances']-i
            if(state[i,2] == 0):
                break
        if(i+1==self.config['chances']):
            return -10
        return None
        
    def save(self):
        self.agent7.save()

    
    def debug1(self,episode,old_state,new_state,action):
        if(self.config['debug']):
            print("%d = %s -> %s -> %s"%(episode,old_state,action,new_state))
            input("continue?")
