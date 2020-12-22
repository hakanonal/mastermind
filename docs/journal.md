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
        - Ok! actually I did very similar solution on my [tic-tac-toe](https://github.com/hakanonal/tic-tac-toe) project. I can iniitially assign very negative number for the items that are not in action space. An it is completed.
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
    - Ok since I think I have a missing reout in my API. I just need a response for the current state no action.
        - Perfect now API call core is also ready. And It was painful.

#### 13.12.2020

- Vue app continue. 
    - Finally the fun part begins. Just use what you have constructed so far. yeah!..
    - Well it is goıing well. I have installed ant-design vue using [this](https://antdv.com/docs/vue/getting-started/) page
    - I am trying to add a restart button at the top. Using [this](https://antdv.com/components/button/) reference
    - So I still have problem when updating the state. In the digit component I get the value and set the valuelocal computed porpoerty when mounted. However It should always watch the porperty value.
    - I have choose some colors from [here](https://www.usability.gov/how-to-and-tools/methods/color-basics.html)
    - Before moving to taking the user feedback and moving to the up of component tree I will also implement the disablity of the chances.
    - Yeap I think we are ready move up now.
    - YEAH!!! it is working finally we got figure it out.
    - Now I need to paramitize the live environment parameters.
        - I have tried [this](https://stackoverflow.com/questions/50828904/using-environment-variables-with-vue-js) article however could not make work yet. And it worked.
    - I also want to show an error message if there is an API access problem.
    - I also need to compare the states before sending played code. Since the API serves a single game, multiple players may overwrite thier actions.
- Deployment...
    - I am trying to deploy my API to Firebase as described [here](https://medium.com/firebase-developers/hosting-flask-servers-on-firebase-from-scratch-c97cfb204579)
    - It seems so complicated for me now. I decided to dockerize the back-end.
    - I bumped into [this](https://medium.com/@justkrup/deploy-a-docker-container-free-on-heroku-5c803d2fdeb1). I decided to open up an account on [heroku](https://www.heroku.com). We'll see what will happen there...
    - Alright it seems pretty straight forward. It is very well documented. And for the scale of my app it is going to be free hopefully.
    - I need to install Heroku CLI on my computer, so I am trying to the that with my limited internet connection. :/
        - All my god it requires, xcode-select. And it takes forever to install...
        - Instead of installing via homebrew I will install the package right away. It is downloading much more faster. Yes I have installed heroku CLI
    - Now trying to deploy via docker image registry using the heroku CLI according to the documents.
        - I am very exciting it seems very promising. "heroku container:push mastermind_api -a hakanonal-mastermind" I used This command, which I can send any pre-built image in my local to -a parametirezed heroku app that is created from the console. 
        - [This](https://dashboard.heroku.com/apps/hakanonal-mastermind/deploy/heroku-container) is the documentation to deploy via heroku container method. 
        - Well it seems to deploy however it is not responding. I think it is about the exposing different port.
            - [This](https://stackoverflow.com/questions/44548074/how-do-i-expose-ports-on-heroku-with-a-dockerfile) may be the answer We'll see...
            - [This](https://github.com/heroku/alpinehelloworld/blob/master/Dockerfile) ,s an example Dockerfile.
            - PORT does not seems to be the problem though. They called dyno and it is not running right now. Looking ways to make it run.
            - The dyno does not seem to be running that's why it is not servicing. That's my assumption though.
            - I am suspicous that since it is a free plan it does not prioritize to start.
    - I am started to look other hosting services. Heroku was seems to fine but I did not get the final reusult. Looking [this](https://www.whoishostingthis.com/compare/docker/) doc
    - Ok I am back go google cloud. I agoing over the panel of google kubernetes. It says first cluster is free. We'll see...
        - So it was very convinient for kubernetes to pull the Dockerfile from github.
        - YEEES! It worked. It is very convinient. you do not have to install anything. It can directlly depoloy from github. So vala!
        - [Here](http://35.197.194.250:5000) This address may change in the feature.
    - Now I am going to configure this to the vue app and we will be on-line.
        - hmmm now I get mixed content error on the browser. I need to serve the API from secure layer.
            - [These](https://cloud.google.com/kubernetes-engine/docs/how-to/managed-certs#console) are very painful
            - [this](https://estl.tech/configuring-https-to-a-web-service-on-google-kubernetes-engine-2d71849520d) is proper explanation but it is damn hard.
    - Is there a way to deploy the vue app on a non secure place?
        - github pages does not allow me to do that.
    - Come on IBM cloud does not accept my credit card. Altogh it is valid. Pass...
    - Let's move on AWS... Nope!
    - Tried firebase which was easy by following [this](https://cli.vuejs.org/guide/deployment.html#firebase) article. However it is also secure and can not be disabled.
    - Ok I am back to digital ocean. I could easly deploy my docker on a droplet. And now looking ways to install SLL.
    - It looks like I need to modify my python script to do that. [here](https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https)
        - waitress does not seem to use properlly ssl. [here](https://stackoverflow.com/questions/19462959/i-can-not-connect-to-https-waitress-wsgi-server)
        - well At least I have activated self signed certificate. However the browser still gives error and won't access the API.
        - [This](https://mherman.org/blog/dockerizing-a-vue-app/) article was helpful for Dockerizing the vue app.
        - I am so tired. In the end I could not managed to do that. I am going to continue for antoher time.

#### 14.12.2020

- Continue on deployment on a fresh day...
    - Well ok when I was reading [this](https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https) article it tells about [this](https://letsencrypt.org/getting-started/) free service that gives SSL certificates. 
    - You're kidding me!  I was just hanging arround pythonanywhere just changing some nobs. I have tried some different variations on WSGI config and valia. So it is totally free. I do not bealive...
    - Finally it is working. 
        - The [API](https://hakanonal.pythonanywhere.com)
        - The [front-end](https://hakanonal.github.io/mastermind-ui/dist/#/)

- Now that is weird: the disabled class has the opocity of %1 in the browser. However, I had coded it as %30 how on earth it has built to %1.
    - I will try on a fresh browser. Nope!
    - I will rebuild and re-deploy. I did re-deploy but git found no difference.
    - I could not figure out the problem and temprarolly manually modifed the index.html inside the dist folder. I know I should not do that but I do not want spent more time on this.

- And [this](https://github.com/hakanonal/mastermind/projects/1#card-50796206) card seems to be completed. Very big achivement for me. Many Thanks!


- So changing gears here. Will continue on working [this](https://github.com/hakanonal/mastermind/projects/1#card-50796280) card
    - So now I am remembering my [tavla](https://github.com/hakanonal/backgammon) project's agent class to implement NN here.
    - Ok I have copied and modifed the neceesarry code. But I need to figure out the shape of the NN.
    - A generic way is 2-d array of state for input and a single node regressor. Would be useful for all game configs. The input shape would be game's chances parameter depandent but at least there will be no change when the digit has changed.
    - Ok When I re-think this game has not have finate set of actions to take. The NN has to guess next code according to the state. So How could implement the rewards in to this NN? very big question. Since my previous projects was spitting out the reward for the finiate output nodes of action. I will not be able to implement this here...
    - Well in here it tells brieflly some applied algorithm in the past. Nobody applied NN for this problem. Where when I re-thinik it would be incorrect to apply. However I need to understand better these cases. Curentlly I have opned-up another branch for this development.

#### 22.12.2020

- I am back on [this](https://github.com/hakanonal/mastermind/projects/1#card-50796280) card again.
    - Reading about [this](https://github.com/wy/PyMastermind#game-ai). An example implementation of mastermind AI
        - I am having hard time to understand the code. It creates all posible codes in an list. Then for each gıess it removes it from the list using the feedback. But I did not understand how it evaluate. Since it loops thorugh all posible answers and evaluateds them all. Which is redicualis, becuase by this method we give ai almost infinate chance to try.
    - Started to read [this](https://stackoverflow.com/questions/1185634/how-to-solve-the-mastermind-guessing-game)
        - Ok when I read a paragraph from that article, I have understand that it is not evaluating against the hidden code it is evaluating againts the the guesed code and removing the possible answers that thier feedbacks are not same as the guess.
    - So what I have understand is these two above solutions are the algorithms that is applied [here](https://en.wikipedia.org/wiki/Mastermind_(board_game)#Worst_case:_Five-guess_algorithm)
    - I understand that there may be multiple different algothims that can be applied. I thinking of to create multiple types of agents so that I can compare them. NN may be one of them but I will not implement it yet. Since I am not sure how to implement a NN here. Even, it may be rediculis to implement NN here.
    - How will I paramitize the agent though? I have opened a [card](https://github.com/hakanonal/mastermind/projects/1#card-51667464) for that
    - Before paramitizing agent I wanted to finilize the input and output shape of the NN. Where input is 12(chances)x(1(red)+1(white)+1(played_code)) conv and output is just 1(). Where input should be complete state. and output is the prediction for next move.
    - However I still do not know how to train against what? Should I spit out score and where? Maybe I can output 4(digits)*6(peg_count) that encodes the  all avaible next code scores...
    - to find the best working code more quicklly. I have created an [experiement]() notebook.
    - Good so as an output I have 4x6 array for each digit I have scrpore for each pegs. I can update the score for each digit??
    - Wow! I think I have nailed it...
    - So first try I do not have any wins. I merged the nn branch and continue with main.
    - I have increased. episode and see if there is going to be a win.

- Documented the code layout in readme.

- Stating a new [card](https://github.com/hakanonal/mastermind/projects/1#card-51670583) to fine tune the NN
    - Well [this](https://wandb.ai/hakanonal/mastermind/runs/1jxd9i2k) run is just a little bit better performer than q-table version. However it is a lot slower of course. 
    - Since the NN model is tiny. I can execute save every update.
    - Can I implement wandb [resume](https://docs.wandb.com/library/resuming) functionaltyy? 
        - Well I have implemented ther resume functionalty however the metrics are not in good shape. Since the program re-starts it does not remember the total and avarage win, loss and rewrard. It would be very convinient if I could log only mark of reward win and loose and other parameters would be calculated by wandb. So I could analyze them by runs easily.
        - Or I can read the metrics from the run. Nope!
        - Well it messes up all run logic so. I have discard my changes about this.

- It is time to deploy it a server so that it can run un attended.
    - Well I do not need to run this on a GPU enabled server.
    - I have installed pyenv via the official github page. [here](https://github.com/pyenv/pyenv) and [here](https://github.com/pyenv/pyenv-installer)
    - I have installed gcc via ```sudo apt-get install build-essential```
    - Had to install dependecies first used [here](https://github.com/pyenv/pyenv/wiki/common-build-problems)
    - Installed python 3.7.2 ```pyenv install 3.7.2```
        - Takeing longer then expected...
    - Created a virtual environment ```pyenv virtualenv 3.7.2 mastermind```