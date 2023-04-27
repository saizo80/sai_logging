# sai logging

a custom logging module used for reporting cron activity.

## about

this logging module will act as a front for the python `logging` package.

this will simultaneously log to a passed file (or none if a file isn't passed) and a stringio stream
to be retrieved later.

## installation

if you have added git.saizo.gay to your pip index for either user or global (see package [instructions](https://git.saizo.gay/saizo/-/packages/pypi/sai-logging/)):

```bash
pip install sai_logging
```

if you have not then you will need to add it as an extra index in the install statement:

```bash
pip install --extra-index-url https://git.saizo.gay/api/packages/saizo/pypi/simple/ sai_logging
```

## use

```python
import sai_logging as logging

# all arguments are optional
log = logging.Logger(
    log_file = "/path/to/logfile",
    color = True,
    stream_level = logging.INFO,
    file_level = logging.DEBUG,
    log_stdout = True,
    stdout_level = logging.INFO,
)

log.debug('debug level log')
log.info('info level log')
log.warning('warning level log')
log.error('error level log')
log.critical('critical level log')

print(log.get_log())
```
