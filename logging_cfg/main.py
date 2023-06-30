import logging, logging.config

# Set up logging
logging.config.fileConfig("log.ini")
loggerF = logging.getLogger('LogFront')
loggerB = logging.getLogger('LogBack')


# log something
loggerF.debug('Front Debug message')
loggerF.info('Front Info message')
loggerF.warning('Front Warning message')
loggerF.error('Front Error message')
loggerF.critical('Front Critical message')

print('============================')

loggerB.debug('Back Debug message')
loggerB.info('Back Info message')
loggerB.warning('Back Warning message')
loggerB.error('Back Error message')
loggerB.critical('Back Critical message')
