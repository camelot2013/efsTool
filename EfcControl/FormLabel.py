# -*- coding: UTF-8 -*-

from EfcControl.Component import Component

class FormLabel(Component):
    def __init__(self):
        Component.__init__(self)
        object.__setattr__(self, 'xtype', 'label')
        object.__setattr__(self, 'eclass', 'FormLabel')

    def __setattr__(self, key, value):
        Component.__setattr__(self, key, value)
        self.__dict__[key] = value