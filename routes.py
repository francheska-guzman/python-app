# import the Flask class, and the function render_template
from flask import Flask, render_template

# create a new instance of the Flask class and save it into the variable app
app = Flask(__name__)

# map the url "/" to the function "index"
@app.route("/")
# defining function
def index():
  # render the index.html from the templates folder.
  return render_template("index.html")

# map the url "/about" to the function "about"
@app.route("/about")
# defining function
def about():
  # render the about.html from the templates folder.
  return render_template("about.html")

# __name__ is a special Python variable that holds the name 
# of the module currently being executed, except when the module 
# is started from the command line, in which case it becomes "__main__".
# When we user run "python routes.py", basically match if __main__ == __main__
# and run the app.
if __name__ == "__main__":
  app.run(debug=True)