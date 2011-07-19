#
# -*- coding: utf-8 -*-
#
# Copyright (c) 2010, Sascha Peilicke <saschpe@gmx.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program (see the file COPYING); if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

__doc__ = 'Generate distribution packages from Python packages on PyPI'
__docformat__ = 'restructuredtext en'
__author__ = 'Sascha Peilicke <saschpe@gmx.de>'
__version__ = '0.3.19'

from py2pack import list, search, fetch, generate, main
