from flask import Flask, request, render_template
# import socket

app = Flask(__name__)


var = 0

@app.route('/')
def index():
    global var
    var += 1
    # ipaddr = socket.gethostbyname(socket.gethostname())
    return render_template('index.html',value = var)



if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True, host='0.0.0.0')
    