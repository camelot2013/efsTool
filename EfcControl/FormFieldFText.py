# -*- coding: UTF-8 -*-

from EfcControl.FormField import FormField


class FormFieldFText(FormField):

    def __init__(self, name,text, x=0, y=0, labelWidth=80, width=150, height=30):
        FormField.__init__(self,x,y,labelWidth,width,height)
        # 初始化父类中的成员变量
        object.__setattr__(self, 'id', 'text_' + name + '_' + text)
        object.__setattr__(self, 'name', 'text_' + name + '_' + text)
        object.__setattr__(self, 'qualifiedId', 'text_' + name + '_' + text)
        object.__setattr__(self, 'xtype', 'ftext')
        object.__setattr__(self, 'eclass', 'FormFieldFText')
        self.fieldLabel = text
        # 初始化父类中成员变量结束
        self.doubleInput = 'false'
        self.enableInputTip ='false'
        self.minLength = 0
        self.maxLength = 0
        self.value =''
        self.validateLengthByBytes = 'true'
        self.helpText =''
        self.permitChars =''
        self.prohibitChars =''

    def __setattr__(self, key, value):
        FormField.__setattr__(self, key, value)
        if key in('doubleInput','enableInputTip','validateLengthByBytes'):
            if value not in ('true', 'false'):
                raise AttributeError('{}.{} is JUST ONLY as true or false'.format(type(self).__name__, key))
        elif key in('maxLength','minLength'):
            if not isinstance(value, int):
                raise AttributeError('{}.{} is JUST ONLY int'.format(type(self).__name__, key))
        elif key in('value','helpText','permitChars','prohibitChars'):
            if not isinstance(value, str):
                raise AttributeError('{}.{} is JUST ONLY str'.format(type(self).__name__, key))
        self.__dict__[key] = value