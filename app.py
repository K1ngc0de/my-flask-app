from flask import Flask, render_template

app = Flask(__name__)

import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # Use port from 
    # Используем порт из environmental variable PORT, if it is, else 5000
    port = int(os.environ.get("PORT", 5002))
    app.run(host="0.0.0.0", port=port)

