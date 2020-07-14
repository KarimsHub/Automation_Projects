# first example for schedule automation
# Don´t name the file schedule.py!!!!

import schedule
import time

def first_test():
    print('this one worked')

schedule.every(10).seconds.do(first_test)
#schedule.every().hour.do(first_test)
#schedule.every().day.at("10:30").do(first_test)
#schedule.every().monday.do(first_test)
#schedule.every().wednesday.at("13:15").do(first_test)
#schedule.every().minute.at(":17").do(first_test)

while True:
    schedule.run_pending()
    time.sleep(1)