from troposphere import (
    Tags,
    Template
)

# Common tags to tag AWS Resources with
common_tags = dict(
    Environment='ApiDev',
    Owner='Foo industries',
    Service='ServiceVPC',
    VPC='Dev'
)

# The CloudFormation template for "stack_dev"
template = Template(Description="Service VPC - used for services")
template.add_metadata({
    "Build": "development",
    "DependsOn": [],
    "Environment": "ApiDev",
    "Revision": "develop",
    "StackName": "ApiDev-Dev-VPC",
    "StackType": "InfrastructureResource",
    "TemplateBucket": "cfn-apidev",
    "TemplateName": "VPC",
    "TemplatePath": "ApiDev/Dev/VPC"
})


def tags(resource_name):
    """ Returns common tags along with custom name tag
    for each kind of resource type.

    Parameters:
        resource_name: str
            Name of resource

    Returns:
        troposphere.Tags

    """
    name_tag = '%s-%s-%s' % (common_tags['Environment'],
                             common_tags['VPC'],
                             resource_name)

    return Tags(Name=name_tag) + Tags(**common_tags)


def generate_template():
    """ Generates and returns the required template.
    Importing the modules from the stack automatically creates required
    resources into the general template.
    """
    import vpc
    import firewall
    import topics
    return template.to_json()
