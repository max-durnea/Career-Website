from flask import Flask

app = Flask("Carreer_App")


@app.route("/")
def home():
  return "Hello Wdorlds"


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
