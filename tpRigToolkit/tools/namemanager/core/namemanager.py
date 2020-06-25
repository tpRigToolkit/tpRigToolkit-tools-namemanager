#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool to manage the nomenclature of tpRigToolkit projects and data
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import os

from tpDcc.core import tool
from tpDcc.libs.qt.widgets import toolset

# Defines ID of the tool
TOOL_ID = 'tpRigToolkit-tools-namemanager'


class NameManagerTool(tool.DccTool, object):
    def __init__(self, *args, **kwargs):
        super(NameManagerTool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = tool.DccTool.config_dict(file_name=file_name)
        tool_config = {
            'name': 'Name Manager',
            'id': 'tpRigToolkit-tools-namemanager',
            'icon': 'namemanager',
            'tooltip': 'Tool to manage the nomenclature of tpRigToolkit projects and data',
            'tags': ['name', 'manager'],
            'logger_dir': os.path.join(os.path.expanduser('~'), 'tpRigToolkit', 'logs', 'tools'),
            'logger_level': 'INFO',
            'is_checkable': False,
            'is_checked': False,
            'menu_ui': {'label': 'Name Manager', 'load_on_startup': False, 'color': '', 'background_color': ''},
            'menu': [
                {'label': 'Name Manager',
                 'type': 'menu', 'children': [{'id': 'tpRigToolkit-tools-namemanager', 'type': 'tool'}]}],
            'shelf': [
                {'name': 'Name Manager',
                 'children': [{'id': 'tpRigToolkit-tools-namemanager', 'display_label': False, 'type': 'tool'}]}
            ]
        }
        base_tool_config.update(tool_config)

        return base_tool_config

    def launch(self, *args, **kwargs):
        return self.launch_frameless(*args, **kwargs)


class NameManagerToolset(toolset.ToolsetWidget, object):

    ID = TOOL_ID

    def __init__(self, *args, **kwargs):

        self._project = kwargs.pop('project', None)

        super(NameManagerToolset, self).__init__(*args, **kwargs)

    def contents(self):
        from tpRigToolkit.tools.namemanager.widgets import namemanager
        name_manager_widget = namemanager.NameManager(project=self._project, parent=self, dev=self._dev)

        return [name_manager_widget]

