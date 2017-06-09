# import the Flask class, and the function render_template
from flask import Flask, render_template

# create a new instance of the Flask class and save it into the variable app
app = Flask(__name__)

# map the url "/" to the function "index"
@app.route("/")
# defining function
def index():
  # return the index.html template
  return render_template("index.html")

# map the url "/about" to the function "about"
@app.route("/about")
# defining function
def about():
  # return the about.html template
  return render_template("about.html")

if __name__ == "__main__":
  app.run(debug=True)