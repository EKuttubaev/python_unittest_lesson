from unittest import TestCase
from functions.email import is_correct_email

class EmailFunctionTextCase(TestCase):
    def test_returns_True_for_correct_mail(self):
        self.assertTrue(is_correct_email("masteralish@gmail.com"))
    def tests_returtns_False_if_email_contains_two_at_signs(self):
        self.assertFalse(is_correct_email("master@Alish@mail.ru"))