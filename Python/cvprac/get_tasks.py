from cvprac import cvp_client as cvp_client
import requests
import os

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cvp1 = "192.168.0.5"
# For an on-prem production environemt, you would list two more CVP nodes
# cvp2 = ""
# cvp3 = ""
cvp_user = "arista"
cvp_pw = "arista6ycd"

client = cvp_client.CvpClient()

# If you had an on-prem production environment, you would list all cvp nodes instead of just cvp1
# client.connect([cvp1, cvp2, cvp3], cvp_user, cvp_pw)
client.connect([cvp1], cvp_user, cvp_pw)

tasks = client.api.get_tasks_by_status('Pending')

for task in tasks:
    taskId = task['workOrderId']
    hostname = task['workOrderDetails']['netElementHostName']
    print(f"{taskId} for {hostname}")
    client.api.execute_task(taskId)