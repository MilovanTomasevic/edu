from decouple import config
from .base import *
# you need to set "myproject = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
if config('EDU_SETTINGS') == 'prod':
   from .prod import *
else:
   from .dev import *