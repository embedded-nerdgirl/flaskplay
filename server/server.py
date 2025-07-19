from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/status")
def status():
    status_info = {
        "status": "ONLINE",
        "battery": "92%"
    }
    return render_template("partials/status_box.html", **status_info)

# This is where stuff gets weird, since this now needs to reach out to the visor camera
# array and stream the data to an embedded display here in the control panel.
#
# This will probably be a massive undertaking lol
@app.route("/camera")
def camera():
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)