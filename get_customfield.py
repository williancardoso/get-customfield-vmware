#!/usr/bin/env python

from __future__ import print_function

from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
from pyVim import connect

import argparse
import atexit
import getpass
import ssl

if __name__ == "__main__":
    """demo/test code for the PyVmomi"""

    #print ("Starting to connect to ESXi ...")
    si = SmartConnect(host="localhost",port=8989,user="user",pwd="pass",sslContext=None)
    content = si.RetrieveContent()

    #fd = si.content.customFieldsManager.AddFieldDefinition(name='regional', moType=vim.VirtualMachine)
    #print(si.content.customFieldsManager)
    f = si.content.customFieldsManager.field
    #print(f)

    for child in content.rootFolder.childEntity:
        if hasattr(child, 'vmFolder'):
            datacenter = child
            vmFolder = datacenter.vmFolder
            vmList = vmFolder.childEntity
            for vm in vmList:
                for k, v in [(x.name, v.value) for x in f for v in vm.customValue if x.key == v.key]:
                    print("hostname:",vm.name,"-",k,"-",v)
    #print("disconnecting to ESXi ...")
    connect.Disconnect(si)
