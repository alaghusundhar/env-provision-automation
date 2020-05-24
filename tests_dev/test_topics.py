import json
import nose.tools as nt

from tdemo.stack_dev import topics, template


expected_topics_template = """
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
        "CloudWatchAlarmTopic": {
            "Value": {
                "Ref": "CloudWatchAlarmTopic"
            }
        },
        "NatEmergencyTopicARN": {
            "Value": {
                "Ref": "NatEmergencyTopic"
            }
        }
    },
    "Resources": {
        "CloudWatchAlarmTopic": {
            "Properties": {
                "TopicName": "ApiDev-Dev-CloudWatchAlarms"
            },
            "Type": "AWS::SNS::Topic"
        },
        "NatEmergencyTopic": {
            "Properties": {
                "TopicName": "ApiDev-Dev-NatEmergencyTopic"
            },
            "Type": "AWS::SNS::Topic"
        }
    }
}

"""


class TestTopicsStack(object):
    def test_topics(self):
        t = template
        nt.assert_equal(sorted(t.to_dict()),
                        sorted(json.loads(expected_topics_template)))
