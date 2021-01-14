#!/usr/bin/env python
"""
a simple api connector to fgt device
use fgtConnector function to create list with header and cookies mandatory for succesful login
"""
import requests

fgt = '172.25.254.129'
unpw = {'username':'adm-a035e82','secretkey': 'hier_password_rein'}
fgturl = 'https://' + fgt + '/logincheck'

def fgtConnector(fgturl, credentials):
	r = requests.post(fgturl, data = credentials, verify = False)
	init_cookies = r.cookies
	csrf_header = {}
	for  cookie in r.cookies:
		if cookie.name == "ccsrftoken":
			csrftoken = cookie.value[1:-1]
			csrf_header = {"X-CSRFTOKEN": csrftoken}
	login_info = [csrf_header, init_cookies]
	return 	login_info

def main():
	fgt_session = fgtConnector(fgturl, unpw)
	q = requests.get('https://' + fgt + '/api/v2/cmdb/system/interface', headers = fgt_session[0], cookies = fgt_session[1], verify = False)
	print(q)

if __name__ == '__main__':
	main()


#Todo:
# logout from fw in main after run 
