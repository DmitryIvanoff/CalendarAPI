from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

from .api import *
from .app import *
from .base import *
from .cache import *
from .cors import *
from .database import *
from .docs import *
from .email import *
from .jwt import *
from .localization import *
from .installed_apps import *
from .logging import *
from .middleware import *
from .password import *
from .environment import *
