# README #

## List of Dependencies ##

* Django 1.8 ('Django==1.8')
* Django Compressor ('django-compressor')
* SQLAlchemy ('sqlalchemy')

## Setup Instructions ##

1. Get Python 3. If you're on Mac, I recommend installing [Homebrew](http://brew.sh) and then running `brew install python3`. This will install dependencies and everything and make sure you're up to date.
2. After you do that, run `pip3 install virtualenv`. This will install the virtualenv module, which will help us with our dev environment.
3. Clone this git project into a folder. Go into that folder and type `virtualenv venv`. This creates your virtual environment. Aw yiss.
4. Open [this article](https://devcenter.heroku.com/articles/getting-started-with-django) for reference.
5. Run `source venv/bin/activate` to start your virtualenv.
6. Run `pip install django-toolbelt`. You shouldn't need to specify pip3 here, since we're in the virtualenv. It'll install a bunch of stuff needed to support the Django project.
7. You can skip the stuff about creating a project in the article in Step 4, because that's already done! Hooray!
8. If you want to start the project, you can run `foreman start` and then go to http://localhost:8080. If you want to stop the server, Ctrl+c.
9. Use the command `heroku git:remote -a deadcity` to add the heroku remote.
10. If you want to push directly to heroku, you can use `git push heroku master`, but if you push to the master branch on github, it'll automatically deploy to heroku anyway.
11. N.B. before you do step 9 create a heroku account and tell me (Carly) what it is so that I can give you permission to push to the remote.
12. Anyway that's basically it please let me (Carly) know if you have any questions and I can help you get your stuff set up
13. Emery if you have tips for Windows users please feel free to add them, I have no clue how Windows setup works anymore
