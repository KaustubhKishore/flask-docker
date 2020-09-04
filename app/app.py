from flask import Flask, request, render_template

import os
import re

cmd = "head -1 /proc/self/cgroup|cut -d/ -f3"
cmd_out = os.popen(cmd).read()

app = Flask(__name__)


var = 0

@app.route('/')
def index():
    global var
    var += 1
    return render_template('index.html',value = var, cont = cmd_out)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    