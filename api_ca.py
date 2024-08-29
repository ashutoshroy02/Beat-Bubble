def make_api_call(filename):

    import base64
    import hashlib
    import hmac
    import os
    import sys
    import time
    import requests as r

    access_key = "b86e8e91257ec0cac71546cd036b5cf5"
    access_secret = "x6IW20OMPt9Ms3Rs2Dc8d8iWfbosFOvcrMHfEv8h"
    requrl = "https://identify-ap-southeast-1.acrcloud.com/v1/identify"

    http_method = "POST"
    http_uri = "/v1/identify"

    data_type = "audio"
    signature_version = "1"
    timestamp = time.time()

    string_to_sign = http_method + "\n" + http_uri + "\n" + access_key + "\n" + data_type + "\n" + signature_version + "\n" + str(
        timestamp)

    sign = base64.b64encode(hmac.new(access_secret.encode('ascii'), string_to_sign.encode('ascii'),
                                     digestmod=hashlib.sha1).digest()).decode('ascii')


    filename = "song.wav"  

    # Check if the file exists
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")

    f = open(filename, "rb")
    sample_bytes = os.path.getsize(filename)

    files = [
        ('sample', (f'{filename}.wav', open(filename, 'rb'), 'audio/mpeg'))
    ]

    data = {'access_key': access_key,
            'sample_bytes': sample_bytes,
            'timestamp': str(timestamp),
            'signature': sign,
            'data_type': data_type,
            "signature_version": signature_version}

    response = r.post(requrl, files=files, data=data)
    response.encoding = "utf-8"
    

    return response

    
