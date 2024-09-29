from flask import Flask, request, jsonify
import requests

nominatimURL = 'https://nominatim.openstreetmap.org/reverse'
pincode = ""
app = Flask(__name__)

@app.route('/api/post_json', methods=['POST'])
def post_json():
    try:
        # Get the JSON data from the request body
        coordinateData = request.get_json()
        # Do something with the data (for example, print it)
        print(coordinateData)

        finalLat = coordinateData['lat']
        finalLon = coordinateData['lon']

        print(finalLat)

        # Logic for getting pincode
        params = {
            'lat': finalLat,
            'lon': finalLon,
            'format': 'json'
        }

        headers = {
            'User-Agent': 'YourAppName/1.0 (your.email@example.com)'
        }
        nominatimResponse = requests.get(nominatimURL, params=params, headers=headers)

        if(nominatimResponse.status_code == 200):
            nominatimData = nominatimResponse.json()
            pincode = nominatimData['address']['postcode']
        else:
            print(f"Error: {nominatimResponse.status_code}")
            print(nominatimResponse.text) 



        # Check if the data is valid or has the required fields
        # if 'name' not in data or 'age' not in data:
        #     return jsonify({"error": "Invalid data"}), 400

        # Respond with a success message and the received data
        # return jsonify({
        #     "message": "Data received successfully",
        #     "received_data": data
        # }), 200

        return pincode
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
    
