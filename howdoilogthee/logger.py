
import os
import shutil
import logging
import logging.handlers

log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(lineno)s - %(funcName)s - %(levelname)s - %(message)s')


def init_logger(log_directory=None, name=None, verbose=False, delete_existing_log_files=False, max_bytes=100*1E6, backup_count=3):
    """
    Initialize the logger.  Call once from the application 'main'.

    :param log_directory: directory where the log files will be written.  Pass in None if no log files are desired.
    :param name: name of the module or application being logged
    :param verbose: sets the log levels to more verbose level
    :param delete_existing_log_files: True to delete all files in log directory

    # set max_bytes and backup_count both to 0 for one big file
    :param max_bytes: max log file size (0 for no limit)
    :param backup_count: number of log files in rotation (0 for one file)

    :return: an instance of the logger and a dict with the handlers (in case the user wants to change the levels)
    """

    log = logging.getLogger()  # we init the root logger so all child loggers inherit this functionality
    handlers = {}

    if log.hasHandlers():
        log.error('logger already initialized')
        return log

    if verbose:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setFormatter(log_formatter)
    if verbose:
        ch.setLevel(logging.INFO)
    else:
        ch.setLevel(logging.WARNING)
    log.addHandler(ch)
    handlers['console'] = ch

    # create file handler
    if log_directory is not None:
        if delete_existing_log_files:
            shutil.rmtree(log_directory, ignore_errors=True)
        os.makedirs(log_directory, exist_ok=True)
        fh_path = os.path.join(log_directory, '%s.log' % name)
        fh = logging.handlers.RotatingFileHandler(fh_path, maxBytes=max_bytes, backupCount=backup_count)
        fh.setFormatter(log_formatter)
        if verbose:
            fh.setLevel(logging.DEBUG)
        else:
            fh.setLevel(logging.INFO)
        log.addHandler(fh)
        handlers['file'] = fh
        log.info('log file path : "%s" ("%s")' % (fh_path, os.path.abspath(fh_path)))

    return log, handlers
