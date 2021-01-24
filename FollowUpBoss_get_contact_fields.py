
# Get All Follow Up Boss Contact Fields. Both Regular and  Custom 

import requests as r
import json

pid = input.get('fub_pid')

sys = 'Your-System'
sys_key = 'Your-System-Key'
auth = 'Basic YourAuthKey'

def get_fub(pid):
	furl = "https://api.followupboss.com/v1/people?id=" + str(pid)
	fields = '&fields=allCustom%2CallFields'
	url = furl + fields
	headers = {
	  'X-System': sys,
	  'X-System-Key': sys_key,
	  'Authorization': auth,
	  'Content-Type': 'application/json'
	}
	results = r.request("GET", url, headers=headers)
	data = results.json()	
	return data['people'][0]
	#return data['people'][0]['customPurchasePrice']

data = get_fub(pid)

return {
	'lastReceivedEmail': data['people'][0]['lastReceivedEmail'],
	'lastReceivedEmailId': data['people'][0]['lastReceivedEmailId'],
	'lastSentEmail': data['people'][0]['lastSentEmail'],
	'lastSentEmailId': data['people'][0]['lastSentEmailId'],
	'lastEmail': data['people'][0]['lastEmail'],
	'lastEmailId': data['people'][0]['lastEmailId'],
	'emailsReceived': data['people'][0]['emailsReceived'],
	'emailsSent': data['people'][0]['emailsSent'],
	'lastIncomingCall': data['people'][0]['lastIncomingCall'],
	'lastIncomingCallId': data['people'][0]['lastIncomingCallId'],
	'lastOutgoingCall': data['people'][0]['lastOutgoingCall'],
	'lastOutgoingCallId': data['people'][0]['lastOutgoingCallId'],
	'firstCall': data['people'][0]['firstCall'],
	'lastCall': data['people'][0]['lastCall'],
	'lastCallId': data['people'][0]['lastCallId'],
	'callsOutgoing': data['people'][0]['callsOutgoing'],
	'callsIncoming': data['people'][0]['callsIncoming'],
	'callsDuration': data['people'][0]['callsDuration'],
	'lastReceivedText': data['people'][0]['lastReceivedText'],
	'lastReceivedTextId': data['people'][0]['lastReceivedTextId'],
	'lastSentText': data['people'][0]['lastSentText'],
	'lastSentTextId': data['people'][0]['lastSentTextId'],
	'lastText': data['people'][0]['lastText'],
	'lastTextId': data['people'][0]['lastTextId'],
	'textsReceived': data['people'][0]['textsReceived'],
	'textsSent': data['people'][0]['textsSent'],
	'lastLeadActivity': data['people'][0]['lastLeadActivity'],
	'lastLeadActivityId': data['people'][0]['lastLeadActivityId'],
	'lastEmEventActivity': data['people'][0]['lastEmEventActivity'],
	'lastEmEventActivityId': data['people'][0]['lastEmEventActivityId'],
	'propertiesViewed': data['people'][0]['propertiesViewed'],
	'propertiesSaved': data['people'][0]['propertiesSaved'],
	'pagesViewed': data['people'][0]['pagesViewed'],
	'lastIdxVisit': data['people'][0]['lastIdxVisit'],
	'nextTask': data['people'][0]['nextTask'],
	'nextTaskHasTime': data['people'][0]['nextTaskHasTime'],
	'nextTaskName': data['people'][0]['nextTaskName'],
	'firstToClaimOffer': data['people'][0]['firstToClaimOffer'],
	'customDEAL': data['people'][0]['customDEAL'],
	'customINFO': data['people'][0]['customINFO'],
	'customASSIGNED': data['people'][0]['customASSIGNED'],
	'customAssignedDate': data['people'][0]['customAssignedDate'],
	'customAssignmentPrice': data['people'][0]['customAssignmentPrice'],
	'customBathrooms': data['people'][0]['customBathrooms'],
	'customBedrooms': data['people'][0]['customBedrooms'],
	'customCloseDate': data['people'][0]['customCloseDate'],
	'customClosedLost': data['people'][0]['customClosedLost'],
	'customCOEDays': data['people'][0]['customCOEDays'],
	'customCondition': data['people'][0]['customCondition'],
	'customEstAssignmentPrice': data['people'][0]['customEstAssignmentPrice'],
	'customEstimatedARV': data['people'][0]['customEstimatedARV'],
	'customEstimatedRepairs': data['people'][0]['customEstimatedRepairs'],
	'customHighRangeOffer': data['people'][0]['customHighRangeOffer'],
	'customInspectionPeriod': data['people'][0]['customInspectionPeriod'],
	'customLotSize': data['people'][0]['customLotSize'],
	'customLowRangeOffer': data['people'][0]['customLowRangeOffer'],
	'customMajorMarket': data['people'][0]['customMajorMarket'],
	'customMapsStreetView': data['people'][0]['customMapsStreetView'],
	'customPodioLink': data['people'][0]['customPodioLink'],
	'customPropstream': data['people'][0]['customPropstream'],
	'customPurchasePrice': data['people'][0]['customPurchasePrice'],
	'customSqft': data['people'][0]['customSqft'],
	'customStatus': data['people'][0]['customStatus'],
	'customTheirAskingPrice': data['people'][0]['customTheirAskingPrice'],
	'customTotalViewLink': data['people'][0]['customTotalViewLink'],
	'customUnderContractDate': data['people'][0]['customUnderContractDate'],
	'customZestimate': data['people'][0]['customZestimate'],
	'customZillowComps': data['people'][0]['customZillowComps'],
	'customZillowLink': data['people'][0]['customZillowLink']
}


