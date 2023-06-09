#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2015-2020 Daniel Rodriguez
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


from .metabase import MetaParams
from .utils.py3 import with_metaclass


__all__ = ['Filter']

# Filter元类
class MetaFilter(MetaParams):
    pass


# filter类
class Filter(with_metaclass(MetaParams, object)):

    _firsttime = True

    def __init__(self, data):
        pass

    def __call__(self, data):
        # 如果是第一次，就调用nextstart,然后把_firsttime设置成False
        if self._firsttime:
            self.nextstart(data)
            self._firsttime = False
        # 调用next
        self.next(data)

    def nextstart(self, data):
        pass

    def next(self, data):
        pass
