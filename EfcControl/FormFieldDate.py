# -*- coding: UTF-8 -*-

from EfcControl.FormField import FormField


class FormFieldDate(FormField):

    def __init__(self, name,text, x=0, y=0, labelWidth=80, width=150, height=30):
        FormField.__init__(self,x,y,labelWidth,width,height)
        # 初始化父类中的成员变量
        object.__setattr__(self, 'id', 'date_' + name + '_' + text)
        object.__setattr__(self, 'name', 'date_' + name + '_' + text)
        object.__setattr__(self, 'qualifiedId', 'date_' + name + '_' + text)
        object.__setattr__(self, 'xtype', 'datefield')
        object.__setattr__(self, 'eclass', 'FormFieldDate')
        self.fieldLabel = text
        # 初始化父类中成员变量结束
        self.format = 'Ymd'
        self.value =''

    def __setattr__(self, key, value):
        FormField.__setattr__(self, key, value)
        if key in('value','format'):
            if not isinstance(value, str):
                raise AttributeError('{}.{} is JUST ONLY str'.format(type(self).__name__, key))
        self.__dict__[key] = value