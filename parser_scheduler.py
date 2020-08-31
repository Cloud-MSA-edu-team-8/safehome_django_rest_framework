from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import pytz

import parser as pr

sched = BlockingScheduler()
local_tz = pytz.timezone('Asia/Seoul')

@sched.scheduled_job('interval', minutes=60*6) # 6시간
def timed_job():
    print('This job is run every one minutes.')

    pr.del_save_data() # news update

sched.start()