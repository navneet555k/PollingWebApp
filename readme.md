# Polling Web App using Oauth #


## Steps to runserver ##

- First we need to get into the environment so first cd into the folder in my case it is (pollingwebapp).
- Now to activate the environment use source env/bin/activate.
- Now cd mysite(name of folder).
- Now use the command "python manage.py runserver" this will activate the site 
- Now use the http provided to go to that url.
-Now you are at the main site.
## Procedures To follow ##

- If you are reading this then you must already be at the main site if not then follow the above "Steps to runserver" to get to the main site
- Now you have to login through google so select your account.
- Now you will directly directed to the page where all the questions are.
- Now you click on the question you want to vote for.
- Now you choose the option you want as the answer to the above question.
- Next you will be redirected to the results page for that question where you will see which answer has got how many votes.
- Now you have an option to vote again if you want.

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

