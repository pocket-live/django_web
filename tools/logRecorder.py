#coding=UTF8
'''
日志封装
'''
import logging
import logging.handlers
import colorlog
import sys, os,time
# 日志级别类型
levelMap = {'DEBUG':logging.DEBUG,
            'INFO':logging.INFO,
            'WARNING':logging.WARNING,
            'ERROR':logging.ERROR,
            'CRITICAL':logging.CRITICAL
            }

log_colors_config = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red'
}

class LogRecorder(object):
    def __init__(self,filename = None,format = '[%(asctime)s] (%(filename)s/%(funcName)s/%(lineno)d/%(levelname)s):\n%(message)s', name = 'LogRecorder',level = 'INFO',propagate = False,is_show_line = True):
        '''
        :param filename: 日志存储路径
        :param format: 日志格式
        :param name: 日志名称
        :param level: 日志等级
        :param propagate: 是否开启父子日志记录器的向上传播功能 若开启，子记录器会获得父记录器的全部Handler，需注意重复添加Handler以免产生重复日志
        '''
        if filename == None:
            log_path = os.path.dirname(__file__) + '/logs'
            if not os.path.exists(log_path): os.mkdir(log_path)
            filename = '%s/%s%s.log' % (log_path,name,time.strftime('%Y-%m-%d'))
        self._log_format = logging.Formatter(format)
        self._log_name = name
        self._log_level = levelMap.get(level)

        self.logger = logging.getLogger(self._log_name)
        self.logger.setLevel(self._log_level)
        self.logger.propagate = propagate

        # 高危日志文件保存(可配合Ideolog插件(只支持后缀为.log)查看等级颜色)
        high_handler = logging.handlers.RotatingFileHandler(
            filename=filename,
            encoding='UTF-8',
            delay=False,
            maxBytes = 1024 * 1024 * 10, # 10MB
            backupCount = 5
            )
        high_handler.setFormatter(self._log_format)
        high_handler.setLevel(logging.WARNING)
        self.logger.addHandler(high_handler)

        # 一般日志(控制台/系统输出)
        sys_handler = logging.StreamHandler()
        color_format = '%(log_color)s' + format
        if is_show_line == False:
            color_format = '%(log_color)s' + '[%(asctime)s]:%(message)s'
        sys_handler.setFormatter(colorlog.ColoredFormatter(color_format,log_colors=log_colors_config))
        sys_handler.setLevel(self._log_level)
        self.logger.addHandler(sys_handler)

        # 基础配置
        logging.basicConfig(level=self._log_level,
                            format='[%(asctime)s.%(msecs)03d]: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            stream=sys.stdout)

    def debug(self, content):
        self.logger.debug(content)
    def info(self, content):
        self.logger.info(content)
    def warning(self, content):
        self.logger.warning(content)
    def error(self, content):
        self.logger.error(content)
    def critical(self, content):
        self.logger.critical(content)

if __name__=='__main__':
    logger = LogRecorder(level='WARNING')
    logger.debug("debug log")
    logger.info("info log")
    logger.warning("warning log")
    logger.error("error log")
    logger.critical("critical log system")