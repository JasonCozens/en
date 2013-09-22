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

from i import (
    I,
    BE,
    S,
    O,
    R,
    T,
    )

class SExciteTest(TestCase):

    def test_excite_node(self):
        # Arrange.
        l = I()
        r = BE(I(),I())
        s = S(l,r)
        # Act.
        ex = s.excite()
        # Assert.
        self.assertEqual(ex[repr(l)], r)

    def test_excite_not_in_dictionary(self):
        # Arrange.
        l = I()
        r = BE(I(),I())
        s = S(l,r)
        particles = {repr(S(I(),I())):I()}
        # Act.
        ex = s.excite(particles)
        # Assert.
        self.assertEqual(len(ex), 2)
        self.assertEqual(ex[repr(l)], r)
        self.assertEqual(ex[repr(S(I(),I()))], I())

    def test_excite_in_dictionary(self):
        # Arrange.
        l = I()
        r = BE(I(),I())
        s = S(l,r)
        particles = {repr(l):I()}
        # Act.
        ex = s.excite(particles)
        # Assert.
        self.assertEqual(len(ex), 1)
        self.assertEqual(ex[repr(l)], T(r,I()))

class MockIdea():

    def __init__(self, excited = {}):
        self.__excited = excited

    def excite(self):
        return self.__excited

class RExciteTest(TestCase):

    def test_excite(self):
        # Arrange.
        x = MockIdea()
        y = MockIdea()
        r = R(x,y)
        # Act.
        excited = r.excite()
        # Assert.
        self.assertEqual(excited, {})

class OExciteTest(TestCase):

    def test_excite(self):
        # Arrange.
        x = MockIdea({'I()':I()})
        y = MockIdea()
        i = O(x,y)
        # Act.
        excited = i.excite()
        # Assert.
        self.assertEqual(excited, x.excite())

def alltests():
    return TestSuite([
        TestLoader().loadTestsFromTestCase(SExciteTest),
        TestLoader().loadTestsFromTestCase(RExciteTest),
        TestLoader().loadTestsFromTestCase(OExciteTest),
    ])
