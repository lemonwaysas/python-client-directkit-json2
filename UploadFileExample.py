from LemonWay import *
import json, base64

with open('images/test.jpg', 'rb') as image_file:
    buffer_encoded = base64.b64encode(image_file.read())
    buffer = buffer_encoded.decode('utf-8')

    response = callService(
        'UploadFile',
        {
            'wallet': '123',
            'fileName': 'test.jpg',
            'type': '3',
            'buffer': buffer
        }
    )

    print(json.dumps(response, indent=4))