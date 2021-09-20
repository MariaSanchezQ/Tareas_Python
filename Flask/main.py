from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/primera")
def Primera():
  return render_template("Primera.html")

@app.route("/segunda")
def Segunda():
  return render_template("Segunda.html")

@app.route("/tercera")
def Tercera():
  return render_template("Tercera.html")

if __name__ == '__main__':
  app.run(
    host = '0.0.0.0',
    port = random.randint(2000,9000)
  )