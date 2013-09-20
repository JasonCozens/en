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

from i import (Idea, I, BE, S)

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

class ISubstTest(TestCase):

    def test_var_neq(self):
        # Arrange.
        i = I()
        # Act.
        s = i.subst(Idea(), Idea())
        # Assert.
        self.assertIsNot(s, i)
        self.assertEqual(s, i)
        
class MockBE(object):

    def __init__(self, equal, image = ""):
        self.__equal = equal
        self.__repr = image

    def __eq__(self, other):
        return self.__equal

    def __repr__(self):
        return self.__repr

class BETest(TestCase):

    def test_eq_is_reflexive(self):
        # Arrange.
        b = BE(Idea(), Idea())
        # Act & Assert.
        self.assertEqual(b == b, True)

    def test_neq_different_types(self):
        # Arrange.
        l1 = MockBE(True)
        r1 = MockBE(True)
        b1 = BE(l1, r1)
        b2 = MockBE(True)
        self.assertEqual(b1 == b2, False)

    def test_eq(self):
        # Arrange.
        l1 = MockBE(True)
        r1 = MockBE(True)
        b1 = BE(l1, r1)
        l2 = MockBE(True)
        r2 = MockBE(True)
        b2 = BE(l1, r1)
        self.assertEqual(b1 == b2, True)

    def test_eq_left_neq(self):
        # Arrange.
        l1 = MockBE(False)
        r1 = MockBE(True)
        b1 = BE(l1, r1)
        l2 = MockBE(False)
        r2 = MockBE(True)
        b2 = BE(l1, r1)
        self.assertEqual(b1 == b2, False)        

    def test_eq_right_neq(self):
        # Arrange.
        l1 = MockBE(True)
        r1 = MockBE(False)
        b1 = BE(l1, r1)
        l2 = MockBE(True)
        r2 = MockBE(False)
        b2 = BE(l1, r1)
        self.assertEqual(b1 == b2, False)

    def test_eq_left_and_right_neq(self):
        # Arrange.
        l1 = MockBE(False)
        r1 = MockBE(False)
        b1 = BE(l1, r1)
        l2 = MockBE(False)
        r2 = MockBE(False)
        b2 = BE(l1, r1)
        self.assertEqual(b1 == b2, False)

class BEReprTest(TestCase):

    def test_repr(self):
        # Arrange.
        l = MockBE(True, "L")
        r = MockBE(True, "R")
        b = BE(l, r)
        expected = "BE(L,R)"
        # Assert.
        self.assertEqual(repr(b), expected)

    def test_repr_check(self):
        # Arrange.
        b = BE(I(), I())
        # Act.
        r = repr(b)
        e = eval(r)
        # Assert.
        self.assertEqual(r, "BE(I(),I())")
        self.assertEqual(e, b)

class BEStrTest(TestCase):

    def test_str(self):
        # Arrange.
        b = BE(I(), I())
        # Act.
        s = str(b)
        # Assert.
        self.assertEqual(s, "(IBEI)")

class STest(TestCase):

    def test_repr(self):
       # Arrange.
        s = S(I(), I())
        # Act.
        r = repr(s)
        e = eval(r)
        # Assert.
        self.assertEqual(r, "S(I(),I())")
        self.assertEqual(e, s)

    def test_str(self):
        # Arrange.
        b = S(I(), I())
        # Act.
        s = str(b)
        # Assert.
        self.assertEqual(s, "(ISI)")        
        
def alltests():
    return TestSuite([
        TestLoader().loadTestsFromTestCase(ITest),
        TestLoader().loadTestsFromTestCase(ISubstTest),
        TestLoader().loadTestsFromTestCase(BETest),
        TestLoader().loadTestsFromTestCase(BEReprTest),
        TestLoader().loadTestsFromTestCase(BEStrTest),
        TestLoader().loadTestsFromTestCase(STest),
    ])
        
