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

from i import (Idea, I, S)

class IT(TestCase):

    def test_repr(self):
        # Act.
        r = repr(I())
        # Assert.
        self.assertEqual(r, 'I()')

    def test_str(self):
        # Act.
        s = str(I())
        # Assert.
        self.assertEqual(s, 'I')

class ST(TestCase):

    def test_new(self):
        # Arrange
        l = Idea()
        r = Idea()
        # Act
        s = S(l, r)
        # Assert
        self.assertEqual(s.l, l)
        self.assertEqual(s.o, S.O)
        self.assertEqual(s.r, r)        

def alltests():
    return TestSuite([
        TestLoader().loadTestsFromTestCase(IT),
        TestLoader().loadTestsFromTestCase(ST),
    ])
        
