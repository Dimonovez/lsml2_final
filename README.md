
## Final project: Fruit classificator

This app helps identify what fruit or vegetable it is. It has web interface and performs all tasks asynchronously.


Images: \
web: flask web app \
worker: celery \
model: flask restful web service, trained model \
redis: message broker

Container orchestration tool is used for managing containers.

## Model

Model: ResNet50, loss: CrossEntropyLoss, metric: Accuracy


Trained model is already included into model image.
To generate a new model:
1. run `model/train.ipynb`
2. rebuild docker images.

## Dataset

Fruits and vegetables were planted in the shaft of a low-speed motor (3 rpm) and a short movie of 20 seconds was recorded.

A Logitech C920 camera was used for filming the fruits. This is one of the best webcams available.

Behind the fruits, we placed a white sheet of paper as a background.

https://www.kaggle.com/datasets/moltean/fruits

## Usage instructions

Run the app:

```sh
$ sudo docker-compose up --build
```

Open browser to view web gui 
[http://localhost:5000](http://localhost:5000)

Get prediction:
1. upload new fruit/vegetable image (or use already uploaded)
2. click 'Check' 

And get fruit/vegetable name!
