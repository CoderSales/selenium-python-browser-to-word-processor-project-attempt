from polygon import RESTClient # issue
# from polygon import polygon.rest
import polygon
# from restclient import restclient
API_KEY=''
client = RESTClient("API_KEY") # issue
polygon.rest("API_KEY")

url2=""
from polygon import RESTClient
from datetime import datetime
from dateutil.relativedelta import relativedelta

client = RESTClient(API_KEY) # api_key
client = RESTClient()  # POLYGON_API_KEY environment variable






client = RESTClient(api_key="<my_API_KEY")



aggs = []
for a in client.list_aggs(
    "AAPL",
    1,
    "minute",
    "2022-01-01",
    "2023-02-03",
    limit=50000,
):
    aggs.append(a)

print(aggs)
