import unittest
import sys, os
from unittest.mock import patch, Mock

import builder

sys.path.append(os.getcwd())
from builder import *

class Service_Builder_Test(unittest.TestCase):
    @patch.object(builder.Service_Builder(), 'spoon')
    def test_spoon(self, mock_spoon):
        mock_spoon.return_value = None
        self.assertEqual(Service_Builder().spoon(), None)
