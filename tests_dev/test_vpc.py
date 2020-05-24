import json
import nose.tools as nt

from tdemo.stack_dev import vpc, template


expected_vpc_template = """
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
        }
    }
}

"""


class TestVPCStack(object):
    def test_vpc(self):
        t = template
        nt.assert_equal(sorted(t.to_dict()),
                        sorted(json.loads(expected_vpc_template)))
