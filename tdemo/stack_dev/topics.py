from troposphere.sns import Topic
from troposphere import (
    Output,
    Ref
)

from . import template as t, common_tags


def generate_topic_name(topic_name):
    return '%s-%s-%s' % (common_tags['Environment'],
                         common_tags['VPC'],
                         topic_name)

# Topics
nat_emergency_topic = t.add_resource(Topic(
    'NatEmergencyTopic',
    TopicName=generate_topic_name('NatEmergencyTopic')
))
cloudwatch_alarm_topic = t.add_resource(Topic(
    'CloudWatchAlarmTopic',
    TopicName=generate_topic_name('CloudWatchAlarms')
))

# Outputs
t.add_output([
    Output(
        "CloudWatchAlarmTopic",
        Value=Ref(cloudwatch_alarm_topic)
    ),
    Output(
        "NatEmergencyTopicARN",
        Value=Ref(nat_emergency_topic)
    )
])
