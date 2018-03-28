import subprocess
import json


# output = subprocess.check_output('ssh -p 29418 Sree@VTLW001L gerrit query --patch-sets  --comments --format=JSON status:open project:myfirstproject', shell=True)
# output = subprocess.check_output('ssh -p 29418 vutuksre@192.168.2.182 gerrit query --patch-sets  --comments --format=JSON status:open project:audio', shell=True)
output = subprocess.check_output('ssh -p 29418 vutuksre@192.168.2.182 gerrit query --patch-sets --comments --format=JSON status:open branch:audio-vtech.lnx.1.0-dev  NOT label:Code-Review =1', shell=True)
with open("final_2.json", "w") as fb:
	fb.write(output)

def json_parser(jfile):
    with open(jfile,"r") as json_data:
        rf=json_data.readlines()
    for obj in rf[:-1]:
    	output = dict()
        jdata = json.loads(obj)
        # prj_name = jdata['project']
        # branch_name = jdata['branch']
        # ow_name = jdata["owner"]["name"]
        output['prj_name']=jdata['project']
        output["branch_name"] = jdata['branch']
        output["chng_ow_name"] = jdata["owner"]["name"]
        rvr_name = None
        rvr_rate = None
    	for val in jdata["comments"]:
			if val['message'].find("Code-Review")>=0:
				rvr_name = val['reviewer']['name']
				rvr_rate = int(val["message"].split('+')[1][0])

			if rvr_name:
				# op = ow_name, rvr_name, rvr_rate
				output['rvr_name']=rvr_name
				output['rvr_rate']=rvr_rate
				print(output)
				# yield output
    	# break
        # print obj
        
json_parser("final_2.json")