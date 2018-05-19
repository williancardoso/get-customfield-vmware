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

    fd = si.content.customFieldsManager.field
    for item in fd:
        if (item.name == "regional"):
            fd_key = item.key

    for child in content.rootFolder.childEntity:
        vmList = child.vmFolder.childEntity
        for vm in vmList:
            #print(vm.name)
            if (vm.name == 'DC0_H0_VM0'):
                #si.content.customFieldsManager.SetField(entity=vm, key=fd.key, value='spo')
                vm.setCustomValue(key=fd_key, value="spo")
    #print("disconnecting to ESXi ...")
    connect.Disconnect(si)
