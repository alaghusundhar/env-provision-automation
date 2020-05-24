from troposphere.sns import Topic
from troposphere import (
    Output,
    Ref
)
from troposphere.ec2 import (
    PortRange,
    NetworkAcl,
    NetworkAclEntry
)

from . import template as t, tags
from vpc import vpc


# Add resources for Network ACL and Network ACL Entries
nacl = t.add_resource(NetworkAcl(
    'VpcNetworkAcl',
    VpcId=Ref(vpc),
    Tags=tags('NetworkAcl')
))

t.add_resource(
    NetworkAclEntry(
        'VpcNetworkAclInboundRulePublic443',
        CidrBlock="0.0.0.0/0",
        Egress=False,
        NetworkAclId=Ref(nacl),
        PortRange=PortRange(From="443", To="443"),
        Protocol="6",
        RuleAction="allow",
        RuleNumber=20001
    )
)

t.add_resource(
    NetworkAclEntry(
        'VpcNetworkAclInboundRulePublic80',
        CidrBlock="0.0.0.0/0",
        Egress=False,
        NetworkAclId=Ref(nacl),
        PortRange=PortRange(From="80", To="80"),
        Protocol="6",
        RuleAction="allow",
        RuleNumber=20000
    )
)

t.add_resource(
    NetworkAclEntry(
        'VpcNetworkAclOutboundRule',
        CidrBlock="0.0.0.0/0",
        Egress="true",
        NetworkAclId=Ref(nacl),
        Protocol="-1",
        RuleAction="allow",
        RuleNumber=30000
    )
)

t.add_resource(
    NetworkAclEntry(
        'VpcNetworkAclSsh',
        CidrBlock="127.0.0.1/32",
        Egress=False,
        NetworkAclId=Ref(nacl),
        PortRange=PortRange(From="22", To="22"),
        Protocol="6",
        RuleAction="allow",
        RuleNumber=10000
    )
)

# Outputs
t.add_output([
    Output(
        "VpcNetworkAcl",
        Value=Ref(nacl)
    )
])
