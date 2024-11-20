import unittest
from journal_functionality import Journal

class TestJournal(unittest.TestCase):
    def test_format_entry(self):
        # Test the format_entry function
        journal = Journal("2024-11-18", "good", "My family", "Could exercise", "Feeling motivated")
        result = journal.format_entry()
        self.assertIsInstance(result, str)  # To ensure it returns a string
        self.assertIn("Date: 2024-11-18", result)  # Checks for correct formatting

if __name__ == "__main__":
    unittest.main()
