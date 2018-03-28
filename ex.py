data = [{
	u'timestamp': 1518610334, 
	u'message': u'Uploaded patch set 1.', 
	u'reviewer': 
		{
			u'username': u'Sree', 
			u'name': u'Sreekanth', 
			u'email': u'sreekanth.vutukuru@votarytech.com'
		}
}, 
{
	u'timestamp': 1518610434, 
	u'message': u'Abandoned', 
	u'reviewer': 
		{
			u'username': u'Sree', 
			u'name': u'Sreekanth', 
			u'email': u'sreekanth.vutukuru@votarytech.com'
		}
}, 
{
	u'timestamp': 1518610445, 
	u'message': u'Restored', 
	u'reviewer': 
		{
			u'username': u'Sree', 
			u'name': u'Sreekanth', 
			u'email': u'sreekanth.vutukuru@votarytech.com'
		}
}, 
{
	u'timestamp': 1518670840, 
	u'message': u'Patch Set 1: Code-Review+1', 
	u'reviewer': 
		{
			u'username': u'Sree', 
			u'name': u'Sreekanth', 
			u'email': u'sreekanth.vutukuru@votarytech.com'
		}
}, 
{
	u'timestamp': 1518671067, 
	u'message': u'Patch Set 1: Code-Review+1', 
	u'reviewer': 
		{
			u'username': u'vinay', 
			u'name': u'Vinay', 
			u'email': u'vinay.jeedipally@votarytech.com'
		}
}
]

for val in data:
	if val['message'].find("Code-Review")>=0:
		rvr_name = val['reviewer']['name']
		rvr_rate = int(val["message"].split('+')[1])
		print(rvr_rate)
		print(rvr_name)