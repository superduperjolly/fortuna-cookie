# Fortuna-cookie
A simple and fun app that allows you to play around with yours or other
people's fortunes.

Please don't take it personally.

## To run
First, make sure your device has [Docker](https://docs.docker.com/get-docker/) installed. It's very important to containerize your code for others to run it easily. 
To even make things easier, I've used simple Make commands for you to run.
Before you can run the app, we have to build the image first by:
```
make build
```
Once the image builds successfully, you can now run the app by:
```
make run
```
The app is now accessible at http://0.0.0.0:5000/

## Some technical details
The app was built with Flask, with the front-end being 


## Future improvements

+ Use other front-end libraries like ReactJS
+ Transfer the persistence of data in the front-end, not in the back-end
+ (!!!) Add tests
