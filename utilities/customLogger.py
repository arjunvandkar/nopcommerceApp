import inspect
import logging
#2023-04-10 09:03:30,408 :INFO : Test_001_Login :************ Test_001_Login ****************
class LogGen:
    @staticmethod
    def loggen():
        loggername = inspect.stack()[1][3] # for giving Test_001_Login test method name in log from where we are calling it
        logger = logging.getLogger(loggername)
        fileHandler = logging.FileHandler('C:/Users/sCs/PycharmProjects/nopcommerceApp/Logs/logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler) # filehandler object

        logger.setLevel(logging.INFO)
        return logger


