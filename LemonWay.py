import socket, json, requests


# Put the Directkit JSON2 here (your should see 'json2' in your URL)
# Make sure your server is whitelisted, otherwise you will receive 403-forbidden
DIRECTKIT_JSON2 = 'https://sandbox-api.lemonway.fr/mb/demo/dev/directkitjson2/Service.asmx'
LOGIN = 'society'
PASSWORD = '123456'
VERSION = '1.8'
LANGUAGE = 'en'
SSL_VERIFICATION = False
UA = 'ua'


class LWException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return 'LWException: ' + self.value


# IP of end-user
def getUserIP():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip if ip != '' else '127.0.0.1'


def callService(serviceName, parameters):
    # add missing required parameters
    parameters['wlLogin'] = LOGIN
    parameters['wlPass'] = PASSWORD
    parameters['version'] = VERSION
    parameters['walletIp'] = getUserIP()
    parameters['walletUa'] = UA

    # wrap to 'p'
    request = json.dumps({'p': parameters})
    serviceUrl = DIRECTKIT_JSON2 + '/' + serviceName

    headers = {
        'Content-type': 'application/json;charset=utf-8',
        'Accept': 'application/json',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache'
    }

    response = requests.post(
        serviceUrl,
        data=request,
        headers=headers,
        json=None,
        verify=SSL_VERIFICATION
    )

    httpStatus = response.status_code
    if httpStatus == 200:
        unwrapResponse = json.loads(response.content)['d']
        businessErr = unwrapResponse['E']
        if businessErr:
            #logging.error(businessErr['Code'] + ' - ' + businessErr['Msg'] + ' - Technical info: ' + businessErr['Error'])
            raise LWException(businessErr['Code'] + ' - ' + businessErr['Msg'])
        return unwrapResponse
    else:
        raise Exception('HTTP Status = ' + str(httpStatus))
