import json
from datetime import datetime

op = dict()
with open("final_2.json", "r") as fobj:
	rf = fobj.readlines()
#	print(rf)
	jdata = json.loads(rf[0])
#	print(jdata)
	# project, No of days, CommidId, change Request, Owner, Name of Branch
	op['project'] = jdata["project"]
	# op["CommitId"] = jdata["id"]
	op["Gr_Number"] = jdata["number"]
	op["Owner"] = jdata["owner"]["name"]
	op["branch_name"] = jdata["branch"]
	def calc_days():
		nw = datetime.now()
		updated = datetime.fromtimestamp(jdata["lastUpdated"])
		days = abs((updated - nw).days)
		return days
	op["No_of_days"] = calc_days()
	
print(op)

