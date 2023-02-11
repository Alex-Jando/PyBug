from .colors import Color
from .search import search

def search_exception(exception: Exception):

    exception_type = str(exception.__class__).split('\'')[1]

    query = f'Python - {exception_type}({exception})'

    links = search(query)

    print(Color(0, 255, 0) + '[PYBUG INFO] Successfully found the following links related to your error.')

    [print(Color(0, 150, 255) + link) for link in links]

def error(exception: Exception):

    print(Color(255, 0, 0) + f'[ERROR] {exception}')

    search_exception(exception)