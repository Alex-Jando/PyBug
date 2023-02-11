import urllib.parse
import urllib3
from html.parser import HTMLParser

from .colors import Color

class HTMLLinkParser(HTMLParser):

    links = []

    def handle_starttag(self, tag: str, attrs: list):

        if tag == 'a' and attrs[0][0] == 'href' and attrs[0][1].startswith('/url'):

            self.links.append(attrs[0][1].split('=')[1].split('&')[0].strip('/'))

def search(query: str):

    query = f'https://www.google.com/search?q={urllib.parse.quote_plus(query)}'

    try:

        print(Color(0, 255, 0) + '[PYBUG INFO] Searching for ressources related to your error...')

        query = urllib3.PoolManager().request('GET', query)

        if str(query.status)[0] != '2':

            print(Color(255, 255, 0) + '[PYBUG WARNING] Failed to find any ressources related to your error due to non 200 HTTP response!')

            return []

        query_html = query.data.decode('UTF-8', 'ignore')

        query_parser = HTMLLinkParser()

        query_parser.feed(query_html)

        query_parser.links = query_parser.links[:-2]

        if query_parser.links:

            return query_parser.links

        else:

            print(Color(255, 255, 0) + '[PYBUG WARNING] Failed to find any ressources related to your error!')

            return []

    except:

        print(Color(255, 0, 0) + '[PYBUG ERROR] Failed to connect search any ressources related to your error! This is most likely because your are not connected to any internet!')

        return []