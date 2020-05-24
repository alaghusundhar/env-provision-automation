from troposphere import (
    Output,
    Join,
    Ref
)
from troposphere.ec2 import (
    DHCPOptions,
    VPCDHCPOptionsAssociation,
    VPC,
    VPCGatewayAttachment,
    InternetGateway,
    SecurityGroup
)

from . import template as t, tags


# VPC
vpc = t.add_resource(VPC(
    "VPC",
    CidrBlock="10.0.0.0/16",
    EnableDnsHostnames=True,
    EnableDnsSupport=True,
    InstanceTenancy="default",
    Tags=tags('ServiceVPC'),
))

# Internet Gateway
internet_gateway = t.add_resource(InternetGateway(
    "InternetGateway",
    Tags=tags('InternetGateway')
))

t.add_resource(VPCGatewayAttachment(
    "VpcGatewayAttachment",
    InternetGatewayId=Ref(internet_gateway),
    VpcId=Ref(vpc)
))


# VPC DHCP Options
dhcp_opts = t.add_resource(DHCPOptions(
    "DhcpOptions",
    DomainName=Join("", [Ref("AWS::Region"), ".compute.internal"]),
    DomainNameServers=[
        "AmazonProvidedDNS"
    ],
    Tags=tags('DhcpOptions')
))

dhcp_opts_assoc = t.add_resource(VPCDHCPOptionsAssociation(
    "VpcDhcpOptionsAssociation",
    DhcpOptionsId=Ref(dhcp_opts),
    VpcId=Ref(vpc)
))

# Security Group
sg = t.add_resource(SecurityGroup(
    "BastionSG",
    GroupDescription="Used for source/dest rules",
    VpcId=Ref(vpc),
    Tags=tags('VPC-Bastion-SG')
))


# Outputs
t.add_output([
    Output(
        "BastionSG",
        Value=Ref(sg)
    ),
    Output(
        "InternetGateway",
        Value=Ref(internet_gateway)
    ),
    Output(
        "VPCID",
        Value=Ref(vpc)
    ),
    Output(
        "VPCName",
        Value=Ref("AWS::StackName")
    )
])
