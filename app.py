from flask import Flask


app = Flask('__main__') # initialize flask app

if __name__ == '__main__':
    app.run(debug=True, port = 5000)

# absolute path: /Library/Frameworks/Python.framework/Versions/3.11/bin/python3
