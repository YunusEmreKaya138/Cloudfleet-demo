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
    number = "X"

    if request.method == 'POST':
        number = int(request.form['number'])
        primes = [num for num in range(1, number + 1) if is_prime(num)]

    return render_template('index.html', primes=primes, number=number)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
