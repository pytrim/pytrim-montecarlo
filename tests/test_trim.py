#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.test_trim

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>


"""

# Copyright 2019 Hendrix Demers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Standard library modules.
import sys

# Third party modules.

# Local modules.

# Project modules.
import trim

# Globals and constants variables.


def test_namespace_packages():
    """
    Namespace packages does not have a __file__ attribute.

    :return:
    """
    if sys.version_info.minor < 7:  # pragma: no cover
        import pytest
        with pytest.raises(AttributeError):
            # noinspection PyStatementEffect
            trim.__file__
    else:
        assert trim.__file__ is None
