import schedule
import time

def do_nothing():
    print("Siddharth Mehta")

schedule.every(10).seconds.do(do_nothing)
schedule.every().wednesday.at("1:00").do(do_nothing())

while 1:
    schedule.run_pending()
    time.sleep(1)
