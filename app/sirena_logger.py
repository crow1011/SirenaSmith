import logging
import sirena_config

def get_logger():
    conf = sirena_config.get_conf()
    log_file = conf['logger']['log_path']
    logger = logging.getLogger(__name__)
    # set logging level
    if conf['logger']['level']=='debug':
        level = logging.DEBUG
    if conf['logger']['level']=='info':
        level = logging.INFO
    if conf['logger']['level']=='warning':
        level = logging.WARNING
    if conf['logger']['level']=='ERROR':
        level = logging.ERROR
    logger.setLevel(level)
    # create the logging file handler
    fh = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger