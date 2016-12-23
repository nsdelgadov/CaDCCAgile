import json
import requests

from cadcc_agile.settings import GOOGLE_API_URL, GOOGLE_URL_SHORTEN_API

def google_url_shorten(url):
    req_url = GOOGLE_API_URL + GOOGLE_URL_SHORTEN_API
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(req_url, data=json.dumps(payload), headers=headers)
    resp = json.loads(r.text)
    return resp['id']
    
    

# Para ver las estadisticas
# https://developers.google.com/url-shortener/v1/url/get