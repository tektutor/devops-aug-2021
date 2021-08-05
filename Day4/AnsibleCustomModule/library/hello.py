from ansible.module_utils.basic import AnsibleModule

def sayHello():
    return "Hello from Ansible Custom Module ..."

def main():
    module = AnsibleModule(
        argument_spec=dict()
    )

    result = dict(
        msg = sayHello()
    )

    module.exit_json(**result)

if __name__ == '__main__':
    main()
