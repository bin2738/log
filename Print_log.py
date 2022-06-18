import os
from data.Data_ifo import Data_info
from data.Data_time.Get_data_time import Get_data_time
from controller.Files.Controller_file import Controller_file


class Print_log:
    def __init__(self) -> None:
        self.__data_info = Data_info()
        self.__get_data_time = Get_data_time()
        self.__controller_file = Controller_file()
        
        self.__controller_file.create()

    def write_log_info(self, text):
        """записать лог инфо"""
        log = "{}--{} {}".format(self.__get_data_time.get_data_timw(), self.__data_info.INFO , text)
        self.__controller_file.write_logs(log)
    
    def write_log_error(self, text):
        """записать лог ошибки"""
        log = "{}--{} {}".format(self.__get_data_time.get_data_timw(), self.__data_info.ERROR , text)
        self.__controller_file.write_logs(log)

    def write_log_warning(self, text):
        """записать лог опасность"""
        log = "{}--{} {}".format(self.__get_data_time.get_data_timw(), self.__data_info.WARNING , text)
        self.__controller_file.write_logs(log)

    def write_log_debug(self, text):
        """записать лог дебаг"""
        log = "{}--{} {}".format(self.__get_data_time.get_data_timw(), self.__data_info.DEBUG , text)
        self.__controller_file.write_logs(log)


if __name__ == "__main__":
    Print_log().write_log_info("testkfldkfldkfsl123")