from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
  return {"message": "HEllo guys (python flask)"}
app.run()
