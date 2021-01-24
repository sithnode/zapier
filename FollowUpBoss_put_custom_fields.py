import requests

# Post Field Values to Custom Fields from your application

person_id = input.get('fub_pid') # input('Enter Follow Up Boss PersionID: ')

sys = 'Your-System'
sys_key = 'Your-System-Key'
auth = 'Basic YourAuthKey'
people_url = "https://api.followupboss.com/v1/people/"+str(person_id)

headers = {
  'X-System': sys,
  'X-System-Key': sys_key,
  'Authorization': auth,
  'Content-Type': 'application/json'
}

payload = {
    'customCOEDays' : input.get('customCOEDays'),
    'customInspectionPeriod' : input.get('customInspectionPeriod'),
    'customEstAssignmentPrice' : input.get('customEstAssignmentPrice'),
    'customAssignmentPrice' : input.get('customAssignmentPrice'),
    'customPurchasePrice' : input.get('customPurchasePrice'),
    'customUnderContractDate' : input.get('customUnderContractDate'),
    'customEstimatedRepairs' : input.get('customEstimatedRepairs'),
    'customEstimatedARV' : input.get('customEstimatedARV'),
    'customCondition' : input.get('customCondition'),
    'customCloseDate' : input.get('customCloseDate')
    }

response = requests.request("PUT", people_url, headers=headers, json = payload)

print(response.text.encode('utf8'))
