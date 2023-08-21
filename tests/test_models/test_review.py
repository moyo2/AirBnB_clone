#!/usr/bin/python3
""" Reviews """
import unittest
import pep8
from models.review import Review

class Review_testing(unittest.TestCase):
    """ BaseModel checks"""

    def testpep8(self):
        """ codestyls_testing """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/review.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
