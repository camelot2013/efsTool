# -*- coding: UTF-8 -*-


class Component(object):

    def __init__(self):
        self.width = 150
        # self.xtype = 'component'
        # self.xtype = 'component'
        object.__setattr__(self, 'xtype', 'component')
        object.__setattr__(self, 'eclass', 'component')
        object.__setattr__(self, 'id', '')
        object.__setattr__(self, 'name', '')
        object.__setattr__(self, 'qualifiedId', '')

    def __setattr__(self, key, value):
        if key == 'width':
            if not isinstance(value, int):
                raise AttributeError('{}.{} is JUST ONLY int'.format(type(self).__name__, key))
        elif key in('xtype','eclass','id','name','qualifiedId'):
            raise AttributeError('{}.{} is READ ONLY'.format(type(self).__name__, key))

        self.__dict__[key] = value
