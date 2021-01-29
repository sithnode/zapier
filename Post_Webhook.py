import requests as r

#url = "https://secure.globiflow.com/catch/<YOUR URL>"  #To Podio Webhook
url = "https://hooks.zapier.com/hooks/catch/<YOUR URL>" #To Zapier Webhook

payload = {\
	"From":"18881234567",\
	"NumSegments ":"1",\
	"Body":"Yes & No thank you",\
	"To":"19515822233",\
	"ApiVersion":"IMaa23c836-17b1-4290-ac11-161968cfa244",\
	"Price":"0.015",\
	"Short":"",\
	"folder":"Inbox",\
	"phone":"8001234567",\
	"action":"inbound_sms_post_url",\
	"campaign":""
	}

results=r.post(url,	json=payload)

print(results)
