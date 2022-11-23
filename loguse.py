from MyLog.logfun import logger_config
import datetime
logger=logger_config(r"C:\Users\djc\Documents\GitHub\Log\logpathj",
                                 "mylog.log",
                                 "dataSerizer")
e="xasdada"
logger.info(e + " " + str("") + " " + str(datetime.time))
logger.info(e + " " + str("") + " " + str(datetime.time))
logger.critical(' loggging critical message')
