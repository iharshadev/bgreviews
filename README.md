# Boardgame Geek Rating predictor

## Introduction
This is a Django REST server built to serve a Naive Bayes model trained to predict the potential rating for a given review about a board game. 

The [dataset](https://www.kaggle.com/jvanelteren/boardgamegeek-reviews) used to train the model is obtained from Kaggle thanks to [@jvanelteren](https://www.kaggle.com/jvanelteren)


## How it's implenented
At it's core, this REST serves a model that is pre-trained and pickled in the `model` directory. `scikit-learn` is used to train, tune, evaluate the model and predict rating.


## Instructions

Running a local server
```bash
$ git clone https://github.com/iharshadev/bgreviews
$ cd bgreviews
$ pip install -r requirements.txt
$ python manage.py runserver
```

Deploy to Heroku

## Links
1. Detailed explanation on how the model is trained can be found [here](https://iharsha.dev/blog/2020-05-11-bggratings)
2. [Live Demo](https://bgrating.netlify.app/)
3. [Video Demo](https://www.youtube.com/watch?v=L5gGwx_F_H4)
