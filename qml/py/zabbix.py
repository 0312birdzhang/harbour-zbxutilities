from pyzabbix import ZabbixAPI, ZabbixAPIException
import sys
ZABBIX_SERVER = 'http://192.168.214.143/zabbix'
zapi = ZabbixAPI(ZABBIX_SERVER)
zapi.login('admin','zabbix')

def getHosts():
    hosts = zapi.host.get(selectInterfaces=["interfaceid"])
    if hosts:
        host_id = hosts[0]["hostid"]
        print("Found host id {0}".format(host_id))
        return "Found host id {0}".format(host_id)
