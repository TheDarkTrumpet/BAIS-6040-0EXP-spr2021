from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

allReports = [
    ("/report", "Sample Report")
]


@app.route('/')
def index():
    return render_template('index.html', reports=allReports)


@app.route('/report')
def report():
    return render_template('report.html')


if __name__ == '__main__':
    app.run(debug=True)
