# -*- coding: UTF-8 -*-

from EfcControl.FormField import FormField


class FormFieldPassword(FormField):
    def __init__(self, name,text, x=0, y=0, labelWidth=80, width=150, height=30):
        FormField.__init__(self,x,y,labelWidth,width,height)
        # 初始化父类中的成员变量
        object.__setattr__(self, 'id', 'pwd_' + name + '_' + text)
        object.__setattr__(self, 'name', 'pwd_' + name + '_' + text)
        object.__setattr__(self, 'qualifiedId', 'pwd_' + name + '_' + text)
        object.__setattr__(self, 'xtype', 'password')
        object.__setattr__(self, 'eclass', 'FormFieldPassword')
        self.fieldLabel = text
        # 初始化父类中成员变量结束
        self.doubleInput = 'false'
        self.enableInputTip = 'false'
        self.allowBlank ='true'
        self.helpText =''
        self.value =''
        self.softEncrypt = 'false'
        self.inputChoice = 'key'

    def __setattr__(self, key, value):
        FormField.__setattr__(self, key, value)
        if key in ('softEncrypt', 'allowBlank','doubleInput','enableInputTip'):
            if value not in ('true', 'false'):
                raise AttributeError('{}.{} is JUST ONLY as true or false'.format(type(self).__name__, key))
        elif key == 'inputChoice':
            if value not in ('key','pin'):
                raise AttributeError('{}.{} is JUST ONLY AS pin or key'.format(type(self).__name__, key))
        elif key in('helpText','value'):
            if not isinstance(value, str):
                raise AttributeError('{}.{} is JUST ONLY str'.format(type(self).__name__, key))
        self.__dict__[key] = value