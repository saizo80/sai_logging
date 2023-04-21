# sai logging

a custom logging module used for reporting cron activity.

## about

this logging module will act as a front for the python `logging` package.

this will simultaneously log to a passed file (or none if a file isn't passed) and a stringio stream
to be retrieved later.

## installation

`pip install git+https://git.saizo.gay/saizo/sai_logging.git`

## use

```python
import sai_logging as log

logging = log.Logger(
    log_file_name='/path/to/logfile',
    log_level=log.DEBUG,
)

logging.debug('debug level log')
logging.info('info level log')
logging.warning('warning level log')
logging.error('error level log')
logging.critical('critical level log')

print(logging.get_log())
```
