# Python and Flask

## An introduction by Esraa and Francheska

### About Python

### About Flask

Flask was created by Armin Ronacher of Pocoo:

"It came out of an April Fool's joke but proved popular enough to make into a serious application in its own right."

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

1. brew install python
2. pip install -U pip setuptools
3. pip install virtualenv
3. open Terminal
4. cd Desktop
5. mkdir python_flask
6. cd python_flask
7. virtualenv venv
8. source venv/bin/activate
9. pip install Flask

### Creating the Project Structure

1. Inside the folder we already created (python_flask), run: "mkdir static".
2. cd static
3. mkdir css
4. mkdir js
5. mkdir img
6. cd ..
7. mkdir templates
8. touch routes.py
9. touch readme.md
10. python routes.py
11. open the browser and go to localhost:5000

At the end, your folder should look like this:

![Folder Structure](./images/folderstructure.png)

### Request-Response Cycle

![Request-Response Cycle](./images/reqrescycle.png)