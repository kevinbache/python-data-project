import os
from pathlib import Path

PACKAGE_ROOT_PATH = Path(os.path.dirname(os.path.realpath(__file__)))
COMPONENTS_PATH = PACKAGE_ROOT_PATH / 'components'

PROJECT_ROOT_PATH = PACKAGE_ROOT_PATH / '..'
DATA_PATH = PROJECT_ROOT_PATH / 'data'
TESTS_PATH = PROJECT_ROOT_PATH / 'test'
