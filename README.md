# Salary prediction API



# Table of Contents



heroku - platform as a service(Paas) is used here



# Heroku

1. procfile:
   1. the file to be executed the first is to be mentioned in this procfile
   2. since in our case, the app.py is to be run, we have mentioned that one
   3. `web:webServerType app:<FlaskAppName>`
2. requirements.txt
   1. required so that heroku can know what all python modules are needed for this to be run 
   2. logs in heroku can be checked for any missed out python modules