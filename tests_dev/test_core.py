import os
import json
import nose.tools as nt
from mock import patch, ANY, Mock

import botocore
from botocore.stub import Stubber

from tdemo.core import core
from tdemo import stack_dev


class TestCore(object):

    def setup(self):
        os.environ['AWS_DEFAULT_REGION'] = 'eu-west-1'
        with open("tests_dev/worksample.cfn.template") as f:
            self.expected_template = f.read()

    def test_successfully_generates_cfn_template(self):
        template = stack_dev.generate_template()
        nt.assert_equals(sorted(json.loads(template)),
                         sorted(json.loads(self.expected_template)))

    @patch('tdemo.core.core._stack_exists')
    @patch('botocore.client.BaseClient._make_api_call')
    def test_successfully_creates_stack(self, mock_botoapi, mock_stack_exists):
        mock_stack_exists.return_value = False
        core.create_stack("MyStack", "{}")
        nt.assert_equals(mock_botoapi.call_count, 1)

    @patch('tdemo.core.core._stack_exists')
    @patch('botocore.client.BaseClient._make_api_call')
    @nt.raises(Exception)
    def test_fails_to_create_stack_if_exists(self,
                                             mock_botoapi,
                                             mock_stack_exists):
        mock_stack_exists.return_value = True
        core.create_stack("MyStack", "{}")
        nt.assert_equals(mock_botoapi.call_count, 0)

    @patch('tdemo.core.core._stack_exists')
    @patch('tdemo.core.core.boto3.client')
    def test_successfully_updates_stack(self, mock_botoapi, mock_stack_exists):
        mock_stack_exists.return_value = True
        core.update_stack("MyStack", "{}")
        nt.assert_equals(mock_botoapi.call_count, 1)

    @patch('tdemo.core.core._stack_exists')
    @patch('tdemo.core.core.boto3.client')
    @nt.raises(Exception)
    def test_fails_to_update_stack_if_does_not_exist(self,
                                                     mock_botoapi,
                                                     mock_stack_exists):
        mock_stack_exists.return_value = False
        core.update_stack("MyStack", "{}")
        nt.assert_equals(mock_botoapi.call_count, 0)

    @patch('tdemo.core.core._stack_exists')
    @patch('tdemo.core.core.boto3.client')
    def test_successfully_deletes_stack(self, mock_botoapi, mock_stack_exists):
        mock_stack_exists.return_value = True
        core.delete_stack("MyStack")
        nt.assert_equals(mock_botoapi.call_count, 1)

    @patch('tdemo.core.core._stack_exists')
    @patch('tdemo.core.core.boto3.client')
    @nt.raises(Exception)
    def test_fails_to_delete_stack_if_does_not_exist(self,
                                                     mock_botoapi,
                                                     mock_stack_exists):
        mock_stack_exists.return_value = False
        core.delete_stack("MyStack")
        nt.assert_equals(mock_botoapi.call_count, 0)
