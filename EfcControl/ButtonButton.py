# -*- coding: UTF-8 -*-

from EfcControl.Component import Component


class ButtonButton(Component):
    def __init__(self, name, text):
        Component.__init__(self)
        self.x =0
        self.y =0
        self.text =text
        self.hotkeys =[]
        self.events =[]
        self.clickEvent='click'
        self.cls=''
        self.height=30
        self.buttonType ='normal'
        object.__setattr__(self, 'xtype', 'button')
        object.__setattr__(self, 'eclass', 'ButtonButton')
        object.__setattr__(self, 'id', 'btn_' + name+'_'+text)
        object.__setattr__(self, 'name', 'btn_' + name+'_'+text)
        object.__setattr__(self, 'qualifiedId', 'btn_' + name+'_'+text)

    def __setattr__(self, key, value):
        if key =='x':
            if not isinstance(value, int):
                raise AttributeError('{}.{} is JUST ONLY int'.format(type(self).__name__, key))
        elif key =='y':
            if not isinstance(value, int):
                raise AttributeError('{}.{} is JUST ONLY int'.format(type(self).__name__, key))
        elif key =='text':
            if not isinstance(value, str):
                raise AttributeError('{}.{} is JUST ONLY str'.format(type(self).__name__, key))
        elif key == 'hotkeys':
            if not isinstance(value, list):
                raise AttributeError('{}.{} is JUST ONLY list'.format(type(self).__name__, key))
        elif key == 'events':
            if not isinstance(value, list):
                raise AttributeError('{}.{} is JUST ONLY list'.format(type(self).__name__, key))
        elif key == 'buttonType':
            if value not in ('exit','submit','normal'):
                raise AttributeError('{}.{} is JUST ONLY as exit, submit, normal'.format(type(self).__name__, key))
        self.__dict__[key] = value