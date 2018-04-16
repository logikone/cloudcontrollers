import logging
import os
from inspect import cleandoc

import click
import colorlog

banner = cleandoc("""
  ____ _                 _    ____            _             _ _
 / ___| | ___  _   _  __| |  / ___|___  _ __ | |_ _ __ ___ | | | ___ _ __ ___
| |   | |/ _ \| | | |/ _` | | |   / _ \| '_ \| __| '__/ _ \| | |/ _ \ '__/ __|
| |___| | (_) | |_| | (_| | | |__| (_) | | | | |_| | | (_) | | |  __/ |  \__ \\
 \____|_|\___/ \__,_|\__,_|  \____\___/|_| |_|\__|_|  \___/|_|_|\___|_|  |___/        
""")


def get_log_level():
    env_log_level: str = os.environ.get('LOG_LEVEL', 'INFO')

    if env_log_level.upper() is 'INFO':
        log_level = logging.INFO
    elif env_log_level.upper() in ('WARN', 'WARNING'):
        log_level = logging.WARNING
    elif env_log_level.upper() == 'ERROR':
        log_level = logging.ERROR
    elif env_log_level.upper() == 'DEBUG':
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    return log_level


logger = logging.getLogger('cloudcontrollers')
logger.setLevel(get_log_level())

log_format = (
    f'{click.style("%(asctime)s",dim=True)} %(log_color)s%(levelname)8s%(reset)s '
    f'{click.style("%(process)d", fg="magenta")} {click.style("---", dim=True)} '
    f'{click.style("[%(threadName)20s]", dim=True)} {click.style("%(name)s", fg="cyan")} '
    f'{click.style(":", dim=True)} %(message)s')

formatter = colorlog.ColoredFormatter(log_format)

handler = colorlog.StreamHandler()
handler.setLevel(get_log_level())
handler.setFormatter(formatter)

logger.addHandler(handler)
