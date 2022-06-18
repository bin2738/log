import os
from unicodedata import name

class Controller_file:
    """Создает файл логов"""
    def create(self):
        """создает файл"""
        with open("log.txt", "w+") as files:
            files.write("LOG_FILES \n")
    
    def write_logs(self, text:str):
        """запись логов"""
        try:
            with open("log.txt", "a+") as file:
                file.write(text + "\n")
        except:
            pass
    
    def delet_log_file(self):
        path = "log.txt"
        try:
            os.remove(path)
        except:
            pass


if __name__ == "__main__":
    pass
