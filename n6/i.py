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

     O = 'I'

     def __init__(self, l = O, r = O):
         self._l = l
         self._o = Idea.O
         self._r = r

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

     def __repr__(self):
          return 'I()'

     def __str__(self):
          return 'I'

     def __eq__(self, other):
          return False
         
class S(Idea):

     O = '!'

     def __init__(self, l = Idea(), r = Idea()):
          super(S, self).__init__(l, r)
          self._o = S.O


