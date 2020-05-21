# -*- coding: UTF-8 -*-

from EfcControl.Component import Component


class Canvas(Component):
    def __init__(self,width=750,height=570):
        Component.__init__(self)
        object.__setattr__(self, 'alignCenter', 'true')
        object.__setattr__(self, 'autoFocus', 'true')
        object.__setattr__(self, 'autoScroll', 'false')
        object.__setattr__(self, 'border', 1)
        object.__setattr__(self, 'dock', 'null')
        object.__setattr__(self, 'eclass', 'Canvas')
        self.height =height
        object.__setattr__(self, 'id', 'root')
        object.__setattr__(self, 'isTrade', 'true')
        self.items =[]
        object.__setattr__(self, 'layout', {'eclass':'LayoutContainerAbsolute','type':'absolute'})
        object.__setattr__(self, 'qualifiedId', 'root')
        object.__setattr__(self, 'region', 'center')
        self.width =width
        self.x =0
        object.__setattr__(self, 'xtype', 'panel')
        self.y=0

    def __setattr__(self, key, value):
        Component.__setattr__(self, key, value)
        if key in('alignCenter','autoFocus','autoScroll','border','dock',  'id','isTrade','layout','qualifiedId','region'):
            raise AttributeError('{}.{} is READ ONLY'.format(type(self).__name__, key))
        elif key in ('x','y', 'height'):
            if not isinstance(value, int):
                raise AttributeError('{}.{} is JUST ONLY int'.format(type(self).__name__, key))
        elif key == 'items':
            if not isinstance(value, list):
                raise AttributeError('{}.{} is JUST ONLY list'.format(type(self).__name__, key))

        self.__dict__[key] = value
