# -*- coding: UTF-8 -*-

from EfcControl.FormFieldDate import FormFieldDate


class FormFieldTime(FormFieldDate):

    def __init__(self, name,text, x=0, y=0, labelWidth=80, width=150, height=30):
        FormFieldDate.__init__(self,x,y,labelWidth,width,height)
        # 初始化父类中的成员变量
        object.__setattr__(self, 'id', 'time_' + name + '_' + text)
        object.__setattr__(self, 'name', 'time_' + name + '_' + text)
        object.__setattr__(self, 'qualifiedId', 'time_' + name + '_' + text)
        object.__setattr__(self, 'xtype', 'timefield')
        object.__setattr__(self, 'eclass', 'FormFieldTime')
        self.fieldLabel = text
        # 初始化父类中成员变量结束
        self.format = 'H:i:s'
        self.value =''

    def __setattr__(self, key, value):
        FormFieldDate.__setattr__(self, key, value)
        if key in('value','format'):
            if not isinstance(value, str):
                raise AttributeError('{}.{} is JUST ONLY str'.format(type(self).__name__, key))
        self.__dict__[key] = value