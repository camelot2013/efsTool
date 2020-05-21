# -*- coding: UTF-8 -*-

from EfcControl.FormField import FormField


class FormFieldNumber(FormField):

    def __init__(self, name,text, x=0, y=0, labelWidth=80, width=150, height=30):
        FormField.__init__(self,x,y,labelWidth,width,height)
        # 初始化父类中的成员变量
        object.__setattr__(self, 'id', 'num_' + name + '_' + text)
        object.__setattr__(self, 'name', 'num_' + name + '_' + text)
        object.__setattr__(self, 'qualifiedId', 'num_' + name + '_' + text)
        object.__setattr__(self, 'xtype', 'numberfield')
        object.__setattr__(self, 'eclass', 'FormFieldNumber')
        self.fieldLabel = text
        # 初始化父类中成员变量结束
        self.doubleInput = 'false'
        self.enableInputTip = 'false'
        self.value =''
        self.decimalPrecision =2
        self.minValue =0
        self.maxValue =9223372036854775807

    def __setattr__(self, key, value):
        FormField.__setattr__(self, key, value)
        if key in ('doubleInput', 'enableInputTip'):
            if value not in ('true', 'false'):
                raise AttributeError('{}.{} is JUST ONLY as true or false'.format(type(self).__name__, key))
        elif key in('minValue','maxValue'):
            if not isinstance(value, int) and not isinstance(value, long):
                raise AttributeError('{}.{} is JUST ONLY int or long'.format(type(self).__name__, key))
        elif key in('decimalPrecision'):
            if not isinstance(value, int):
                raise AttributeError('{}.{} is JUST ONLY int'.format(type(self).__name__, key))
        elif key in('value'):
            if not isinstance(value, str):
                raise AttributeError('{}.{} is JUST ONLY str'.format(type(self).__name__, key))
        self.__dict__[key] = value