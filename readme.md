###### An introduction by Esraa and Francheska

# Python and Flask

### About Python

### About Flask

![Ronacher](./images/ronacher.jpg)

Flask was created by Armin Ronacher of Pocoo:

"It came out of an April Fool's joke but proved popular enough to make into a serious application in its own right."

![Flask Logo](./images/flask.png)

Flask is a micro web framework written in Python, and is based on the Werkzeug toolkit and Jinja2 template engine, both of them Pocoo projects that were created.

Micro-framework are normally framework with little to no dependencies to external libraries or particular tools. This has pros and cons:

	Pros
	* The framework is light
	* There are little dependency to update and watch for security bugs

	Cons 
	* You will have to do more work by yourself
	* Increase yourself the list of dependencies by adding plugins. 

### Flask popularity

Despite the lack of a major release, Flask has become extremely popular among Python enthusiasts. As of mid 2016, it was the most popular Python web development framework on GitHub.

Applications that use Flask:

### Sources

* Official Python website: https://www.python.org/

* Lynda Course called Learning Flash: https://www.lynda.com/Flask-tutorials/11121-0.html

### Installation

1. open Terminal and run:
2. brew install python
3. pip install -U pip setuptools
4. pip install virtualenv

	Virtualenv enables multiple side-by-side installations of Python, one for each project. It doesn’t actually install separate copies of Python, but it does provide a clever way to keep different project environments isolated.

### Creating the Project Structure

1. cd Desktop
2. mkdir python_flask
3. cd python_flask
4. virtualenv venv
5. source venv/bin/activate

	Whenever you want to work on a project, you only have to activate the corresponding environment. 

6. pip install Flask
7. mkdir static
8. cd static
9. mkdir css
10. mkdir js
11. mkdir img
12. cd ..
13. mkdir templates
14. touch routes.py
15. touch readme.md
16. python routes.py
17. open the browser and go to localhost:5000

At the end, your folder should look like this:

![Folder Structure](./images/folderstructure.png)

### Request-Response Cycle

![Request-Response Cycle](./images/reqrescycle.png)