# -*- coding: UTF-8 -*-

from EfcControl.FormField import FormField


class FormFieldComboBox(FormField):

    def __init__(self, name,text, x=0, y=0, labelWidth=80, width=150, height=30):
        FormField.__init__(self,x,y,labelWidth,width,height)
        # 初始化父类中的成员变量
        object.__setattr__(self, 'id', 'combo_' + name + '_' + text)
        object.__setattr__(self, 'name', 'combo_' + name + '_' + text)
        object.__setattr__(self, 'qualifiedId', 'combo_' + name + '_' + text)
        object.__setattr__(self, 'xtype', 'combobox')
        object.__setattr__(self, 'eclass', 'FormFieldComboBox')
        self.fieldLabel = text
        # 初始化父类中成员变量结束
        # self.displayField = 'text'
        object.__setattr__(self, 'displayField', 'text')
        self.value =''
        object.__setattr__(self, 'displayType', 'valuetext')
        # self.displayType = 'valuetext'
        # self.forceSelection ='true'
        object.__setattr__(self, 'forceSelection', 'true')
        # self.listWidth =0
        object.__setattr__(self, 'listWidth', 0)
        # self.queryMode ='local'
        object.__setattr__(self, 'queryMode', 'local')
        self.storeType = 'file'
        # self.typeAhead ='false'
        object.__setattr__(self, 'typeAhead', 'false')
        # self.valueField ='value'
        object.__setattr__(self, 'valueField', 'value')
        self.storeFile ={}

    def __setattr__(self, key, value):
        FormField.__setattr__(self, key, value)
        if key in ('valueField','typeAhead','queryMode','listWidth','forceSelection','displayType','displayField'):
            raise AttributeError('{}.{} is JUST ONLY'.format(type(self).__name__, key))
        elif key in('value'):
            if not isinstance(value, str):
                raise AttributeError('{}.{} is JUST ONLY str'.format(type(self).__name__, key))
        elif key =='storeType':
            if value not in('file','constant'):
                raise AttributeError('{}.{} is JUST ONLY file or constant'.format(type(self).__name__, key))
        elif key =='storeFile':
            if not isinstance(value, dict):
                raise AttributeError('{}.{} is JUST ONLY dict'.format(type(self).__name__, key))
        self.__dict__[key] = value