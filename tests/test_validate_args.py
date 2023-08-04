import unittest
from auto_server_scripts.validate_args import validate_args
from auto_server_scripts.arguments_parser import arguments_parser
from auto_server_scripts.exceptions.ArgumentsNotValid import ArgumentsNotValid

class test_validate_args(unittest.TestCase):
    
    def test_type_none(self):
    
        arguments = arguments_parser([])
        with self.assertRaises(ArgumentsNotValid):
            validate_args(arguments)
