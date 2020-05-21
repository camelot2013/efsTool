# -*- coding: UTF-8 -*-

from EfcControl.Component import Component


class GridColumnColumn(Component):
    def __init__(self, name, text,width=60):
        # 初始化父类中的成员变量
        Component.__init__(self)
        object.__setattr__(self, 'xtype', 'gridcolumn')
        object.__setattr__(self, 'eclass', 'GridColumnColumn')
        object.__setattr__(self, 'id', name)
        object.__setattr__(self, 'name', name)
        object.__setattr__(self, 'qualifiedId', name)
        # 初始化父类中成员变量结束
        object.__setattr__(self, 'dataIndex', name)
        self.align ='left'
        self.cls =''
        self.dataType ='string'
        object.__setattr__(self, 'dateFormat', '')
        object.__setattr__(self, 'displayType', 'valuetext')
        object.__setattr__(self, 'editable', 'false')
        self.filterName =''
        self.flex =0
        self.hidden ='false'
        object.__setattr__(self, 'inputMethod', 'normal')
        object.__setattr__(self, 'isKey', 'false')
        self.items =[]
        object.__setattr__(self, 'locked', 'false')
        object.__setattr__(self, 'maxLength', 0)
        object.__setattr__(self, 'maxValue', 9223372036854775807)
        object.__setattr__(self, 'minLength', 0)
        object.__setattr__(self, 'minValue', 0)
        object.__setattr__(self, 'relationField', '')
        self.sortable ='true'
        self.storeType ='constant'
        self.storeFile ={}
        self.text =text
        self.visible ='false'
        self.width =width


    def __setattr__(self, key, value):
        Component.__setattr__(self, key, value)
        if key == 'storeType':
            if value not in ('constant','file'):
                raise AttributeError('{}.{} is JUST ONLY AS constant or file'.format(type(self).__name__, key))
        elif key in('items'):
            if not isinstance(value, list):
                raise AttributeError('{}.{} is JUST ONLY list'.format(type(self).__name__, key))
        elif key in('hidden','sortable','visible'):
            if value not in ('true','false'):
                raise AttributeError('{}.{} is JUST ONLY AS true or false'.format(type(self).__name__, key))
        elif key in('align'):
            if value not in ('left','center','right'):
                raise AttributeError('{}.{} is JUST ONLY AS left,center,right'.format(type(self).__name__, key))
        elif key == 'displayType':
            if value not in ('constant','text'):
                raise AttributeError('{}.{} is JUST ONLY AS constant or text'.format(type(self).__name__, key))
        elif key == 'dataType':
            if value not in ('string','currency','select'):
                raise AttributeError('{}.{} is JUST ONLY AS select, currency, string'.format(type(self).__name__, key))
        elif key in('flex'):
            if not isinstance(value, int):
                raise AttributeError('{}.{} is JUST ONLY int'.format(type(self).__name__, key))
        elif key in('storeFile'):
            if not isinstance(value, dict):
                raise AttributeError('{}.{} is JUST ONLY dict'.format(type(self).__name__, key))
        elif key in('cls','filterName'):
            if not isinstance(value, str):
                raise AttributeError('{}.{} is JUST ONLY str'.format(type(self).__name__, key))
        elif key in('dataIndex','dateFormat','displayType','editable','inputMethod','isKey','locked','maxLength','maxValue','minLength','minValue','relationField'):
            raise AttributeError('{}.{} is JUST ONLY'.format(type(self).__name__, key))
        self.__dict__[key] = value