"""Unit tests for the Secret type functionality in KeePassEntry."""
import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the src directory to the path to import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

try:
    from KeePassLibrary.keywords.keepassentry import KeePassEntry
    from KeePassLibrary.errors import RobotFrameworkVersionError, EntryInvalid
except ImportError as e:
    print(f"Failed to import modules: {e}")
    print("Make sure the src directory is accessible")
    raise


class TestKeePassEntrySecret(unittest.TestCase):
    """Test cases for the Secret type functionality."""

    def setUp(self):
        """Set up test fixtures."""
        # Create a mock context for KeePassEntry
        mock_ctx = MagicMock()
        self.keepass_entry = KeePassEntry(mock_ctx)
        
        # Create a mock entry
        self.mock_entry = MagicMock()
        self.mock_entry.password = "test_password"

    def test_get_entry_password_default_behavior(self):
        """Test that default behavior returns plain password."""
        result = self.keepass_entry.get_entry_password(self.mock_entry)
        self.assertEqual(result, "test_password")

    def test_get_entry_password_as_secret_false(self):
        """Test that as_secret=False returns plain password."""
        result = self.keepass_entry.get_entry_password(self.mock_entry, as_secret=False)
        self.assertEqual(result, "test_password")

    def test_get_entry_password_invalid_entry(self):
        """Test that invalid entry raises EntryInvalid."""
        with self.assertRaises(EntryInvalid):
            # Pass an object that's not an Entry instance  
            invalid_entry = MagicMock()
            # Make isinstance return False for this mock
            with patch('builtins.isinstance', return_value=False):
                self.keepass_entry.get_entry_password(invalid_entry)

    @patch('KeePassLibrary.keywords.keepassentry.ROBOT_FRAMEWORK_HAS_SECRET', False)
    def test_get_entry_password_as_secret_unsupported(self):
        """Test that as_secret=True raises error when Secret is not supported."""
        with patch.object(self.keepass_entry, '_get_robot_framework_version', return_value='6.1.1'):
            with self.assertRaises(RobotFrameworkVersionError) as context:
                self.keepass_entry.get_entry_password(self.mock_entry, as_secret=True)
            
            self.assertIn("Secret type is not available", str(context.exception))
            self.assertIn("Robot Framework 6.1.1", str(context.exception))

    @patch('KeePassLibrary.keywords.keepassentry.ROBOT_FRAMEWORK_HAS_SECRET', True)
    @patch('KeePassLibrary.keywords.keepassentry.Secret')
    def test_get_entry_password_as_secret_supported(self, mock_secret):
        """Test that as_secret=True works when Secret is supported."""
        # Mock version check to return True
        with patch.object(self.keepass_entry, '_is_secret_supported', return_value=True):
            mock_secret_instance = MagicMock()
            mock_secret.return_value = mock_secret_instance
            
            result = self.keepass_entry.get_entry_password(self.mock_entry, as_secret=True)
            
            mock_secret.assert_called_once_with("test_password")
            self.assertEqual(result, mock_secret_instance)

    def test_is_secret_supported_version_74(self):
        """Test version check for Robot Framework 7.4."""
        with patch.object(self.keepass_entry, '_get_robot_framework_version', return_value='7.4.0'):
            with patch('KeePassLibrary.keywords.keepassentry.ROBOT_FRAMEWORK_HAS_SECRET', True):
                result = self.keepass_entry._is_secret_supported()
                self.assertTrue(result)

    def test_is_secret_supported_version_75(self):
        """Test version check for Robot Framework 7.5."""
        with patch.object(self.keepass_entry, '_get_robot_framework_version', return_value='7.5.0'):
            with patch('KeePassLibrary.keywords.keepassentry.ROBOT_FRAMEWORK_HAS_SECRET', True):
                result = self.keepass_entry._is_secret_supported()
                self.assertTrue(result)

    def test_is_secret_supported_version_73(self):
        """Test version check for Robot Framework 7.3 (should fail)."""
        with patch.object(self.keepass_entry, '_get_robot_framework_version', return_value='7.3.0'):
            with patch('KeePassLibrary.keywords.keepassentry.ROBOT_FRAMEWORK_HAS_SECRET', True):
                result = self.keepass_entry._is_secret_supported()
                self.assertFalse(result)

    def test_is_secret_supported_version_80(self):
        """Test version check for Robot Framework 8.0."""
        with patch.object(self.keepass_entry, '_get_robot_framework_version', return_value='8.0.0'):
            with patch('KeePassLibrary.keywords.keepassentry.ROBOT_FRAMEWORK_HAS_SECRET', True):
                result = self.keepass_entry._is_secret_supported()
                self.assertTrue(result)

    def test_is_secret_supported_no_import(self):
        """Test version check when Secret import fails."""
        with patch('KeePassLibrary.keywords.keepassentry.ROBOT_FRAMEWORK_HAS_SECRET', False):
            result = self.keepass_entry._is_secret_supported()
            self.assertFalse(result)

    def test_get_robot_framework_version(self):
        """Test getting Robot Framework version."""
        with patch('robot.__version__', '7.4.0'):
            result = self.keepass_entry._get_robot_framework_version()
            self.assertEqual(result, '7.4.0')

    def test_get_robot_framework_version_no_attribute(self):
        """Test getting Robot Framework version when __version__ is not available."""
        with patch('robot.__version__', side_effect=AttributeError):
            result = self.keepass_entry._get_robot_framework_version()
            self.assertEqual(result, 'unknown')


if __name__ == '__main__':
    unittest.main()