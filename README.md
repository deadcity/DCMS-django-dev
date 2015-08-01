# README #

## List of Dependencies ##

* Django 1.8 ('Django==1.8')
* Django Compressor ('django-compressor')
* SQLAlchemy ('sqlalchemy')

## Setup Instructions ##

1. Get Python 3. You can download an installer from python's [homepage](https://www.python.org/) or use your favorite package manager. If you're on Mac, I recommend installing [Homebrew](http://brew.sh) and then running `brew install python3`. This will install dependencies and everything and make sure you're up to date.
2. After you do that, run `pip3 install virtualenv`. (If you are on Windows, `pip3` might instead be `pip3.exe`.) This will install the virtualenv module, which will help us with our dev environment.
3. Clone this git project into a folder. Go into that folder and type `virtualenv venv`. This creates your virtual environment. Aw yiss.
4. Open [this article](https://devcenter.heroku.com/articles/getting-started-with-django) for reference.
5. Activate your virtual environment.
  * OS X - Run `source venv/bin/activate`.
  * Windows - Run `venv/bin/activate`.
6. Run `pip install django-toolbelt`. You shouldn't need to specify pip3 here, since we're in the virtualenv. It'll install a bunch of stuff needed to support the Django project.
7. You can skip the stuff about creating a project in the article in Step 4, because that's already done! Hooray!
8. If you want to start the project, you can run `foreman start` and then go to http://localhost:8080. If you want to stop the server, Ctrl+c.
9. Use the command `heroku git:remote -a deadcity` to add the heroku remote.
10. If you want to push directly to heroku, you can use `git push heroku master`, but if you push to the master branch on github, it'll automatically deploy to heroku anyway.
11. N.B. before you do step 9 create a heroku account and tell me (Carly) what it is so that I can give you permission to push to the remote.
12. Anyway that's basically it please let me (Carly) or Emery (for Windows questions) know if you have any questions and I can help you get your stuff set up.


## Deployment Instructions ##

1. Make sure of the following configuration in "DCMS/platform_settings.py". (Note: This file is intentionally not part of source control.)
```
DEBUG = False
COMPRESS_ENABLED = not DEBUG
STATIC_ROOT = <path where static files will be collected to>
```

2. DCMS does not use the Django ORM but there are still some Django modules we're using that do. They handle things like user account logins and session management. We need to make sure their tables are up-to-date. Run the following command from the project-root.
```
python3 manage.py migrate
```

3. DMCS's models are managed by SQLAlchemy. We do not yet make use of a migration tool. Until we do, they should be created from a fresh database, after we apply the Django migrations in step 2. Run the following command from the project-root.
```
python3 manage.py sqla_create
```

4. Collect and compile all the various static files to some place on the server where they will be served from. This should also compile the coffeescript and compress the resultant javascript. Run the following commands from the project-root. (I don't know what order these commands need to be run in and they might very well need to be run multiple times like below. I do know though that this works.)
```
python3 manage.py collectstatic
python3 manage.py compress
python3 manage.py collectstatic
```

I believe that should do it. Let me (Emery) know if you have any questions.
