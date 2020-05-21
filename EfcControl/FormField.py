# -*- coding: UTF-8 -*-

from EfcControl.Component import Component


class FormField(Component):

    def __init__(self,x=0,y=0,labelWidth=80, width=150, height=30):
        Component.__init__(self)
        object.__setattr__(self, 'autoNextFocus', 'true')
        object.__setattr__(self, 'disabled', 'false')
        self.width =width
        self.x = x
        self.y = y
        object.__setattr__(self, 'xtype', 'formfield')
        object.__setattr__(self, 'eclass', 'formfield')
        object.__setattr__(self, 'id', '')
        object.__setattr__(self, 'name', '')
        object.__setattr__(self, 'qualifiedId', '')
        self.height =height
        self.inputMethod ='normal'
        self.labelTextAlign ='right'
        self.labelWidth =labelWidth
        self.fieldLabel = ''
        object.__setattr__(self, 'hidden', 'false')
        self.textAlign ='left'
        self.events =[]
        self.hotkeys =[]
        self.cls =''
        self.dict =''

    def __setattr__(self, key, value):
        Component.__setattr__(self,key,value)
        if key in('alignCenter','autoFocus','autoScroll','border','dock',  'isTrade','layout','region','hidden'):
            raise AttributeError('{}.{} is READ ONLY'.format(type(self).__name__, key))
        if key in('fieldLabel','cls','dict'):
            if not isinstance(value, str) and not isinstance(value, unicode):
                raise AttributeError('{}.{} is JUST ONLY str'.format(type(self).__name__, key))
        elif key in('x','y','height','labelWidth'):
            if not isinstance(value, int):
                raise AttributeError('{}.{} is JUST ONLY int'.format(type(self).__name__, key))
        elif key in('labelTextAlign','textAlign'):
            if value not in ('center','left','right'):
                raise AttributeError('{}.{} is JUST ONLY AS center, left, right'.format(type(self).__name__, key))
        elif key == 'inputMethod':
            if value not in ('normal','notempty','readonly'):
                raise AttributeError('{}.{} is JUST ONLY AS normal, notempty, readonly'.format(type(self).__name__, key))

        self.__dict__[key] = value