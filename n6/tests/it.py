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

class ITest(TestCase):

    def test_eq_is_reflexive(self):
        # Arrange.
        i = I()
        # Act & Assert.
        self.assertEqual(i == i, True)

    def test_eq(self):
        self.assertEqual(I() == I(), True)

    def test_not_eq(self):
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

    def __init__(self, equal):
        self.__equal = equal

    def __eq__(self, other):
        return self.__equal

class BOpTest(TestCase):

    def test_eq_is_reflexive(self):
        # Arrange.
        b = BOp('b', Idea(), Idea())
        # Act & Assert.
        self.assertEqual(b == b, True)

    def test_neq_different_types(self):
        # Arrange.
        l1 = MockBOp(True)
        r1 = MockBOp(True)
        b1 = BOp('b', l1, r1)
        b2 = MockBOp(True)
        self.assertEqual(b1 == b2, False)

    def test_eq(self):
        # Arrange.
        l1 = MockBOp(True)
        r1 = MockBOp(True)
        b1 = BOp('b', l1, r1)
        l2 = MockBOp(True)
        r2 = MockBOp(True)
        b2 = BOp('b', l1, r1)
        self.assertEqual(b1 == b2, True)

    def test_eq_left_neq(self):
        # Arrange.
        l1 = MockBOp(False)
        r1 = MockBOp(True)
        b1 = BOp('b', l1, r1)
        l2 = MockBOp(False)
        r2 = MockBOp(True)
        b2 = BOp('b', l1, r1)
        self.assertEqual(b1 == b2, False)        

    def test_eq_right_neq(self):
        # Arrange.
        l1 = MockBOp(True)
        r1 = MockBOp(False)
        b1 = BOp('b', l1, r1)
        l2 = MockBOp(True)
        r2 = MockBOp(False)
        b2 = BOp('b', l1, r1)
        self.assertEqual(b1 == b2, False)

    def test_eq_left_and_right_neq(self):
        # Arrange.
        l1 = MockBOp(False)
        r1 = MockBOp(False)
        b1 = BOp('b', l1, r1)
        l2 = MockBOp(False)
        r2 = MockBOp(False)
        b2 = BOp('b', l1, r1)
        self.assertEqual(b1 == b2, False)
        
def alltests():
    return TestSuite([
        TestLoader().loadTestsFromTestCase(ITest),
        TestLoader().loadTestsFromTestCase(BOpTest),
    ])
        
