# -*- coding: UTF-8 -*-

from EfcControl.FormFieldNumber import FormFieldNumber


class FormFieldMoney(FormFieldNumber):

    def __init__(self, name,text, x=0, y=0, labelWidth=80, width=150, height=30):
        FormFieldNumber.__init__(self,name, text, x, y, labelWidth, width, height)
        # 初始化父类中的成员变量
        object.__setattr__(self, 'id', 'money_' + name + '_' + text)
        object.__setattr__(self, 'name', 'money_' + name + '_' + text)
        object.__setattr__(self, 'qualifiedId', 'money_' + name + '_' + text)
        object.__setattr__(self, 'xtype', 'currencyfield')
        object.__setattr__(self, 'eclass', 'FormFieldMoney')
        # 初始化父类中成员变量结束
        self.currencySymbol =''
        self.actionLikeTerm = 'false'
        self.integerLength =15
        self.useThousandSeparator = 'true'
        # 在父类Component中通过__setattr__设置xtype为只读属性,为保证在__init__中对xtype设置正确的初始值，通过object对象的__setattr__来实现初始化


    def __setattr__(self, key, value):
        FormFieldNumber.__setattr__(self, key, value)
        if key in('useThousandSeparator', 'actionLikeTerm'):
            if value not in ('true','false'):
                raise AttributeError('{}.{} is JUST ONLY AS true or false'.format(type(self).__name__, key))
        elif key =='integerLength':
            if not isinstance(value, int):
                raise AttributeError('{}.{} is JUST ONLY int'.format(type(self).__name__, key))
        elif key =='currencySymbol':
            if not isinstance(value, str):
                raise AttributeError('{}.{} is JUST ONLY str'.format(type(self).__name__, key))

        self.__dict__[key] = value

