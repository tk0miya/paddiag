#!/usr/bin/python

import unittest
from parser import Transformer


class TransformerTestCase(unittest.TestCase):
    def setUp(self):
        self.transformer = Transformer()
