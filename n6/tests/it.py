#!/usr/bin/env python3
#    Engineering Note 6: The Imagination (Algebra).
#    Copyright (C) 2013  Edward Jason Cozens
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from unittest import (
    TestCase,
    TestSuite,
    TestLoader
    )

from i import (Idea, I, BOp)

class IT(TestCase):

    def test_equal_is_reflexive(self):
        # Arrange.
        i = I()
        # Act & Assert.
        self.assertEqual(i == i, True)

    def test_equal(self):
        self.assertEqual(I() == I(), True)

    def test_not_equal(self):
        self.assertEqual(I() == Idea(), False)

    def test_repr(self):
        # Act.
        r = repr(I())
        # Assert.
        self.assertEqual(r, 'I()')
        self.assertEqual(type(eval(r)), I)

    def test_str(self):
        # Act.
        s = str(I())
        # Assert.
        self.assertEqual(s, 'I')
        
class MockBOp(object):

    def __init__(self, repr):
        self.__repr = repr

    def __repr__(self):
        return self.__repr

class BOpT(TestCase):

    def test_repr(self):
        # Arrange.
        l = MockBOp('l')
        r = MockBOp('r')
        b = BOp('B', 'b', l, r)
        # Act.
        rep = repr(b)
        # Assert.
        self.assertEqual(rep, 'B(l,r)')
        
def alltests():
    return TestSuite([
        TestLoader().loadTestsFromTestCase(IT),
        TestLoader().loadTestsFromTestCase(BOpT),
    ])
        
