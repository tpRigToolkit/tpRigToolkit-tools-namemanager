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

    def __init__(self, project=None, parent=None, dev=False):
        if project:
            naming_file = project.get_naming_file()
        else:
            environment = 'development' if dev else 'production'
            config = tpDcc.ConfigsMgr().get_config('tpRigToolkit-names', environment=environment)
            naming_file = config.get_path()

        self.NAMING_LIB().naming_file = naming_file
        self.NAMING_LIB().init_naming_data()

        super(NameWidget, self).__init__(data_file=naming_file, parent=parent)


class NameManager(base.BaseWidget, object):
    def __init__(self, project=None, parent=None, dev=False):
        self._project = project
        self._dev = dev
        super(NameManager, self).__init__(parent=parent)

    def ui(self):
        super(NameManager, self).ui()

        self._name_widget = NameWidget(project=self._project, dev=self._dev)
        self.main_layout.addWidget(self._name_widget)
