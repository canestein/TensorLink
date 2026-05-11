# test_tensorlink.py
"""
Tests for TensorLink module.
"""

import unittest
from tensorlink import TensorLink

class TestTensorLink(unittest.TestCase):
    """Test cases for TensorLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TensorLink()
        self.assertIsInstance(instance, TensorLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TensorLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
