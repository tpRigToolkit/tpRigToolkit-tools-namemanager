#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains general tests for tpRigToolkit-tools-namemanager
"""

import pytest

from tpRigToolkit.tools.namemanager import __version__


def test_version():
    assert __version__.__version__
