#Check what vm is running 

import subprocess
cmd = "prlctl list -a | grep running"
ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
output = ps.communicate()[0]
If ( output is not null):
 print ("there are some vm running")
else:
 print ("no one is running")
