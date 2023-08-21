#!/usr/bin/python3

import unittest
import pep8
from models.city import City

class City_testing(unittest.TestCase):
  

    def testpep8(self):
      
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/city.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
