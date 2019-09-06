#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: trim.montecarlo

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
import os.path
from logging import getLogger

# Third party modules.

# Local modules.

# Project modules.

# Globals and constants variables.
__author__ = 'Hendrix Demers'
__email__ = 'hendrix.demers@mail.mcgill.ca'
__version__ = '0.1.0'
__copyright__ = '2019, ' + __author__
__project_name__ = 'pyTRIM-MonteCarlo'

logger = getLogger(__name__)


def get_current_module_path(module_filepath, relative_path=""):
    """
    Return the current module path by using :py:obj:`__file__` special module variable.

    An example of usage::

        module_path = get_current_module_path(__file__)

    :param str module_filepath: Pass :py:obj:`__file__` to get the current module path
    :param str relative_path: Optional parameter to return a path relative to the module path
    :return: a path, either the module path or a relative path from the module path
    :rtype: str
    """
    base_path = os.path.dirname(module_filepath)
    logger.debug(base_path)

    file_path = os.path.join(base_path, relative_path)
    logger.debug(file_path)

    file_path = os.path.normpath(file_path)
    logger.debug(file_path)

    return file_path
