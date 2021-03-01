import requests
import os
import urllib3
from requests.auth import HTTPBasicAuth 

urllib3.disable_warnings(urllib3.exceptions.insecureRequestWarning)
server=os.getenv('VCENTER_HOST')
username=os.getenv('VCENTER_USERNAME')
password=os.getenv('VCENTER_PASSWORD')
print(server,username,password)

ENDPOINT_SESSION= f'http://{server}/rest/com/vmware/cis/session'

def login_vmware():
 url=ENDPOINT_SESSION
 response=request.post(url,requests.auth.auth(username,password),verify=False)
 if response.status_code==200;
  content= response.json()
  token = content['value']
  return token



def lis_vms(token):
    
 url=f'https://{server}/rest/vcenter/vm'
 headers={
    'Content-Type':'application/json',
    'vmware-api-session-id':token
 }
 response = request.get(url,headers=headers,verify=False)
 if response.status_code ==200:
    vms=[]
   content = response.json()
   for vm in content['value']:
       temp_dict={}
       vm_id=vm['vm']
       vm_name=vm['name']
       vm_power_state=vm['power_state']
       vm_cpu_count = vm['cpu_count']
       vm_memory_size_mb= vm['memory_size_Mib']
       print(f'ID:{vm_id} -Name:{vm_name} -State:{vm_power_state} -CPU:{vm_cpu_count} -Memory:{vm_memory_size_mb}')
       temp_dict['vm_id']=vm_id
       temp_dict ['vm_name']=vm_name
       temp_dict ['vm_power_state']=vm_power_state 
       temp_dict ['vm_cpu_count']=vm_cpu_count
       temp_dict ['vm_memory_size_mb']=vm_memory_size_mb
       vms.append(temp_dict)
    print(vms)   

token=login_vmware()
#vms=list_vms(token)



