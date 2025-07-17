from flask import Flask, render_template, request

app = Flask(__name__)

#prime number calculator
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#getting requested number and re push it
@app.route('/', methods=['GET', 'POST'])
def index():
    primes = []
    number = "n"

    #This line allows Flask to execute the following commands if an input is submitted through the HTML
    if request.method == 'POST':
        if int(request.form['number']) <= 0:
            warning = "Please enter a positive number."
            
            return render_template('index.html', warning=warning)
        
        else:
            number = int(request.form['number'])
            primes = [num for num in range(1, number + 1) if is_prime(num)]
            #his variable will use for data base section of the project
            primeCount = len(primes)          

    return render_template('index.html', primes=primes, number=number)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
