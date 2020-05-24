##  Script : AWS Environment Provisioning Using Python Troposphere
##  Author : Alagusundaram Nithyananndam
##  Role   : Senior DevOps Engineer


from troposphere import Ref, Template, Retain, Parameter
import troposphere.ec2 as ec2
from troposphere.ec2 import VPC , Tags, Subnet, InternetGateway, VPCGatewayAttachment, RouteTable, NetworkAcl
import logging
import argparse
import os

t = Template()
t.set_version()
environments=["dev","staging","production"]

LOGGER=logging.getLogger()
logging.basicConfig(format="[%(asctime)s %(levelname)s: %(message)s ",level="INFO")

parser=argparse.ArgumentParser(description="Environment Scaling Using Python Troposphere")
parser.add_argument("-e","--environment",type=str, required=True, choices=['development','integration','production'])
args=parser.parse_args()

repolocation=os.path.dirname(os.path.realpath(__file__))
configurationpath="{}/environment_profiles/{}.yaml".format(repolocation,args.environment)


print(repolocation)
print(configurationpath)

## Adding New VPC to Environment

t.add_resource(VPC(
    "VPC",
    EnableDnsSupport="true",
    CidrBlock="10.100.0.0/16",
    EnableDnsHostnames="true",
    DeletionPolicy="Retain",
    Tags=Tags(
        Application=Ref("AWS::StackName"),
        Network="{0} Spot Instance VPC",
        Name="alagu-test-vpc"
    )
))

## Adding Subnet

t.add_resource(
    Subnet(
        'Subnet',
        CidrBlock='10.0.0.0/24',
        VpcId=Ref(VPC),
        Tags=Tags(
            Application=Ref("AWS::StackName"))))

## Adding Internet Gateway

#internetGateway = t.add_resource(
#    InternetGateway(
#        'InternetGateway',
#        Tags=Tags(
#            Application="AWS::StackName")))

## Mapping Gateway to A VPC

#gatewayAttachment = t.add_resource(
#    VPCGatewayAttachment(
#        'AttachGateway',
#        VpcId=Ref(VPC),
#        InternetGatewayId=Ref(internetGateway)))

## Adding Routing Table

#routeTable = t.add_resource(
#    RouteTable(
#        'RouteTable',
#        VpcId=Ref(VPC),
#        Tags=Tags(
#            Application="AWS::StackName")))

#networkAcl = t.add_resource(
#    NetworkAcl(
#        'NetworkAcl',
#        VpcId=Ref(VPC),
#        Tags=Tags(
#            Application="AWS::StackName"),
#    ))

#instanceType_param = t.add_parameter(Parameter(
#    'InstanceType',
#    Type='String',
#    Description='EC2 instance type',
#    Default='t1.micro',
#    AllowedValues=[
#        't1.micro',
#        't2.micro', 't2.small', 't2.medium'],
#    ConstraintDescription='must be a valid EC2 instance type.',
#))

for env in environments:
    instance = ec2.Instance(env,DeletionPolicy=Retain)
    instance.ImageId = "ami-ed6bec86"
    instance.InstanceType = "t1.micro"
    t.add_resource(instance)

print(t.to_json())
#print(t.to_yaml())