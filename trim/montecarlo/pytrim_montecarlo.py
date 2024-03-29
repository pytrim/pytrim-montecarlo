#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: trim.montecarlo.pytrim_montecarlo

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Main of the application pyTRIM-MonteCarlo.
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
from logging import getLogger
import sys

# Third party modules.

# Local modules.

# Project modules.
from trim.montecarlo import setup_logger
from trim.montecarlo.arguments import get_arguments
from trim.montecarlo.simulation import Simulation

# Globals and constants variables.
logger = getLogger(__name__)


class TrimMonteCarloCli:
    def __init__(self):
        self.arguments = None

    def run(self):
        self.arguments = get_arguments()

        simulation = Simulation(self.arguments.input, self.arguments.output)

        simulation.run()


if __name__ == '__main__':  # pragma: no cover
    setup_logger()
    logger.debug("arguments: {}".format(sys.argv))

    cli = TrimMonteCarloCli()
    cli.run()
