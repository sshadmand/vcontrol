import requests

class DeployCommandC:
    def deploy(self, args, daemon):
        files = {'myfile': open(args.path, 'rb')}
        # !! TODO how do files work with swagger?
        r = requests.post(daemon+"/deploy_template/"+args.machine, files=files)
        return r.text
