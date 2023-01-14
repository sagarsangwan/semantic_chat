from .base_settings import *
if os.environ.get("MOD") == 'prod':
    from .prod_settings import *
else:
    from .local_settings import *
