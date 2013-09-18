#!/usr/bin/env python3
#
# Affero GPL
#
from unittest import (
    TestSuite,
    TextTestRunner,
    )

def alltests():
    return TestSuite([
        ])

TextTestRunner(verbosity = 2).run(alltests())
