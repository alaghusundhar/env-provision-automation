## Author : Alagusundaram Nithyanandam
## Role : Senior DevOps Engineer

import argparse
import logging
import os
import sys
import importlib
from templategenerator import ScalingActionTaker
import templategenerator as gen
sys.path.append(".")
LOGGER=logging.getLogger()
logging.basicConfig(format="[%(asctime)s] %(levelname)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    level="INFO")
formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")

actions = ["create","update","delete","generate"]
environment=["development","integration-1","integration-2","prod-1","prod-2"]

203 993 9908
def parse_args():

    parser = argparse.ArgumentParser(
        prog='python main.py',
        usage='%(prog)s [options]',
        description='Python Troposphere to CloudFormation Demo project.'
    )
    parser.add_argument(
        '--action',
        type=str,
        choices=actions,
        required=True,
        help='Actions to Perform'
    )
    parser.add_argument(
        '--env',
        type=str,
        choices=environment,
        required=True,
        help='Environment Name to Be Created'
    )
    parser.add_argument(
        '--capacity',
        type=str,
        required=False,
        default="default",
        help='Updates based on desired capacity.'
    )
    parser.add_argument(
        '--mode',
        type=str,
        required=False,
        choices=["local","jenkins"],
        help='Deployment Mode'
    )
    return parser

def main():

    parser = parse_args()
    script_path = os.path.dirname(os.path.realpath(__file__))
    yml_path = os.path.join(script_path, "capacity")
    args = vars(parser.parse_args())
    profile_path = "{}/capacity/{}/managed_stacks.yml".format(script_path, args["capacity"])
    configuration_path = "{}/capacity/{}/{}.yml".format(script_path, args["capacity"], args["env"])
#    module_stack = importlib.import_module()
    if args['action'] == "generate":
        module_name = args['generate'][0]
#        module_stack = importlib.import_module(module_name)
#        template = module_stack.generate_template()
        print ("generate")
    elif args['action'] == "create":
#x        template = module_stack.generate_template()
#        module_name = args['create'][0]
#        stack_name = args['create'][1]
        module_stack = importlib.import_module(args["env"])
        template = module_stack.generate_template()
#        core.create_stack(stack_name, template)
        print("Create")
        print(template)
        gen.ScalingActionTaker()
    elif args['action'] == "update":
        module_name = args['update'][0]
        stack_name = args['update'][1]
#        module_stack = importlib.import_module(module_name)
#        template = module_stack.generate_template()
#        core.update_stack(stack_name, template)
        print("update")
    elif args['action'] == "delete":
        stack_name = args['delete'][0]
        print("delete")
#        core.delete_stack(stack_name)
    else:
        parser.print_help()

#parse_args()
if __name__ == '__main__':
    main()