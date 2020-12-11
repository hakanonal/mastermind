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
        - Ok I am moving pretty fast I am almost there. Now time to time agent guesses 0 because there is 0 in the q_table. The greedy method also considers the actions that is below 1111. Now what? 
            - In thory if I explore all the time I will not bump this error. and it is working. So the greedy method has to be fixed.
    - How to fix greedy method.
        - Ok! actually I did very similar solution on my tic-tac-toe project. I can iniitially assign very negative number for the items that are not in action space. An it is completed.
- We got the first result: 
    - wandb dashboard has been configured. you can check it from [here](https://wandb.ai/hakanonal/mastermind)
    - Unfourtunatelly avarage win is very close to zero. Here is the [run](https://wandb.ai/hakanonal/mastermind/runs/1byxxyuq) Since the number of avaible states and avaible action space very large. policy file is rediculasly large and memory consumption is mindbuggling. in 1000 episodes it is resanablly fast but it is not enough for training. So when we increase the episode number q-table gets very large. The program tries to memorize all posisbilites and simply it is not enugh area to memorize all posisbilies. In this circumtances we need to convert this into NN. 

- Before moving into NN, I want to make this code a playable game for everybody. So I am again trying to host the code on colab so that everybody can run the code without installing any python lib on thier local environment.
    - I have check [this](https://www.programiz.com/python-programming/package) article. There is a __init__.py in every module. What is that?
    - [This](https://packaging.python.org/tutorials/packaging-projects/) article explains the pip packaging procedure fully.
    - Read about [this](https://docs.python.org/3/tutorial/modules.html#packages)
    - Implemented the [setup.py](https://github.com/hakanonal/mastermind/blob/main/setup.py). Will see the results. Unfourtunatelly I can not make it. I am tired. Will look at it with a fresh mind.

#### 08.12.2020

- This journal location is bugging me. I did not like to write in wiki pages interface. So I am looking places to keep this journal. I am trying a seperate file. Inpired from [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/about-readmes)
    - Yes! this is definatelly better.
- Now where were we? Today I want to work on this [card](https://github.com/hakanonal/mastermind/projects/1#card-50796206) create hostable environment for users to play this game. 
    - Curentlly I am intershipping in a software company. I am learning [vue](https://vuejs.org) framwork here. Maybe I can create a vue interface for the game.
    - This reposotory is completed strutured for python environment. Should code it here or create another reposotry.
    - I want to reuse the code that I have contructed here. However the game rues fairlly simple. Maybe I should completelly re-write in vue JS and only call the AI functionallty via API.
        - When check the environment class, the whole environment is ment to be prepeared for AI to be trained. And it is designed as console app. When I check agent class, there is nothing to re-use there because it consists of training advancements where vue framework has nothing to do with that. 
        - On the other hand environment class has:
            - code generation
            - state struture (which is key element of both apps)  
            - isEnded method
            - play method
        - Maybe I can convert these into an  API that initiates a game and updates the stuture. That would be good baseline for the following future [card](https://github.com/hakanonal/mastermind/projects/1#card-50796246)
        - I am considering to create seperate reposotory for the front-end, becasue it will be easier to deploy to live. Or is it?
            - [This](https://blog.logrocket.com/build-deploy-vue-js-app-github-pages/) article is very helpful. It kinf of explains and also provides and automated node.js script file. But how the github pages work? I have very well understood how github pages are working. I hacve even created a test vue default project and deployed to [here](https://hakanonal.github.io/my-first-vue/dist/#/). the [repo](https://github.com/hakanonal/my-first-vue). To sum up:
                - Create the vue.config.js file like [this](https://github.com/hakanonal/my-first-vue/blob/master/vue.config.js)
                - dist folder should not be ignored by git.
                - From github reposotory setting enable github pages for root. 
                - Wait for couple of minutes.-
        - So I will be creating seperate reposottry. Ok frontend is done how about back-end. How should I deploy it?
            - Flask seems pretty easy to use according to [this](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask) article. I can create an api.py that accesses the environment. Hmmm that would be evan interesting because by this way there would be only one instance of state and everybody would be able to play the same game. How interesting :)
            - [This](https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f) article is a little bit more sophisticated. It combines the methods via class and declares the class as resource. So the class has to be iin aligened with API. [This](https://gist.github.com/jamescalam/0b309d275999f9df26fa063602753f73) is the full script.
            - Maybe [this](https://palletsprojects.com/p/flask/) official pages should be read. Alright [this](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) page is a little bit more straightforward.
    - Ok It is all set let's code. I will create api.py that creates the environment and exposes to the flask API. 
        - I neeeded to re arrange the validateUserInout method so that it can be exposed. It was specific to console app.
        - Well I think I did a very convinient way to expose the game as API. I am exited to use it in vue.
        - However I do not know how to deploy this API to where. I'll do that later better to note it to project [board](https://github.com/hakanonal/mastermind/projects/1).
            

- By the way this packaging system is not completed yet and it is bugging me since vscode continouslly lints errors even though the code is perfectlly working. I want to look this topic today also.
    - So I have chance to look this topic. And I think I have solved it. The problem was about linting and solved changing the vscode settings. [This](https://stackoverflow.com/questions/1899436/pylint-unable-to-import-error-how-to-set-pythonpath) article helped.
    - I have also moved the environment and agent clases into ai module.

- Yeah I have also managed to make work the colab hosted notebook work. So By this way peaople does not have to install python environment on their machine to play.
    
    
#### 09.12.2020

- I have relized that my [hosted play notebook](https://colab.research.google.com/github/hakanonal/mastermind/blob/main/play.ipynb) does not explain the board view. It should also explain.what the numbers mean. Done!
- Today I want to continue on [card](https://github.com/hakanonal/mastermind/projects/1#card-50796206) 
    - Before moving into vue front-end app I want to quicklly investigate how am I going to deploy the back-end API. I want it free and simple. Like github pages.
        - I think I found a good solution. pythonanywhere.com is service. It enables you a console. Will try to deploy my code there.
        - Side note: I have learned that by providing the python version of to the virtualenv command, you can create different virtual environments with different python versions without using pyenv. [This](https://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv) helped. In my case pythonanywhere has installed all python version into the path /usr/bin/python3.7
        - Ok first of all wandb gives some kind of a error. however the play.py script works fine. When I execute the api.py I get OSError: [Errno 98] Address already in use.
        - This is going to take more time then I think. I will check this later. However there seems to be solutions. It seems a little bit complicated then I thoght the official [doc](https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/)
        - I can not get out of it I am stucked. [This](https://dev.to/thetrebelcc/how-to-run-a-flask-app-over-https-using-waitress-and-nginx-2020-235c) article is another useful one. For simple live flask serve. Well simple enough. I have modifed api.py and all we need a python environment on a internet connected server. I am leaving this topic now.
    - Now vue app and new repository yeah! I am exicted. but first I need to pee... :D
        - New reposiitory has been installed. I have created a fresh vue app and deployed it to github pages. Now let's begin the hard part.
        - [Repo](https://github.com/hakanonal/mastermind-ui)
        - [Published Game](https://hakanonal.github.io/mastermind-ui/dist/#/)

- Starting to code vue.
    - Well how can I construct the UI. I need a decent design for that.
    - I need a component that is like a button and will be selectable a color. Where each color is representted by number. Maybe I can find such component on the net.
        - Well that was easy [this](https://saintplay.github.io/vue-swatches/examples/#simple) seems perfect. Maybe I can wrap this component with my component so that I can convert the color into digit.
            - I am trying to wrap this component to my component called Digit. And I am having trouble to properlly work. I am stuck already. The build does not give any error but, browser console gives the "vue-swatches.umd.min.js?7f75:1 Uncaught (in promise) TypeError: Cannot read property '_c' of undefined". Well I give-up vue swatches does not seem to be working properlly. It has also no proper documentation. about this error.
        - Lookin for another component. Well all other components are very complicated. This was pretty easy to use. Maybe it has problem with type script? Well there is no other option to use vue-swatches at this poiinit I need to figure out this error.
        - It is not about typescript. I have created an empty project and tried to use the swatches there. I get the same error. I will try other versions of swatches.


#### 10.12.2020

- Continue on vue app. 
    - I am suspicous about the versions of my environment. So I will try different versions of node vue and swatches.
    - vue. And yes a fresh installation of vue 2. I have easilly managed to show the swatch there.
    - Now how am I going to convert the my repo to vue 2 :/. Yeah! I have go over both my repo and my test vue2 empty project and copy paste adapted the code accordinglly. And the swatch did work. vue gives no error at all. However, the vscode linter gives some errors. I want to also that. Ok that was also easy I have closed vscode window and reopened the project it has gone. So we can continue where we have left off.
    - I have come over bunch of problems which are almost imposible to list them all here. I have go thorugh them pretty quicklly.  However the problems where all around typescript related.
    - Got "Avoid mutating a prop directly" error. I understand that putating a prop is not good idea. Instead mutate regular variable and you are ok.
    - Now I am looking for swatches [API](https://saintplay.github.io/vue-swatches/api/props.html) ini detail.
        - Well not much to do here.
    - I will try to create the board. This front-end jon is painful. There is too much trial and error.
    - I am going over [this](https://class-component.vuejs.org)  article. Hence It is important for me to understand the coding style.
    - I still did not understand how Props computed methods getters and setters. In digit component I have color data. When it is changed I wantt the digit's value property to respective digit value. and vica-versa. So???. So many questions...

#### 11.12.2020

- I was mainlly working on my internee job. So I will have limited tiime to work today. Will continue on vue.
    - Finally after many trial and errors. I have managed to at least construct the board. 
        - The paramatization bedazzled me a lot. 
        - Also typescript errors is enourmouslly high. It even gives errors for spaces and so...
        - Note that during this process I did more than 10 google search for different little errors...
    - I have checked how to call API. [This](https://vuejs.org/v2/cookbook/using-axios-to-consume-apis.html) helped. So I have installed axios
    - I have bumped into CORS error in console I think I need to adjust API server to fix this. 
        - I find [this](https://github.com/may-day/wsgicors) but I did not understand. 
        - Since the postman get send sucesfully api calls I am lookinig for aixon right now.
        - I will try clients to call API this should not be that much painfull.
        - I am trying [fetch](https://www.npmjs.com/package/fetch)
        - Trying another [client](https://www.npmjs.com/package/node-fetch). I am very surprised this this is so complicated. I am getting the same CORS error.
        - I have go back to axios cors solutions read [this](https://stackoverflow.com/questions/50949594/axios-having-cors-issue)
        - I go back to server side again. found [this](https://flask-cors.readthedocs.io/en/latest/) flask cors. YES!! this solved it.