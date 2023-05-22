from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_strings_list = parse.parse_qsl(url_components.query)
        dic = dict(query_strings_list)
        country = dic.get("country")
        print(country)

        if country:
            url = f"https://restcountries.com/v3.1/name/{country}"
            print(url)
            res = requests.get(url)
            print(res)
            data = res.json()
            capital = data[0]["capital"][0]
            response = f"The capital of {country} is {capital}."
        else:
            response = "Country parameter is missing."

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

        return
