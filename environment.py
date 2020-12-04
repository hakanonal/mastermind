from agent import agent
import wandb

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
        self.initGame()
        self.metrics = {
            'tot_win' : 0,
            'exploration_rate' : self.agent7.exploration_rate,
        }

    def initGame(self):
        self.state = "         "         
        self.actions_played = []
        self.turn = 1

    def start(self):
        for episode in range(1,self.config['episode']+1):
            self.initGame()
            #game phase
            while True:
                
                action_to_play = self.agent7.get_next_action(self.state)
                new_state = self.agent7.play(self.state,action_to_play)

                self.debug1(episode,self.state,new_state,action_to_play)
                self.actions_played.append((self.state,new_state,action_to_play))
                self.state = new_state
                self.printState(self.state)
                self.turn *= -1
                winner = self.findWinner()
                if winner is not None:
                    break


            #q-tatble update backpropogation phase
            if winner == 1:
                self.metrics['X_tot_win'] += 1
                self.metrics['X_avg_win'] = self.metrics['X_tot_win'] / episode
                self.agent7.update(self.actions_played,1)
            if winner == 0:
                self.metrics['tot_draw'] += 1
                self.metrics['avg_draw'] = self.metrics['tot_draw'] / episode
                self.agent7.update(self.actions_played,0)
            if winner == -1:
                self.metrics['O_tot_win'] += 1
                self.metrics['O_avg_win'] = self.metrics['O_tot_win'] / episode
                self.agent7.update(self.actions_played,-1)

            self.metrics['exploration_rate'] = self.agent7.exploration_rate
            wandb.log(self.metrics,step=episode)

                
    def findWinner(self):
        # Win-X=1 | tie=0 | Win-O=-1 | game not ended=null
        if self.agentX.didIWin(self.state):
            return 1
        if self.agentO.didIWin(self.state):
            return -1
        if self.state.find(" ") == -1:
            return 0
        return None
        
    def save(self):
        self.agent7.save()

    
    def debug1(self,episode,old_state,new_state,action):
        if(self.config['debug']):
            print("%d = %s -> %s -> %s"%(episode,old_state,action,new_state))
            input("continue?")

    def printState(self,state):
        if(self.config['print_state']):
            print("%s|%s|%s"%(state[0],state[1],state[2]))
            print("-----")
            print("%s|%s|%s"%(state[3],state[4],state[5]))
            print("-----")
            print("%s|%s|%s"%(state[6],state[7],state[8]))
            input("continue?")
