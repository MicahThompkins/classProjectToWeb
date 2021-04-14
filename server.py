from flask import Flask, request
from scan import ScanClass
app = Flask(__name__)
# scanner = ScanClass()

@app.route('/', methods=['POST'])
def hello_world():
    scanner = ScanClass()
    request_data = request.get_json()
    domain =""
    method =""
    # print(request_data)
    if request_data:
        if 'domain' in request_data:
            domain = request_data['domain']
            print("domain: " + domain)
        if 'method' in request_data:
            method = request_data['method']
            print("method: " + method)
    returnVal = {"output": scanner.scan(domain, method)}
    print(returnVal)
    return returnVal

if __name__ == '__main__':
    app.run()