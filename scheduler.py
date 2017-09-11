import schedule
import time
import CricketScore

#schedule.CancelJob

def job():
	execfile("CricketScore.py")


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)