from flask import Flask, request, jsonify
import request

nominatimURL = 'https://nominatim.openstreetmap.org/reverse'
pincode = ""
app = Flask(__name__)

@app.route('/api/post_json', methods=['POST'])
def post_json():
    try:
        # Get the JSON data from the request body
        coordinateData = request.get_json()

        finalLat = (coordinateData['lat1'] + coordinateData['lat2'] + coordinateData['lat3'] + coordinateData['lat4']) / 4
        finalLon = (coordinateData['lon1'] + coordinateData['lon2'] + coordinateData['lon3'] + coordinateData['lon4']) / 4

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

        return pincode
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
    
