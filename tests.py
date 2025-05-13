import unittest
from check_pwd import check_pwd


class TestCheckPwd (unittest.TestCase):

    def test_assert_false(self):
        """tests takes a blank entry and should return false"""
        self.assertFalse(check_pwd(""))

    def testing_valid_entry(self):
        """testing for a valid length"""
        self.assertTrue(check_pwd("Test~length13"))


if __name__ == '__main__':
    unittest.main()
