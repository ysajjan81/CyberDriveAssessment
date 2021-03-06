# Cyber Drive Assessment

## Api Credentials End points

## Requirements 
- Python 3.8
- pip 20.2.3

## Intallation and setup

- Create Virtual Environment 
    1. pip install virtualenvwrapper-win
    2. mkvirtualenv envname 
    3. workon envname
( you can direct install django in system)
- pip install django
- pip install djangorestframework
- git clone https://github.com/ysajjan81/CyberDriveAssessment.git
- cd restApiAccountCredentials
- python manage.py runserver

### User Stories
- [X]  Endpoint for registration requres a user name, email, and password that meets basic complexity requirements. 
- [X] Login endpoint issues some type of token for authentication.
- [X] Logout endpoint causes the issued token to become invalid
- [X] Change password endpoint requires current password to be correct in order to apply new password. New password must meet complexity requirements.
- [X] Change username & change email endpoint requires current password.
- [X] Use the built-in SQLite database for the project.
- [X] The API should be run with the command: python manage.py runserver without any issues.
- [X] The API should have a superuser & a working admin dashboard. Include the superuser login credentials in your submission.

## Superuser Credential 
- Name - sajjan 
- Password - Samsung@135

### App Walkthough GIF
<img src="walkthrough.gif" width=800 height=400><br>

## Template used 
- Travello - (https://colorlib.com/wp/template/travello/)<br>
- Form - (https://www.w3docs.com/learn-html/html-form-templates.html)

