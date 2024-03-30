import unittest
import os

from main import load_and_validate_input
from models import TranslationRequest

class TestInputValidation(unittest.TestCase):

    def setUp(self) -> None:
        # Get the directory of the current file
        self.tests_path = os.path.dirname(os.path.realpath(__file__))
        self.requests_path = os.path.join(self.tests_path, 'resources', 'requests')

    
    def test_valid_input(self):
        """Test loading a validation with correct input"""
        valid_input_path = os.path.join(self.requests_path, 'valid_request.json')
        try:
            result = load_and_validate_input(valid_input_path)
            self.assertTrue(isinstance(result, TranslationRequest))
        except Exception as e:
            self.fail(f"Valid input raised an exception {e}")

    def test_missing_tasks(self):
        """Test input handling with missing 'tasks' key."""
        missing_taks_path = os.path.join(self.requests_path, 'missing_tasks_request.json')
        with self.assertRaises(Exception):
            load_and_validate_input(missing_taks_path)

    def test_bad_structure(self):
        """Test input handling with incorrect task structure."""
        bad_structure_path = os.path.join(self.requests_path, 'bad_structure_request.json')
        with self.assertRaises(Exception):
            load_and_validate_input(bad_structure_path)
        
    
if __name__ == "__main__":
    unittest.main()