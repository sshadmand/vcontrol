import json
import requests

class RegisterMachineC:
    def register_machine(self, args, daemon):
        """
        use default or supply credentials
        use generic driver from docker-machine
        note that they will be sent to the vcontrol daemon
        """
        payload = {}
        payload['machine'] = args.machine
        payload['ip'] = args.ip
        payload['password'] = args.password
        r = requests.post(daemon+"/register_machine", data=json.dumps(payload))
        return r.text
