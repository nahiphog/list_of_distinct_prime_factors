######################################################
###### [1] In general clock terms
######################################################
from datetime import datetime
start_time = datetime.now()

print(f"The total runtime of this script is {datetime.now() - start_time}.\n")

######################################################
###### [2A] In seconds only
######################################################
import time
start_time = time.time()

print("This script took %s seconds to run." % (time.time() - start_time))

######################################################
###### [2B] In proper time unit, especially when it can run for over a minute
######################################################
from humanfriendly import format_timespan
from time import time
start_time = time()

print(f"This script took { format_timespan( time() - start_time) } to run." )
