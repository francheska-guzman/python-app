# Python and Flask

### Table of Contents

1. [About the project](#about)
2. [About Python](#about-python)
3. [Python has a design philosophy](#python-philosophy)
4. [About Flask](#about-flask)
5. [Flask popularity](#flask-popularity)
6. [Request-Response Cycle](#cycle)
7. [Sources](#sources)
8. [Installation](#installation)

## <a id="about">About the project</a>

General Assembly's Web Development Immersive <br />
Group Homework <br />
Developed by Esraa Alaarag and Francheska Guzman.

## <a id="about-python">About Python</a>

![Python](./images/python.jpg)

A widely used high-level interpreted programming language for general-purpose programming, created by Guido van Rossum  and first released in 1991.

![Rossum](./images/Rossum.jpg)

Python's name is derived from the television series Monty Python's Flying Circus, and it is common to use Monty Python references in example code.

![Python](./images/circus.jpg)

Python is a multi-paradigm programming language: object-oriented programming and structured programming are fully supported.

Python uses dynamic typing and a mix of reference counting and a cycle-detecting garbage collector for memory management. An important feature of Python is dynamic name resolution (late binding), which binds method and variable names during program execution.

The design of Python offers some support for functional programming in the Lisp tradition. The language has map(), reduce() and filter() functions; list comprehensions, dictionaries, and sets.

## <a id="python-philosophy">Python has a design philosophy</a>

- Beautiful is better than ugly

- Explicit is better than implicit

- Simple is better than complex

- Complex is better than complicated

- Readability counts

##### Examples
![example](./images/1.png)
![example](./images/2.png)
![example](./images/3.png)
![example](./images/4.png)
![example](./images/5.png)

[More examples](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

The python file extension is: .py

## <a id="about-flask">About Flask</a>

Flask was created by Armin Ronacher of Pocoo:

![Ronacher](./images/ronacher.jpg)

"It came out of an April Fool's joke but proved popular enough to make into a serious application in its own right."

Flask is a micro web framework written in Python, and is based on the Werkzeug toolkit (a utility library for Python) and Jinja2 (a template engine for Python), both of them Pocoo projects that were created.

Micro-framework are normally framework with little to no dependencies to external libraries or particular tools. This has pros and cons:

	Pros
	* The framework is light
	* There are little dependency to update and watch for security bugs

	Cons 
	* You will have to do more work by yourself
	* Increase yourself the list of dependencies by adding plugins. 
	
It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. 

## <a id="flask-popularity">Flask popularity</a>

![Flask Logo](./images/flask.png)

Despite the lack of a major release, Flask has become extremely popular among Python enthusiasts. As of mid 2016, it was the most popular Python web development framework on GitHub.

[Click here to see applications powered by Flask.](http://flask.pocoo.org/community/poweredby/)

## <a id="cycle">Request-Response Cycle</a>

![Request-Response Cycle](./images/reqrescycle.png)

![Request-Response Cycle](./images/reqrescycle1.png)

## <a id="sources">Sources</a>

* [Official Python website](https://www.python.org/)

* [Flask website](http://flask.pocoo.org/)

* [Lynda tutorial called Learning Flash](https://www.lynda.com/Flask-tutorials/11121-0.html)

* [A tour of the differences between JavaScript and Python](https://blog.glyphobet.net/essay/2557)

* [Python Tutorial: if __name__ == '__main__'](https://www.youtube.com/watch?v=sugvnHA7ElY)

## <a id="installation">Installation</a>

1. open Terminal and run:
2. **brew install python**
3. **pip install -U pip setuptools**
4. **pip install virtualenv** (Virtualenv enables multiple side-by-side installations of Python, one for each project. It doesn’t actually install separate copies of Python, but it does provide a clever way to keep different project environments isolated.)