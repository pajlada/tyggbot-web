# tyggbot-web
web interface for tyggbot

## Requirements
 * Python 3 (tested with 3.4)
 * pip
 
## Installation
1. `git clone git@github.com:pajlada/tyggbot-web.git`
2. `cd tyggbot-web`
3. `pip install -r pip-requirements.txt --user`
4. `cp config.example.ini config.ini`
5. Open up **config.ini** in your editor of choice and modify the parameters to suit your needs
6. `npm install .`
7. `cd static`
8. `gulp build`

Now to run the website easily, while debugging or just testing things out, just run app.py with `./app.py`.
For more extended use, you should set up a WSGI Server with nginx or similar software.
