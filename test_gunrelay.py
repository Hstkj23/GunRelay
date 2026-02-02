# test_gunrelay.py
"""
Tests for GunRelay module.
"""

import unittest
from gunrelay import GunRelay

class TestGunRelay(unittest.TestCase):
    """Test cases for GunRelay class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GunRelay()
        self.assertIsInstance(instance, GunRelay)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GunRelay()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
