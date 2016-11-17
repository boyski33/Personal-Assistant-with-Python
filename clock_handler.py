import datetime


class ClockHandler(object):
    def __init__(self):
        self.current_time = str(
            datetime.datetime.time(datetime.datetime.now())).split(':')

    def get_current_hour(self):
        return int(self.current_time[0])

    def get_current_minutes(self):
        return int(self.current_time[1])

    def get_current_seconds(self):
        return int(self.current_time[2].split('.')[0])
