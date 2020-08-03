import os,sys
import logging
from logging.handlers import TimedRotatingFileHandler

path = os.path.dirname(os.path.dirname(__file__))
log_path = os.path.join(path,"logs")

class Logger(object):
    def __init__(self,logger_name="logs"):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        self.log_file_name = "logs.txt"
        self.backup_count = 10 #最多存放日志数量
        #日志输入级别
        self.console_output_level = "WARNING"
        self.file_output_level = "DEBUG"
        #日志输出格式
        self.formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s")

    def get_logger(self):
        """
        在logger中添加日志句柄并返回，如果已有logger句柄直接返回
        @return: logger
        """
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            #每天只创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(log_path,self.log_file_name),when="D",
                                                    interval=1,backupCount=self.backup_count,delay=True,
                                                    encoding="utf-8")
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger

logger = Logger().get_logger()