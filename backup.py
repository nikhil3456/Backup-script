
import json
import os,sys
from datetime import datetime
with open('list.json') as data_file:    
    data = json.load(data_file)
command=sys.argv[1]
if command=='backup':
    for i in range(len(data)):
        os.system('cp ' + data[i][0] + ' ' + './' + data[i][1]) 
elif command=='restore':
    for i in range(len(data)):
        os.system('cp ' + './' + data[i][1] + ' ' + data[i][0]) 
elif command=='push':
    time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    os.system('git add -A')
    os.system('git commit -m "New file added on'+ time + '"')
    os.system('git push -u origin master')
else:
    print("Invalid argument")
