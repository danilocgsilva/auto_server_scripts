import unittest
from auto_server_scripts.validate_args import validate_args
from auto_server_scripts.arguments_parser import arguments_parser
from auto_server_scripts.exceptions.ArgumentsNotValid import ArgumentsNotValid
import argparse
from unittest import mock

class test_validate_args(unittest.TestCase):
    
    def test_type_none(self):
        arguments = arguments_parser()
        with self.assertRaises(ArgumentsNotValid):
            validate_args(arguments)
            
    @mock.patch(
        'argparse.ArgumentParser.parse_args',
        return_value=argparse.Namespace(
            type="apache_new_vhost",
            dockerreceipt_inject=True,
            dockerreceipt_address=None,
            server_name="my_server_name"
        )
    )
    def test_dockerreceipt_inject_missing_dockerreceipt_address(self, mock_args):
        arguments = arguments_parser()
        
        with self.assertRaises(ArgumentsNotValid):
            validate_args(arguments)
            
    @mock.patch(
        'argparse.ArgumentParser.parse_args',
        return_value=argparse.Namespace(
            type="apache_new_vhost", 
            server_name=None
        )
    )
    def test_missing_server_name_with_apache_new_vhost(self, mock_args):
        arguments = arguments_parser()
        with self.assertRaises(ArgumentsNotValid):
            validate_args(arguments)

    @mock.patch(
        'argparse.ArgumentParser.parse_args',
        return_value=argparse.Namespace(
            type="apache_new_vhost",
            dockerreceipt_inject=False,
            server_name="my_server_name"
        )
    )
    def test_missing_server_name_with_apache_new_vhost(self, mock_args):
        arguments = arguments_parser()
        self.assertEqual(True, validate_args(arguments))
        
    @mock.patch(
        'argparse.ArgumentParser.parse_args',
        return_value=argparse.Namespace(
            type="apache_new_vhost", 
            server_name="my_server_name",
            dockerreceipt_inject=True,
            dockerreceipt_address="/docker-receipts/my-project/"
        )
    )
    def test_dockerreceipt_inject_with_dockerreceipt_address(self, mock_args):
        arguments = arguments_parser()
        
        self.assertEqual(True, validate_args(arguments))


if __name__ == '__main__':
    unittest.main()