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
    Idea,
    BE,
    S,
    )

class SExTest(TestCase):

    def test_(self):
        # Arrange.
        l = Idea()
        r = BE(Idea(),Idea())
        s = S(l,r)
        # Act.
        ex = s.excite()
        # Assert.
        self.assertEqual(ex[repr(l)], r)

def alltests():
    return TestSuite([
        TestLoader().loadTestsFromTestCase(SExTest),
    ])