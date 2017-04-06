from LemonWay import *
import json

try:
    print('---------- Wallet notexist: ----------\n')
    response = callService(
        'GetWalletDetails',
        {
            'wallet': 'notexist'
        }
    )
    print(json.dumps(response, indent=4))
except Exception as e:
    print(e)


try:
    print('---------- Wallet sc: ----------\n')
    response = callService(
        'GetWalletDetails',
        {
            'wallet': 'sc'
        }
    )
    print(json.dumps(response, indent=4))
except Exception as e:
    print(e)