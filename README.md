# AI that learns how to play the game Mastermind

This project idea has brought to my attention by my cousin [Onur](https://www.linkedin.com/in/onur-eren-449a9913/). So here we are. 

## Some related links

- [Game Rules](https://en.wikipedia.org/wiki/Mastermind_(board_game))
- [Project Board](https://github.com/hakanonal/mastermind/projects/1) !! Project is not finished yet. Check the progress from the board.
- [Wandb dashboard](https://wandb.ai/hakanonal/mastermind) !! You can watch the AI training progress from this dashboard.
- [Graphical UI Game](https://hakanonal.github.io/mastermind-ui/dist) !! To play on nice UI.
- [Console Game](https://colab.research.google.com/github/hakanonal/mastermind/blob/main/play.ipynb) !! To play the game via hosted colab console
- [My Journal](docs/journal.md) !! I write my trials, errors and achivements in this journal.
- [UI Repo](https://github.com/hakanonal/mastermind-ui) !! User Interface repo for this project !!

## How to play

### First Option

Click [here](https://hakanonal.github.io/mastermind-ui/dist) to play via Graphical UI Vue App.

### Second Option

Click the [notebook](https://colab.research.google.com/github/hakanonal/mastermind/blob/main/play.ipynb) that is being hosted in colab and follow the instructions there.

### Third Option

Clone repo and execute the following codes
```
pip install -r requirements.txt
```
```
python play.py
```

## Code Layout

- `api.py` - It defines the API that is being called by [vue GUI app](https://github.com/hakanonal/mastermind-ui). 
- `discovery/*.ipynb` - It is the temporary rapid development for the any agent.
- `main.py` - It is the main python script to executte the agent training for a fixed defined hyper-parameters.
- `play.ipynb` - It is the wraper to play the game in console via google colab environment.
- `play.py` - It is the script to play the game in console locally.
- `setup.py` - responsible for this repo packeging. 
- `Docker*` - Reponsible to dockerize the API to fast deploy live environment
- `sweep_example.yaml` - It is an example of [sweep](https://docs.wandb.com/sweeps) configuration.
- `train.py` - It is the wrapper script to train the agent with not only single set of hyper-parameters but for defined [sweep](https://docs.wandb.com/sweeps), so that single script can executes multiple runs for different set of hyper-parameters.