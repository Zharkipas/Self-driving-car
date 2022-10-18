from flask import Flask

app = Flask(__name__) #'_amin_'

@app.route('/home')
def greeting():
    return 'Welcome'

if __name__ == '_main':
    app.run(port=3000)
