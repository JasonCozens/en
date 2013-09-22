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
from copy import (
    deepcopy,
    )

class Idea(object):
    pass

    def __eq__(self, other):
        if other is self:
            return True
        return type(other) == type(self)
    
    def subst(self, expr, var):
        if self == var:
            return deepcopy(expr)
        return deepcopy(self)

class I(Idea):
     
    def __repr__(self):
        return type(self).__name__ + '()'

    def __str__(self):
        return type(self).__name__


class BE(Idea):

    @property
    def l(self):
        return self.__l

    @property
    def r(self):
        return self.__r

    def __init__(self, l, r):
        self.__l = l
        self.__r = r

    def __eq__(self, other):
        if other is self:
            return True
        if type(other) != type(self):
             return False
        return (other.l == self.l) & (other.r == self.r)

    def __repr__(self):
        return "{0}({1},{2})".format( \
            type(self).__name__, repr(self.__l), repr(self.__r))

    def __str__(self):
        return "({0}{1}{2})".format(str(self.l), type(self).__name__, str(self.r))

    def subst(self, expr, var):
        if self == var:
            return deepcopy(expr)
        return type(self)(self.l.subst(expr, var), self.r.subst(expr, var))

class S(BE):
    
    def excite(self, excited = {}):
        if repr(self.l) in excited:
            excited[repr(self.l)] = T(self.r,excited[repr(self.l)])
        else:
            excited[repr(self.l)] = self.r
        return excited
        
class O(BE):
    pass
        
class R(BE):

    def excite(self, excited = {}):
        return {}
        
class T(BE):
    pass
        
class E(BE):
    pass
        
class D(BE):
    pass

