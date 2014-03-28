from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
  return "We the best!"

if __name__ == "__main__":
  app.run()


