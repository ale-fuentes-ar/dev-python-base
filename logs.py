#!/user/bin/env python3
"""
"""

import os
import logging
from logging import handlers


# TODO: convert setting logs in a function
# TODO: use lib, example 'logguru'
# set level 
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
# instance
log = logging.Logger("ale", log_level)
# level : dev, tqs, etc
# ch = logging.StreamHandler()
# ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "logs-file.log", 
    maxBytes=100, # indicating to use 10**6,
    backupCount=10
)
fh.setLevel(log_level)
# format: more information
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
# ch.setFormatter(fmt)
# target: set target
# log.addHandler(ch)
fh.setFormatter(fmt)
log.addHandler(fh)

"""
# logging : root logger
log.debug("Msg for dev")
log.info("Several msg")
log.warning("Avise but not error")
log.error("Erro bring for only one execution  ")
log.critical("Geral ERRO, e.x. DBA down")
"""

print("-" * 10)
try:
    1/0
except ZeroDivisionError as e:
    # print(f"[ERRO] has a error {str(e)}")
    log.error("Has a error %s", str(e))
    # stdout
    # stderr
    # python logs.py &2> /tmp/error.log
    
