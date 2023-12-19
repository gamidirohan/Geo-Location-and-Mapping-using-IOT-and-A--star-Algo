from flask import Flask, request

app = Flask(__name__)

@app.route('/receiveData', methods=['POST'])
def receive_data():
    try:
        # Get data from the request
        data = request.data.decode('utf-8')

        # Process and store the data in a CSV file
        with open('received_data.csv', 'a') as file:
            file.write(data + '\n')

        print("Data received and saved:", data)

        return "Data received successfully"
    except Exception as e:
        print("Error:", str(e))
        return "Error processing data"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
