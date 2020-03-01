# Polling Web App using Oauth #


## View Of The Projet In Images ##
Page:1 (main page)
![image](https://user-images.githubusercontent.com/53183532/75633120-4a1bbb00-5c28-11ea-9d8f-1ddf965e2e58.png)
Page:2 (google login)
![image](https://user-images.githubusercontent.com/53183532/75633154-7df6e080-5c28-11ea-8613-751f8950166b.png)
Page:3 (questions)
![image](https://user-images.githubusercontent.com/53183532/75633169-9535ce00-5c28-11ea-8496-a675f2da61ae.png)
Page:4 (details)
![image](https://user-images.githubusercontent.com/53183532/75633182-b5fe2380-5c28-11ea-8a9a-04733e2396ef.png)
Page:5 (results)
![image](https://user-images.githubusercontent.com/53183532/75633189-c57d6c80-5c28-11ea-85c4-7b4e6114ad73.png)


## Steps to runserver ##

- First, git clone my repo <br>
    ```git clone https://github.com/codenavneet/PollingWebApp.git```
- Then get into the environment <br>
    ``` cd PollingWebApp```
- Now to activate the environment use <br>
    ``` source env/bin/activate```
- Then - <br>
```cd mysite```
- Now use the command- 
    ```python manage.py runserver```
- Now use the http provided to go to that url.
## Procedures To follow ##

- If you are reading this then you must already be at the main site if not then follow the above "Steps to runserver" to get to the main site
- Now you have to login through google so select your account.
- Now you will directly directed to the page where all the questions are Here your usename (unique) and signout option will also be present redirecting you to the main page.
- Now you click on the question you want to vote for.
- Now you choose the option you want as the answer to the above question.
- Next you will be redirected to the results page for that question where you will see which answer has got how many votes.
- Now you have an option to vote again or  go back to the questions page to change question and vote again if you want.

## If you want to add Questions or Choices use this procedure ##
- Whatever you site is in my case http://127.0.0.1:8000/ change it to http://127.0.0.1:8000/polls/admin/ .
- Now you will be asked for username and password enter it now click on add questions or add choices whatever you require.
- Now for a choice you add select the corresponding question for it from the dropdown menu.
- Now you have added new questions or choices as you required.
- Now go to http://127.0.0.1:8000/polls/ you will be able to see the added questions.
- So this is it  for this section you are all set.

## TO add a Oauth service provider do the following ##
- Djando framework offers various sign in options google,facebook,github,...etc.
- In this project i will be signing in through google so i will tell about it.
- add some things to installed apps in settings of the project
-   'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'login',
SITE_ID=1
LOGIN_REDIRECT_URL='http://127.0.0.1:8000/polls/'
- After adding all this you when you runserver you will get a socialapp sections
- Now add that provider as google and all the details required name the url as localhost:8000
- Now get client id and secret id from https://console.developers.google.com/ .Here i will not be mentioning my client id and 
secret id as it might be used in some undesirable manner if needed ask me for it personally.
- Add  client id and secret id .
- Now LOGIN_REDIRECT_URL='http://127.0.0.1:8000/polls/' is for redirecting you to the page which should appear just after you google sign. The above is what is my redirect page.
- This is it we are now able to sign in through google into our site.

### How I Felt Doing This Project ###
+ So first of all this is the first project of my life as i am completely new to Web Development.
+ The most important thing i have learnt while doing this project is that for any problem i can trust google or youtube it helped me a lot :)
+ Sometimes when you put in effort and you get so many errors we should not get frustated and continue working again late in my case i had to create environment nearly 6-7 times to atlast get the basic model working because i was not able to resolve errors in previous environments.
+ But yes when you get things working you feel much happier than ever.

## What else did i learn ? ##

- The most valuable thing i learned was git which helped me when i was not able to drag and drop more than 100 files in github. Git made things si much easier for me.
-
How did I install Django ?
So basically what I did was I had to setup a virtual env
```pip3 install virtualenv```
In virtual env use ```source bin/activate``` to activate the virtual environment 
Then simply use ```pip3 install Django```

### What is a virtual environment? ###
A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This is one of the most important tools that most of the Python developers use.

### Details regarding Django admin ###

Django password: bullu@123
Username: navneet

How to create an app:-
```Python manage.py startapp (appname)```

Two http methods are as under:-
post and get
Get is for fetching the data from server
Post is for adding new data to server

To create superuser:-
Python manage.py createsuperuser

In Django model view template

Template includes:
Html 
Css javascipt
And dal (Django template language) for including dynamic data 


ORM(object relational mapper)

psql -U postgres


I learnt about this but this but was of no use:-

CREATE DATABASE name
\list(list all the current databases available)
\connect (name of database) ;

To delete a database use this command

DROP DATABASE (name of database);

My master password for pgadmin is navneet@123

To start a project:-

Django-admin startproject mysite


