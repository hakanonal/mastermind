# AI that learns how to play the game Mastermind

This project idea has brought to my attention by my cousin [Onur](https://www.linkedin.com/in/onur-eren-449a9913/). So here we are. 

## How To Play

Check the notebook [play](play.ipynb)

## Journal

#### 04.12.2020

- I have read the game rules from [here](https://en.wikipedia.org/wiki/Mastermind_(board_game))
- Checked some python already made implementaions like [this](https://www.askpython.com/python/examples/create-mastermind-game-in-python) and [this](https://bnbasilio.medium.com/mastermind-a-how-to-in-python-7b80ca9809ab)
- Created a this github repository. 
- Copied my agent/environment code template from my other projects.
- Prepeared the template to start coding accordinglly for the game.
- Well! I have went though my template. I need to figure out:
    - the q-table struture (I may decide to use a neural net. I do not know how to choose right now)
    - code the game rules
    - figure out metrics.
    - print the board
    - add user input functionallty.
- So curentlly the code is not working. Work is in progess...
- [This](https://bnbasilio.medium.com/mastermind-a-how-to-in-python-7b80ca9809ab) article has a good algorithm to find the feedback array check provideFeedback method in the article.

#### 06.12.2020

- Let's continue with the previous list. I want to create the game without ai right now. So I need
    - code the game rules
    - figure out metrics.
    - print the board
- While coding I find a way to host the game for pıblic. I will use [this](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb) method. I'll check that later.
- Could not work on this properlly...

#### 07.12.2020

- Will continue now...
- the environment class is almost finished. Curentlly in the status of debugging...
- So the playable version of the game has completed. A user can play right now.
- I will try to publish via colab.
    - That did not work. Because the references to the environment and agent classes are not working properlly in colab.
- So the game has completed. Now it is time to construct the agent class. Curentllt the games ai mode is not working properlly. At least iit is not tested well.
- Agent:
    - I have bumped into unhashable type: 'list' error. since the state in in list format and it is not hashable. 
        - I will try [this](https://stackoverflow.com/questions/7027199/hashing-arrays-in-python) blog to fix. Done...
    - So the action space quite high. it is the digits^peg_count. For the default values it is 4^6=4096. However I can still try to keep a q-table. We'll see the size of it after some iterations.
        - I need to think through the action space. The above sentences seems to be incorrect. Let's assume though default parameters. 4 digits and 6 pegs. So I need to 4 different digits that each digit can be between 1 and 6. So the highest number is 6666. So my q-table's each state action space array should be in the size of 6666 fır this case. I bealive there is better way to store this I will not consider to find a better way now. I wll come back this issue if there is memory or ant other size problems.
        - Ok I have moving pretty fast I am almost there. Now time to time agent guesses 0 because there is 0 in the q_table. So the greedy method alson considers the actions that is below 1111. Now what? 
            - In thory if I explore all the time I will not bump this error. and it is working. So the greedy method has to be fixed


    
    
        
