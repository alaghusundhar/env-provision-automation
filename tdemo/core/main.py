# -*- coding: utf-8 -*-


""" Sample Troposphere to CloudFormation Demo project """


import sys
import importlib
import argparse

from tdemo.core import core


def _parse_args():
    ''' Following are the usage options:
    tdemo [--generate <STACK_MODULE>]
    tdemo [--create <STACK_MODULE> <STACK_NAME>]
    tdemo [--update <STACK_MODULE> <STACK_NAME>]
    tdemo [--delete <STACK_NAME>]
    '''
    parser = argparse.ArgumentParser(
        prog='python main.py',
        usage='%(prog)s [options]',
        description='Sample Troposphere to CloudFormation Demo project.'
    )
    parser.add_argument(
        '--generate',
        type=str,
        nargs=1,
        metavar=("<STACK_MODULE>"),
        help='Generates a JSON CFN template from stack.'
    )
    parser.add_argument(
        '--create',
        type=str,
        nargs=2,
        metavar=("<STACK_MODULE>", "<STACK_NAME>"),
        help='Creates a stack.'
    )
    parser.add_argument(
        '--update',
        type=str,
        nargs=2,
        metavar=("<STACK_MODULE>", "<STACK_NAME>"),
        help='Updats a stack.'
    )
    parser.add_argument(
        '--delete',
        type=str,
        nargs=1,
        metavar=("<STACK_NAME>"),
        help='Deletes a stack.'
    )
    return parser


def main():
    """ Control management to generate templates and create, update and
    delete AWS Stack of resources from these templates.

    It is designed such that there can be many stacks represented as
    python modules that generate a cloudformation template. Through this
    you can control and test any stack by providing its name (or module name)
    as input.

    The purpose for this is to be efficient in managing many stacks.
    """
    parser = _parse_args()
    args = vars(parser.parse_args())
    if args['generate']:
        module_name = args['generate'][0]
        module_stack = importlib.import_module(module_name)
        template = module_stack.generate_template()
    elif args['create']:
        module_name = args['create'][0]
        stack_name = args['create'][1]
        module_stack = importlib.import_module(module_name)
        template = module_stack.generate_template()
        core.create_stack(stack_name, template)
    elif args['update']:
        module_name = args['update'][0]
        stack_name = args['update'][1]
        module_stack = importlib.import_module(module_name)
        template = module_stack.generate_template()
        core.update_stack(stack_name, template)
    elif args['delete']:
        stack_name = args['delete'][0]
        core.delete_stack(stack_name)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
