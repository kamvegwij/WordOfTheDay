from flask import Flask, render_template, url_for, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'haveagreatdayxx'

@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template("home.html")

if __name__ == "__main__":
    app.run(app, debug=True)