# dToDo

## About dToDo

dToDo provides an extremely easy way to track your daily tasks. There's no registration needed. Just a click to start to arrange your daily life. 

You todo-list will be tracked by an unique url, which works like the URL shortening. With this magic, you can easily sync your todo-list between different platform, just save your unique url as a synchronized bookmark.

## Example

#### Demo

[dToDo](http://dtodo.wyan.im/)

#### Screenshot
![image](https://raw.github.com/teloon/dtodo/master/media/images/intro.png)

## Prerequisites

* [tornado](http://tornadoweb.org)
* [mongoDB](http://www.mongodb.org/)

## How to run

1. checkout the code and install the prerequisites;
1. run `mongod` to start the mongo daemon;
2. run `python app.py` to start the tornado server;
3. visit http://localhost:8888;

#TODO

1. randomize the url id
1. fix demo problem
1. add logging module
1. fix bug: not delete the last todo
