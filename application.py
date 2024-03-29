from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return str(Fibonacci(20))

def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    
