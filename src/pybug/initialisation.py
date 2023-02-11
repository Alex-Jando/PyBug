import os
import sys

from .errors import error
from .colors import Color

FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), os.path.basename(sys.argv[0]))

def init(file: str, debug: bool = True):

    if not os.path.basename(file) == os.path.basename(__file__):

        with open(FILE_PATH, 'rb') as f:

            try:

                exec(f.read())

            except Exception as e:

                if debug:

                    error(e)

                else:

                    print(Color(255, 0, 0) + f'[ERROR] {e}')

        sys.exit()

    else:
        
        pass