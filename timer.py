######################################################
###### [1] In general clock terms
######################################################
from datetime import datetime
start_time = datetime.now()

print(f"The total runtime of this script is {datetime.now() - start_time}.\n")

######################################################
###### [2] In seconds only
######################################################
import time
start_time = time.time()

print("This script took %s seconds to run." % (time.time() - start_time))
