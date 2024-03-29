#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.montecarlo.file

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the `trim.montecarlo.file` module.
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

# Third party modules.

# Local modules.

# Project modules.
from trim.montecarlo.file import write, read

# Globals and constants variables.


def test_write_read(tmpdir):
    file_path = tmpdir.join("output.hdf5")

    hdf5_file = write(file_path)
    assert hdf5_file.filename == file_path
    assert hdf5_file.mode == "r+"
    assert hdf5_file.driver == "core"
    assert hdf5_file.userblock_size == 0

    hdf5_file.close()

    hdf5_file = read(file_path)
    assert hdf5_file.filename == file_path
    assert hdf5_file.mode == "r"
    assert hdf5_file.driver == "core"
    assert hdf5_file.userblock_size == 0
