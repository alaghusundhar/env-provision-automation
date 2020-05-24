Troposphere demo
================
Sample Troposphere to CloudFormation Demo project.


Installation
============
The following commands will install the demo project into the executable
path with the script named as "tdemo". It also installs all its dependencies
which are boto3, troposphere, nose, mock and argparse.

```bash
>> git clone https://github.com/dsouzajude/troposphere-demo.git
>> cd troposphere-demo
>> python setup.py install
>> tdemo
```


What this demo does?
====================
This is a simple [Troposphere](https://github.com/cloudtools/troposphere) demo
that generates an AWS CloudFormation template similar to [worksample.cfn.template](https://github.com/dsouzajude/troposphere-demo/blob/master/worksample.cfn.template).
Through this you can also create, update and delete stacks from the generated
template.


Intention
=========
The intention behind this demo is to propose my structure for organizing troposphere
templated files such that it can be made easy to manage more efficiently across
many stacks. Each stack can be implemented as a python module that contains the
the necessary troposphere template files to generate the CloudFormation template.

Each stack can then be managed by the [controller](https://github.com/dsouzajude/troposphere-demo/blob/master/tdemo/core/main.py)
that would take as input the stack module name and generate the template from it.
Further on, from this template the stack can be created, updated or deleted via
the same controller.


Demo
====
For the demo, you need to set your aws credentials at the "\~/.aws/credentials"
location and necessary default aws values at "\~/.aws/config". You can also
set them as environment variables when running the demo. For more details
see [here](http://boto3.readthedocs.io/en/latest/guide/configuration.html).

Usage:
------

```bash
>> tdemo --help

usage: python main.py [options]

Sample Troposphere to CloudFormation Demo project.

optional arguments:
  -h, --help            show this help message and exit
  --generate <STACK_MODULE>
                        Generates a JSON CFN template from stack.
  --create <STACK_MODULE> <STACK_NAME>
                        Creates a stack.
  --update <STACK_MODULE> <STACK_NAME>
                        Updats a stack.
  --delete <STACK_NAME>
                        Deletes a stack.
```

Generating the sample template for the sample "stack_dev" stack:
----------------------------------------------------------------
Note "stack_dev" stack is represented as a python module.

```bash
>> tdemo --generate tdemo.stack_dev

```

Outputs the [worksample.cfn.template](https://github.com/dsouzajude/troposphere-demo/blob/master/worksample.cfn.template)
template.

Creating the stack:
-------------------
Creates a stack on AWS with the name Dev. Prior to creating, it first generates
the CloudFormation template from the troposphere configuration and then creates
the stack.

```bash
>> tdemo --create tdemo.stack_dev Dev
```

Updating the stack:
-------------------
Updates the stack that was created. Again, it generates the CloudFormation
template from the troposphere configuration and then updates the stack with the
updated template.

```bash
>> tdemo --update tdemo.stack_dev Dev
```


Delete stack:
-------------
Deletes a stack that was created.

```bash
>> tdemo --delete Dev
```


Running tests
=============
`cd` into the project home directory and run the tests via nose.

```
>> cd troposphere-demo
>> nosetests -svx tests_dev
```
