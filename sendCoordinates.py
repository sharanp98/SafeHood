from flask import Flask, request, jsonify
import requests
import ai
import ssl

app = Flask(__name__)

# Nominatim reverse geocoding URL
NOMINATIM_URL = 'https://nominatim.openstreetmap.org/reverse'

@app.route('/api/coordinates_to_zipcode', methods=['POST'])
def coordinates_to_zipcode():
    try:
        # Parse JSON data from the request
        coordinate_data = request.get_json()

        lat = coordinate_data.get('lat')
        lon = coordinate_data.get('lon')

        if not lat or not lon:
            return x({"error": "Latitude and longitude are required."}), 400

        # Reverse geocoding to get zipcode
        params = {'lat': lat, 'lon': lon, 'format': 'json'}
        headers = {'User-Agent': 'YourAppName/1.0 (your.email@example.com)'}
        
        response = requests.get(NOMINATIM_URL, params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        nominatim_data = response.json()
        zipcode = nominatim_data.get('address', {}).get('postcode')

        if not zipcode:
            return jsonify({"error": "Unable to retrieve zipcode from the coordinates."}), 404

        # Fetch neighborhood safety data based on the retrieved zipcode
        safety_data = ai.get_neighborhood_safety(zipcode)

        return jsonify(safety_data)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error with Nominatim request: {str(e)}"}), 502
    except KeyError:
        return jsonify({"error": "Invalid response format from Nominatim."}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    #context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    #context.load_cert_chain(certfile='cert.pem', keyfile='key.pem', password='helloj')

    app.run(host="0.0.0.0", port=5000)