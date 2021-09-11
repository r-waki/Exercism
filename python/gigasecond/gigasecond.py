from datetime import datetime, timedelta

def add(moment):
    gigasecond = timedelta(seconds=1000000000) 
    return moment + gigasecond
