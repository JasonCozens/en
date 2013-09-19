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
class Idea(object):

     @property
     def l(self):
          return self._l

     @property
     def o(self):
          return self._o

     @property
     def r(self):
          return self._r

class I(Idea):

    def __eq__(self, other):
        if other is self:
            return True
        return type(other) == I
     
    def __repr__(self):
        return 'I()'

    def __str__(self):
        return 'I'

class BOp(Idea):

    @property
    def l(self):
        return self.__l

    @property
    def r(self):
        return self.__r

    def __init__(self, B, b, l, r):
        self.__B = B
        self.__l = l
        self.__b = b
        self.__r = r

    def __eq__(self, other):
        if other is self:
            return True
        if type(other) != type(self):
             return False
        return (other.l == self.l) & (other.r == self.r)

    def __repr__(self):
        return ''



