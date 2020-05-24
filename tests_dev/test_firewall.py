import json
import nose.tools as nt

from tdemo.stack_dev import firewall, template


expected_firewall_template = """
{
    "Description": "Service VPC - used for services",
    "Metadata": {
        "Build": "development",
        "DependsOn": [],
        "Environment": "ApiDev",
        "Revision": "develop",
        "StackName": "ApiDev-Dev-VPC",
        "StackType": "InfrastructureResource",
        "TemplateBucket": "cfn-apidev",
        "TemplateName": "VPC",
        "TemplatePath": "ApiDev/Dev/VPC"
    },
    "Outputs": {
        "BastionSG": {
            "Value": {
                "Ref": "BastionSG"
            }
        },
        "InternetGateway": {
            "Value": {
                "Ref": "InternetGateway"
            }
        },
        "VPCID": {
            "Value": {
                "Ref": "VPC"
            }
        },
        "VPCName": {
            "Value": {
                "Ref": "AWS::StackName"
            }
        },
        "VpcNetworkAcl": {
            "Value": {
                "Ref": "VpcNetworkAcl"
            }
        }
    },
    "Resources": {
        "BastionSG": {
            "Properties": {
                "GroupDescription": "Used for source/dest rules",
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "ApiDev-Dev-VPC-Bastion-SG"
                    },
                    {
                        "Key": "Environment",
                        "Value": "ApiDev"
                    },
                    {
                        "Key": "Owner",
                        "Value": "Foo industries"
                    },
                    {
                        "Key": "Service",
                        "Value": "ServiceVPC"
                    },
                    {
                        "Key": "VPC",
                        "Value": "Dev"
                    }
                ],
                "VpcId": {
                    "Ref": "VPC"
                }
            },
            "Type": "AWS::EC2::SecurityGroup"
        },
        "DhcpOptions": {
            "Properties": {
                "DomainName": {
                    "Fn::Join": [
                        "",
                        [
                            {
                                "Ref": "AWS::Region"
                            },
                            ".compute.internal"
                        ]
                    ]
                },
                "DomainNameServers": [
                    "AmazonProvidedDNS"
                ],
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "ApiDev-Dev-DhcpOptions"
                    },
                    {
                        "Key": "Environment",
                        "Value": "ApiDev"
                    },
                    {
                        "Key": "Owner",
                        "Value": "Foo industries"
                    },
                    {
                        "Key": "Service",
                        "Value": "ServiceVPC"
                    },
                    {
                        "Key": "VPC",
                        "Value": "Dev"
                    }
                ]
            },
            "Type": "AWS::EC2::DHCPOptions"
        },
        "InternetGateway": {
            "Properties": {
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "ApiDev-Dev-InternetGateway"
                    },
                    {
                        "Key": "Environment",
                        "Value": "ApiDev"
                    },
                    {
                        "Key": "Owner",
                        "Value": "Foo industries"
                    },
                    {
                        "Key": "Service",
                        "Value": "ServiceVPC"
                    },
                    {
                        "Key": "VPC",
                        "Value": "Dev"
                    }
                ]
            },
            "Type": "AWS::EC2::InternetGateway"
        },
        "VPC": {
            "Properties": {
                "CidrBlock": "10.0.0.0/16",
                "EnableDnsHostnames": "true",
                "EnableDnsSupport": "true",
                "InstanceTenancy": "default",
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "ApiDev-Dev-ServiceVPC"
                    },
                    {
                        "Key": "Environment",
                        "Value": "ApiDev"
                    },
                    {
                        "Key": "Owner",
                        "Value": "Foo industries"
                    },
                    {
                        "Key": "Service",
                        "Value": "ServiceVPC"
                    },
                    {
                        "Key": "VPC",
                        "Value": "Dev"
                    }
                ]
            },
            "Type": "AWS::EC2::VPC"
        },
        "VpcDhcpOptionsAssociation": {
            "Properties": {
                "DhcpOptionsId": {
                    "Ref": "DhcpOptions"
                },
                "VpcId": {
                    "Ref": "VPC"
                }
            },
            "Type": "AWS::EC2::VPCDHCPOptionsAssociation"
        },
        "VpcGatewayAttachment": {
            "Properties": {
                "InternetGatewayId": {
                    "Ref": "InternetGateway"
                },
                "VpcId": {
                    "Ref": "VPC"
                }
            },
            "Type": "AWS::EC2::VPCGatewayAttachment"
        },
        "VpcNetworkAcl": {
            "Properties": {
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "ApiDev-Dev-NetworkAcl"
                    },
                    {
                        "Key": "Environment",
                        "Value": "ApiDev"
                    },
                    {
                        "Key": "Owner",
                        "Value": "Foo industries"
                    },
                    {
                        "Key": "Service",
                        "Value": "ServiceVPC"
                    },
                    {
                        "Key": "VPC",
                        "Value": "Dev"
                    }
                ],
                "VpcId": {
                    "Ref": "VPC"
                }
            },
            "Type": "AWS::EC2::NetworkAcl"
        },
        "VpcNetworkAclInboundRulePublic443": {
            "Properties": {
                "CidrBlock": "0.0.0.0/0",
                "Egress": "false",
                "NetworkAclId": {
                    "Ref": "VpcNetworkAcl"
                },
                "PortRange": {
                    "From": "443",
                    "To": "443"
                },
                "Protocol": "6",
                "RuleAction": "allow",
                "RuleNumber": 20001
            },
            "Type": "AWS::EC2::NetworkAclEntry"
        },
        "VpcNetworkAclInboundRulePublic80": {
            "Properties": {
                "CidrBlock": "0.0.0.0/0",
                "Egress": "false",
                "NetworkAclId": {
                    "Ref": "VpcNetworkAcl"
                },
                "PortRange": {
                    "From": "80",
                    "To": "80"
                },
                "Protocol": "6",
                "RuleAction": "allow",
                "RuleNumber": 20000
            },
            "Type": "AWS::EC2::NetworkAclEntry"
        },
        "VpcNetworkAclOutboundRule": {
            "Properties": {
                "CidrBlock": "0.0.0.0/0",
                "Egress": "true",
                "NetworkAclId": {
                    "Ref": "VpcNetworkAcl"
                },
                "Protocol": "-1",
                "RuleAction": "allow",
                "RuleNumber": 30000
            },
            "Type": "AWS::EC2::NetworkAclEntry"
        },
        "VpcNetworkAclSsh": {
            "Properties": {
                "CidrBlock": "127.0.0.1/32",
                "Egress": "false",
                "NetworkAclId": {
                    "Ref": "VpcNetworkAcl"
                },
                "PortRange": {
                    "From": "22",
                    "To": "22"
                },
                "Protocol": "6",
                "RuleAction": "allow",
                "RuleNumber": 10000
            },
            "Type": "AWS::EC2::NetworkAclEntry"
        }
    }
}

"""


class TestFirewallStack(object):
    def test_firewall(self):
        t = template
        nt.assert_equal(sorted(t.to_dict()),
                        sorted(json.loads(expected_firewall_template)))
