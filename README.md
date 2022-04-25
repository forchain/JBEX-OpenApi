# jbex openapi

* doc directory: include the openapi doc, you could make your sdk with the doc.
* SDK directory: include java and python sdk

If you have any questions, please post your issues on the board, We will ack you as soon as we can.Thanks.

friendly api doc at : <https://apidocs.jbex.com>

## bots
### 1. Jubi History
export history within specified time range, the exported file is  /tmp/jubi-history.xlsx

#### command
```shell
cd sdk/python/traders
cp config/sample.json config/config.json
python jubi_history.py
```
#### config
in sdk/python/traders/jubi_history.py
```
1. year, month, day
start date
2. days
time span, zero means to the latest
3. pair
token pair, e.g., "BTCUSDT"
4. secret, api_secret
apply from JUBI
5. proxy
https proxy, in case jubi api server was blocked by ISP, e.g. "https://127.0.0.1:1087"
```