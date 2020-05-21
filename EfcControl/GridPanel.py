# -*- coding: UTF-8 -*-

from EfcControl.Component import Component


class GridPanel(Component):
    def __init__(self, name, text, x=0, y=0, width=150, height=30):
        # 初始化父类中的成员变量
        Component.__init__(self)
        object.__setattr__(self, 'xtype', 'efcgrid')
        object.__setattr__(self, 'eclass', 'GridPanel')
        object.__setattr__(self, 'id', 'grid_'+ name)
        object.__setattr__(self, 'name', 'grid_'+ name)
        object.__setattr__(self, 'qualifiedId', 'grid_'+ name)
        # 初始化父类中成员变量结束
        self.checkFlag = 'single'
        self.collapsible = 'false'
        self.columns = []
        self.disabled ='false'
        # self.enableColumnResize = 'true'
        object.__setattr__(self, 'enableColumnResize', 'true')
        self.height = height
        self.hidden ='false'
        self.rowSizeOfPage = 1
        self.showNumber = 'false'
        self.store ={"data": [],"fields": []}
        self.x =x
        self.y =y
        self.width =width

    def __setattr__(self, key, value):
        Component.__setattr__(self, key, value)
        if key == 'store':
            if not isinstance(value, dict):
                raise AttributeError('{}.{} is JUST ONLY dict'.format(type(self).__name__, key))
        elif key == 'showNumber':
            if value not in ('true', 'false'):
                raise AttributeError('{}.{} is JUST ONLY as true or false'.format(type(self).__name__, key))
        elif key == 'rowSizeOfPage':
            if not isinstance(value, int):
                raise AttributeError('{}.{} is JUST ONLY int'.format(type(self).__name__, key))
        elif key == 'enableColumnResize':
            if not isinstance(value, dict):
                raise AttributeError('{}.{} is JUST ONLY dict'.format(type(self).__name__, key))
        elif key == 'checkFlag':
            if value not in ('single', 'multi', 'none'):
                raise AttributeError('{}.{} is JUST ONLY as single, multi, none'.format(type(self).__name__, key))
        elif key == 'collapsible':
            if value not in ('true', 'false'):
                raise AttributeError('{}.{} is JUST ONLY as true or false'.format(type(self).__name__, key))
        elif key == 'columns':
            if not isinstance(value, list):
                raise AttributeError('{}.{} is JUST ONLY list'.format(type(self).__name__, key))
        self.__dict__[key] = value