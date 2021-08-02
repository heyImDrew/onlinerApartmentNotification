from datetime import datetime, timedelta


def datetime_differ(time_1, time_2):
    return (datetime.now() - time_1) > timedelta(time_2)
