from flask import Flask

app = Flask(__name__)

HTML = open("jarvproto.html")

@app.route('/')
def proto_hello():
    is_Connected = True
    return { "value": { "message": "Welcome to JarvProto!", "is_connected": is_Connected } }

if __name__ == "__main__":
    app.run(debug=True, host="local.jarv", port=65432)
