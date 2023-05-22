from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_strings_list = parse.parse_qsl(url_components.query)
        dic = dict(query_strings_list)
        country = dic.get("capital")
        print(capital)

        if country:
            url = f"https://restcountries.com/v3.1/name/{capital}"
            print(url)
            res = requests.get(url)
            data = res.json()
            capital = data[0]["name"]["common"]
            response = f"The country of {capital} is {country}."
        else:
            response = "capital parameter is missing."

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

        return
