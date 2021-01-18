import requests
import json


class ZabbixTools:
    url = "http://172.28.13.140/api_jsonrpc.php"
    headers = {'Content-Type': 'application/json'}

    def request_api(self, data):
        request_zabbix = requests.request('GET', self.url, headers=self.headers, data=json.dumps(data), verify=False)
        return request_zabbix

    ######获得token######
    def user_login(self):
        zabbix_token = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": "Admin",
                "password": "zabbix"
            },
            "id": 1
            # "auth":
        }
        try:
            request_auth = requests.request('GET', self.url, headers=self.headers, data=json.dumps(zabbix_token),
                                            verify=False)
            request_auth_json = request_auth.json()
            auth = request_auth_json['result']
        except Exception as e:
            return '0'
        return auth

    ######获取主机列表######
    def get_hosts(self):
        data = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": [
                    "host"
                ],
                "selectInterfaces":
                    ["ip"],

                "selectGroups": ['name']
            },
            "id": 2,
            "auth": self.user_login()
        }
        request_host = self.request_api(data)
        return json.loads(request_host.content)['result']

    ###创建group###
    def create_host_group(self):
        data = {
            "jsonrpc": "2.0",
            "method": "hostgroup.create",
            "params": {
                "name": "xxx--11"
            },
            "auth": self.user_login(),
            "id": 1
        }
        create_host_groups = self.request_api(data)
        return create_host_groups.json()

    ###更新host信息####
    def host_update(self):
        data = {
            "jsonrpc": "2.0",
            "method": "host.update",
            "params": {
                "hostid": "10432",
                "groups": [{"groupid": "95"}]
                # "status": 0
            },
            "auth": self.user_login(),
            "id": 1
        }
        host_updates = self.request_api(data)
        return host_updates.json()


a = ZabbixTools()
ip_key_list = []
group_values_list = []
for group_name_ip_dict in a.get_hosts():
    key = dict(group_name_ip_dict).get('interfaces')[0].get('ip')
    ip_key_list.append(key)
    values = dict(group_name_ip_dict).get('groups')[0].get('name')
    group_values_list.append(values)
ip_group_list = dict(zip(ip_key_list, group_values_list))
print(ip_group_list)
ip_host = '10.109.207.7'
# for ip_hosts in ip_group_list:
# print(ip_hosts)
print(ip_group_list['172.28.13.175'])





https