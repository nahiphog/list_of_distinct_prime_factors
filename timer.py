######################################################
###### [1] In general clock terms.
######################################################
from datetime import datetime
startTime = datetime.now()

print(f"The total runtime of this script is {datetime.now() - startTime}.\n")

######################################################
###### [2] In seconds only
######################################################
import time
start_time = time.time()

print("This script took %s seconds to run." % (time.time() - start_time))
