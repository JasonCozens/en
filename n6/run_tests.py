#!/usr/bin/env python3
#
# Affero GPL
#
import unittest

def alltests():
    return unittest.TestSuite([
        ])

unittest.TextTestRunner(verbosity = 2).run(alltests())
