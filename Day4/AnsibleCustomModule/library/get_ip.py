#!/usr/bin/python3

import subprocess as sp
from ansible.module_utils.basic import AnsibleModule

def get_IP():
    tempStr = sp.getoutput('ip addr show dev eth0')
    tokens = tempStr.split('\n')
    ipAddrLine = tokens[2]
    ipWithCIDR = ipAddrLine.split (' ')
    ip = ipWithCIDR[5].split('/')

    return ip[0]


def main():
    module = AnsibleModule(
        argument_spec=dict()
    )

    result = dict(
        IPAddress = get_IP()
    )

    module.exit_json(**result)

if __name__ == '__main__':
    main()
