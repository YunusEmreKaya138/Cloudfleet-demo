from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient, InsertOne
from datetime import datetime

app = Flask(__name__)

client = MongoClient("mongodb://mongo-service:27017") #this line connects to the MongoDB service
# Make sure to replace "mongo-service" with the actual service name if different
db = client["demo-db"]
collection = db["Calculations"]



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
    number = None
    
    #This line allows Flask to execute the following commands if an input is submitted through the HTML
    if request.method == 'POST':
        if int(request.form['number']) <= 0 or request.form['number'] == None: #find a way prevent null cuz this one not working
            warning = "Please enter a positive number."

            return render_template('index.html', warning=warning)
        
        else:
            number = int(request.form['number'])
            primes = [num for num in range(1, number + 1) if is_prime(num)]
            #This variables will use for data base section of the project
            primeCount = len(primes)          
            now = datetime.now()
            collection.insert_one({
                "Timestamp": now,
                "PrimeLimit": number,
                "PrimeCount": primeCount})
            
    #variable for displaying recent 10 logs
    recent_logs = collection.find().sort("Timestamp", -1).limit(10)

    return render_template('index.html', primes=primes, number=number, recent_logs=recent_logs)

# API endpoint (JSON)
@app.route('/api/primes', methods=['GET'])
def api_primes():
    try:
        number = int(request.args.get('number', 0))
        if number <= 0:
            return jsonify({"error": "Please provide a positive integer as 'number' parameter."}), 400
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid number parameter."}), 400

    primes = [num for num in range(1, number + 1) if is_prime(num)]
    primeCount = len(primes)
    now = datetime.now()
    collection.insert_one({
        "Timestamp": now,
        "PrimeLimit": number,
        "PrimeCount": primeCount
    })

    return jsonify({
        "prime_limit": number,
        "prime_count": primeCount,
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
