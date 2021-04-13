from flask import Flask, request
from scan import ScanClass
app = Flask(__name__)
scanner = ScanClass()

@app.route('/')
def hello_world():
    request_data = request.get_json()
    domain =""
    method =""
    # print(request_data)
    if request_data:
        if 'domain' in request_data:
            domain = request_data['domain']
        if 'method' in request_data:
            method = request_data['method']
    returnVal = {"output": scanner.scan(domain, method)}
    print(returnVal)
    return returnVal

if __name__ == '__main__':
    app.run()