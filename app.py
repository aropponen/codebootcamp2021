from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
        return render_template('base.html', title="BootCamp2021", heading="BootCamp2021", content="Hello world!")

if __name__ == '__main__':
    app.run()