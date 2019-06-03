# reddit-vid

A program that aims to automate the creation of "reddit videos" (r/AskReddit style).

The goal for this project is to be able to composite text to speech audio alongside screenshots for a given reddit post and export it as a video. It is currently in development. 

The current state of the project is such that you can choose a reddit post and the program takes screenshots for all top level comments within the post. 

## Installation

Clone the repo

```console
$ git clone https://github.com/kyb3r/reddit-vid
$ cd reddit-vid
```

Install dependancies
```console
$ pipenv install
```

Create a .env file with your [reddit client id and secret](https://praw.readthedocs.io/en/latest/getting_started/quick_start.html).
```env
CLIENT_ID=xxxxxx
CLIENT_SECRET=xxxxxxx
```

Finally run the app via
```
pipenv run python3 app.py
```