from flask import Flask

app = Flask(__name__) #'_main_'

@app.route('/home')
def greeting():
    return 'Welcome'

if __name__ == '_main_':
    app.run(port=3000)
