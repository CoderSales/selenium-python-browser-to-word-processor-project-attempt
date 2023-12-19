# debugging

Error:

`requests.exceptions.ConnectionError: HTTPConnectionPool(host='127.0.0.1', port=5500): Max retries exceeded with url: / (Caused`

add a closing bracket for the parser:
)

[requests.exceptions.ConnectionError: HTTPConnectionPool(host='127.0.0.1', port=8000): Max retries exceeded with url: /api/1/](https://stackoverflow.com/questions/56010271/requests-exceptions-connectionerror-httpconnectionpoolhost-127-0-0-1-port-8)

fixed

____

## parsing bug

[nltk](https://www.nltk.org/install.html)
