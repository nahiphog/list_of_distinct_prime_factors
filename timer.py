######################################################
###### [1] In general clock terms
######################################################
from datetime import datetime
start_time = datetime.now()

print(f"Elapsed time: \t  {datetime.now() - start_time}" )

######################################################
###### [2A] In seconds only
######################################################
import time
start_time = time.time()

print(f"Elapsed time: \t { time() - start_time }" )

######################################################
###### [2B] In proper time unit, especially when it can run for over a minute
######################################################
from humanfriendly import format_timespan
from time import time
start_time = time()

print(f"Elapsed time: \t { format_timespan( time() - start_time) }" )

######################################################
###### [3] Show current date and time
######################################################
from time import time, ctime
print( ctime(time()) ) #Output: Fri Apr 17 05:36:03 2020
