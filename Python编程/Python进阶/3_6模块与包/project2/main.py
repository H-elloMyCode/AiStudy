import sys
import os

utils_path = os.path.join(os.path.dirname(__file__), 'utils')
sys.path.append(utils_path)

import my_utils
print(my_utils.PI)