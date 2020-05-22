# -*- coding: UTF-8 -*-

from EfcControl.FormFieldMoney import FormFieldMoney
from EfcControl.Component import Component
from EfcControl.FormFieldFText import FormFieldFText
from EfcControl.ButtonButton import ButtonButton
from EfcControl.FormFieldNumberText import FormFieldNumberText
from EfcControl.FormFieldChinese import FormFieldChinese
from EfcControl.FormFieldPassword import FormFieldPassword
from EfcControl.FormFieldNumber import FormFieldNumber
from EfcControl.FormFieldComboBox import FormFieldComboBox
from EfcControl.GridPanel import GridPanel
from EfcControl.GridColumnColumn import GridColumnColumn
from EfcControl.Canvas import Canvas
from EfcBuild.faceBuild import faceBuild
from EfcBuild.javaBuild import javaBuild
import numpy as np
import json
import xlrd
import os
from EfcBuild.messageBuild import messageBuild
from jinja2 import PackageLoader,Environment, FileSystemLoader


if __name__ == "__main__":
    # env = Environment(loader=PackageLoader('EfcBuild', ''))
    # env = Environment(loader=FileSystemLoader('D:/src/python/efsTool/EfcBuild'))
    # template = env.get_template('reqTemplate')
    # fields=[{'fieldDescription':'冻结操作标志','fieldName':'FROPTP'},{'fieldDescription':'冻结编号','fieldName':'FRENUM'}]
    # print template.render({'fields':fields,'grids':[{'GridName':'FCFLX2','columns':[{'fieldDescription':'维护标志','fieldName':'WEIHBZ'},{'fieldDescription':'交易金额','fieldName':'JIOYJE'}]}]})

    # mbuild = messageBuild('99AA')
    # req=mbuild.createReqPacket()
    # res=mbuild.createResPacket()
    # mbuild.writePacket()
    # fb = faceBuild()
    # field = fb.createinstance(False,'char','CUACNO','客户账号')
    # print hasattr(field,'maxLength')
    # field = fb.createinstance(False, 'money', 'CUACNO', '客户账号')
    # print hasattr(field, 'maxLength')
    example2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
    print [j**2 for i in example2 if len(i)>1 for j in i if j%2 == 0]