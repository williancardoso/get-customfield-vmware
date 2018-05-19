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

    print ("Starting to connect to ESXi ...")
    si = SmartConnect(host="localhost",port=8989,user="user",pwd="pass",sslContext=None)
    content = si.RetrieveContent()

    ### Criando customfield
    fd = si.content.customFieldsManager.AddFieldDefinition(name='regional', moType=vim.VirtualMachine)

    print("disconnecting to ESXi ...")
    connect.Disconnect(si)
    
