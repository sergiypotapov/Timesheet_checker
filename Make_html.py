__author__ = 'spotapov'
import TimeC
from flask import Flask, render_template
app = Flask(__name__)

file_list, week_n  = TimeC.RunTests('D:/Test/')
@app.route("/")
def template_test():
    return render_template('template.html', file_list=file_list, week_n = week_n)

if __name__ == '__main__':
    app.run(debug=True)