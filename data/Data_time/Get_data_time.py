import datetime 

class Get_data_time:    
    def get_data_timw(self)->str:
        dt = datetime.datetime.now()
        dt_str = dt.strftime("[ DATA: %d/%m/%y TIME: %H:%M:%S ]")
        return dt_str
    