#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool that allow to define the nomenclature for tpRigToolkit projects and data
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import tpDcc
from tpDcc.libs.qt.core import base
from tpDcc.tools.nameit.widgets import nameit
from tpRigToolkit.managers import names


class NameWidget(nameit.NameIt, object):

    NAMING_LIB = names.RigToolkitNameLib

    def __init__(self, parent=None):
        config = tpDcc.ConfigsMgr().get_config('tpRigToolkit-naming')
        super(NameWidget, self).__init__(data_file=config.get_path(), parent=parent)


class NameManager(base.BaseWidget, object):
    def __init__(self, parent):
        super(NameManager, self).__init__(parent=parent)

    def ui(self):
        super(NameManager, self).ui()

        self._name_widget = NameWidget()
        self.main_layout.addWidget(self._name_widget)
