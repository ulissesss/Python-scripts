import subprocess
cmd = "prlctl list -a | grep running"
ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
output = ps.communicate()[0]
print(output)

#prlctl start f83e88ba-d717-4b6c-bb80-92bec6d1bd58
