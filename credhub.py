"""
A simple Cloud Foundry Flask app to test PCF Credhub Service Broker

Author: Mark Alston
License: See LICENSE.txt

"""
from flask import Flask
import os
import json

app = Flask(__name__)

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))

@app.route('/credhub')
def credhub():
    print('------- Start: credhub values ------\n')
    if 'VCAP_SERVICES' in os.environ:
        services = json.loads(os.getenv('VCAP_SERVICES'))
        creds_env = services['credhub'][0]['credentials']
        for cred_key in creds_env:
            print(cred_key)
        for cred_value in creds_env.values():
            print(cred_value)
    else:
        print('------- End: credhub values ------')
        return 'Env variable VCAP_SERVICES was not found'

    print('------- End: credhub values ------')
    return 'Credhub successful - see application log'

if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
