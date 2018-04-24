#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2015, 2016, 2017 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from . import Indicator
import random as rnd
from os import urandom


class Random(Indicator):
    '''
    This indicator gives a random signal
    '''
    lines = ('random',)

    params = (('min', 10), ('max', 95),)

    plotinfo = dict(plotymargin=0.05, plotyhlines=[0.0, 1.0])

    def __init__(self):
        self.next_tick = None
        random_data = urandom(4)
        seed = int.from_bytes(random_data, byteorder="big")
        rnd.seed(seed)

    def set_next_tick(self):
        self.next_tick = rnd.randint(self.p.min, self.p.max)

    def next(self):
        if self.next_tick is 0:
            self.lines.random[0] = True
            self.set_next_tick()
            return
        elif self.next_tick is None:
            self.set_next_tick()
        elif self.next_tick > 0:
            self.next_tick -= 1

        self.lines.random[0] = False
