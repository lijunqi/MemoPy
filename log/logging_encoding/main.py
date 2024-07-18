import logging
import sys

# 设置logging模块的默认编码为UTF-8
logging.basicConfig(stream=sys.stdout, level=logging.INFO, encoding='utf-8')

# 创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)

# 创建一个输出到控制台的handler
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

# 将handler添加到logger
logger.addHandler(stream_handler)

# 使用logger记录日志
a = u'\u2502'
logger.info(a)
logger.info('这是一条使用UTF-8编码的日志记录')
