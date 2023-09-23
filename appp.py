from flask import Flask, request, jsonify
import hashlib
from block import Blockchain  # Import your blockchain code

from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors

app = Flask(__name__)
CORS(app) 
bc = Blockchain('data.txt')  # Create a global instance of your Blockchain class

@app.route('/api/verify', methods=['POST'])
def verify_cid():
    data = request.get_json()
    target_cid = data.get('target_cid')

    exists = bc.cid_exists(target_cid)
    return jsonify({'exists': exists})

# IPFS API endpoint (assuming your IPFS daemon is running locally on the default HTTP port)
ipfs_api_url = "http://127.0.0.1:5001/api/v0/add"

# Function to upload data to IPFS and return the CID
def upload_data_to_ipfs(data):
    # Create a request payload with the data
    files = {'file': ('temp_data.txt', data)}

    # Upload the data to IPFS
    response = requests.post(ipfs_api_url, files=files)

    if response.status_code == 200:
        data = json.loads(response.text)
        return data['Hash']  # Return the CID for the uploaded data
    else:
        return None

@app.route('/upload-data', methods=['POST'])
def handle_upload():
    try:
        data = request.get_json()
        user_data = data.get('userData')

        if user_data:
            print(f"User-provided CID: {user_data}")
            # Upload user's data to IPFS
            data_cid = upload_data_to_ipfs(user_data)

            if data_cid:
                # Append the CID to data.txt
                with open('data.txt', 'w') as data_file:
                    data_file.write(f"Uploaded Row CID: {data_cid}\n")

                return jsonify({'cid': data_cid}), 200
            else:
                return jsonify({'error': 'Failed to upload data to IPFS'}), 500
        else:
            return jsonify({'error': 'No data provided'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
