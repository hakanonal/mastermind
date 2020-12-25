from .agentWC import agentWC
import wandb
import random
from IPython.display import clear_output

class environment:

    def __init__(self, config=None):

        if(config is None):
            wandb.init(project="mastermind")
            self.config = wandb.config
        else:
            wandb.init(project="mastermind",config=config)
            self.config = config
        self.agent7 = agentWC(self.config,self)
        self.config['peg_space'] = list(range(1,self.config['peg_count']+1))
        self.initGame()
        self.metrics = {
            'tot_win' : 0,
            'tot_loose' : 0,
            'tot_reward' : 0,
            'exploration_rate' : self.agent7.exploration_rate,
        }

    def initGame(self):
        self.state = [[0 for i in range(3)] for j in range(self.config['chances'])] #np.zeros((self.config['chances'],3))
        self.hidden_code = self.generateRandomCode()
        self.actions_played = []
        self.agent7.initGame()
    
    def generateRandomCode(self):
        generated_code = []
        for _ in range(1,self.config['digits']+1):
            generated_code.append(random.choice(self.config['peg_space']))
        return int("".join([str(i) for i in generated_code]))

    def validateUserInput(self,guessed_code):
        if(not guessed_code.isnumeric()):
            return False, "Only integers alllowed"
        guessed_code = [int(d) for d in list(guessed_code)]
        if(len(guessed_code) != self.config['digits']):
            return False, "Invalid digit count"
        for peg in guessed_code:
            if(peg not in self.config['peg_space']):
                return False, "Invalid Code! Avaible optipons %s"%self.config['peg_space']
        return True, ""
    
    def askActionToPlay(self):
        while True:
            guessed_code = input("Guess (%s digits): " % self.config['digits'])
            result,message = self.validateUserInput(guessed_code)
            if(not result): print(message) 
            else: break
        return int("".join([str(i) for i in guessed_code]))
        

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
            else:
                self.metrics['tot_loose'] += 1
                self.metrics['avg_loose'] = self.metrics['tot_loose'] / episode
            self.metrics['tot_reward'] += reward
            self.metrics['avg_reward'] = self.metrics['tot_reward'] / episode
            if(self.config['mode'] == 'ai'):
                self.agent7.update(self.actions_played,reward)
            if(self.config['mode'] == 'user'):                
                self.printState(self.state)
                print(self.metrics)
                print("Generated code was: %0*d"%(self.config['digits'],self.hidden_code))

            self.metrics['exploration_rate'] = self.agent7.exploration_rate
            wandb.log(self.metrics,step=episode)


    def play(self,chance,action_to_play):
        new_state = self.state.copy()
        red,white = self.provideFeedback(self.hidden_code,action_to_play)
        new_state[chance-1] = (red,white,action_to_play)
        return new_state

    def provideFeedback(self, guessToCopy, codeToCopy):
        red = 0
        white = 0
        code = [int(i) for i in str(codeToCopy)]
        guess = [int(i) for i in str(guessToCopy)]
        for i in range(0, self.config['digits']):
            if guess[i] == code[i]:
                code[i] = '-'
                guess[i] = ''
                red = red + 1
        for i in range(0, self.config['digits']):
            if guess[i] in code:
                code[code.index(guess[i])] = '-'
                guess[i] = ''
                white = white + 1
        return red,white
            
    def printState(self,state):
        clear_output(wait=True)
        for i in range(self.config['chances']):
            print("| %d+%d | %0*d |"%(state[i][0],state[i][1],self.config['digits'],state[i][2]))
        if(self.config['debug']):
            print("| --- | %0*d"%(self.config['digits'],self.hidden_code))

    def isEnded(self,state):
        for i in range(self.config['chances']):
            if(state[i][0] == self.config['digits']):
                return self.config['chances']-i
            if(state[i][2] == 0):
                return None
        return -10

    def chance(self,state=None):
        state_to_check = state if state is not None else self.state
        for i in range(self.config['chances']):
            if(state_to_check[i][2] == 0):
                return i+1
        return i+1


    def save(self):
        self.agent7.save()

    
    def debug1(self,episode,old_state,new_state,action):
        if(self.config['debug'] and self.config['mode'] == 'ai'):
            print("%d = %s -> %s -> %s"%(episode,old_state,action,new_state))
            input("continue?")
