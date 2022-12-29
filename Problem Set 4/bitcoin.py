#must have requests module installed to work
#pip install requests

import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument.")

elif sys.argv[1].isalpha():
    sys.exit("Command-line argument is not a number.")

else:
    n = float(sys.argv[1])
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    out = request.json()

    ratefloat = out["bpi"]["USD"]["rate_float"]
    cost = ratefloat * n
    print(f"${cost:,.4f}")
