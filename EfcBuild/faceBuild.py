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
from EfcControl.FormFieldDate import FormFieldDate
from EfcControl.GridPanel import GridPanel
from EfcControl.GridColumnColumn import GridColumnColumn
from EfcControl.Canvas import Canvas
from EfcControl.ButtonButton import ButtonButton
from configparser import *
import os
import sys
from EfcDef import *
import xlrd


class faceBuild(object):
    @property
    def faceDir(self):
        return self.__faceDir

    @property
    def ioDir(self):
        return self.__ioDir

    def __init__(self):
        self.__faceDir =getDefDir('FACE','outDir')
        self.__ioDir =getDefDir('IO','defDir')
        self.inCanvas = Canvas(1000,570)
        self.outCanvas = Canvas(1000,570)

    def calcXY(self,iRow, iCol):
        x = 100 + ((iCol % 4 if iCol % 4 > 0 else 4) - 1) * 250
        y = 12 + (iRow - 1) * 36
        return x,y


    def createinstance(self, isColumn, dataType, name, text):
        aClassName = ''
        if isColumn:
            aClassName ='GridColumnColumn'
        else:
            if dataType not in('select', 'grid', 'char', 'int', 'double','money', 'date'):
                raise AttributeError('接口定义文件中类型描述错误')
            if dataType =='grid':
                aClassName ='GridPanel'
            elif dataType =='char':
                aClassName ='FormFieldFText'
            elif dataType =='select':
                aClassName ='FormFieldComboBox'
            elif dataType =='date':
                aClassName ='FormFieldDate'
            elif dataType =='money':
                aClassName ='FormFieldMoney'
            elif dataType in('int','double'):
                aClassName = 'FormFieldNumber'
        aMod = sys.modules['EfcControl.' + aClassName]
        aClass = getattr(aMod, aClassName)
        return aClass(name,text)

    def insetGridColumn(self, canvas, gridName, gridColumn):
        if type(gridColumn) == GridColumnColumn:
            for canv_item in canvas.items:
                if canv_item['eclass'] == 'GridPanel' and canv_item['id'] =='grid_'+gridName:
                    canv_item['columns'].append(gridColumn.__dict__)

    def fillFace(self, table, canvas):
        isGrid = False
        gridName = ''
        iRow = 1  # 行
        iCol = 1  # 列
        for iIndex in range(1, table.nrows):
            rowValue = table.row_values(iIndex)

            dataName = rowValue[1].strip()
            dataLabel = rowValue[2].strip()
            dataType = rowValue[3].strip().lower()
            dataLeng = rowValue[4]

            if '/' == dataName:
                isGrid = False
                gridName = ''
                continue

            field = self.createinstance(isGrid, dataType, dataName, dataLabel)
            isColumn = False
            if dataType == 'grid':
                isGrid = True
                iRow = iRow + 1
                iCol = 1
                gridName = dataName
                field.x, field.y = self.calcXY(iRow, iCol)
                field.width, field.height = 800, 80
                iRow = iRow + 3
            else:
                if not isGrid:
                    field.x, field.y = self.calcXY(iRow, iCol)
                    iRow, iCol = (iRow + 1, 1) if iCol > 3 else (iRow, iCol + 1)
                else:
                    isColumn = True
                    self.insetGridColumn(canvas, gridName, field)
            if hasattr(field,'maxLength'):
                try:
                    field.maxLength = int(dataLeng)
                except ValueError,e:
                    field.maxLength =0
            if not isColumn:
                canvas.items.append(field.__dict__)
        return iRow

    def createFace(self, defFile):
        tableIn =getDefTable(self.ioDir, defFile, 'req')
        iRow = self.fillFace(tableIn, self.inCanvas)
        buttonSubmit = ButtonButton('SUBMIT','提交')

        iRow = iRow +1
        buttonSubmit.x, buttonSubmit.y = self.calcXY(iRow, 1)
        buttonSubmit.events.append('click')
        buttonSubmit.hotkeys.append({"event": "click","key": "ALTO"})
        buttonSubmit.cls ='confirm'
        buttonExit = ButtonButton('EXIT', '退出')

        buttonExit.x, buttonExit.y = self.calcXY(iRow, 2)
        buttonExit.events.append('click')
        buttonExit.cls = 'exit'
        self.inCanvas.items.append(buttonSubmit.__dict__)
        self.inCanvas.items.append(buttonExit.__dict__)
        tableOut = getDefTable(self.ioDir, defFile, 'res')
        self.fillFace(tableOut, self.outCanvas)
        buttonOK =ButtonButton('OK', '确认')
        iRow = iRow +1
        buttonOK.x, buttonOK.y = self.calcXY(iRow, 1)
        buttonOK.events.append('click')
        buttonOK.cls = 'confirm'
        self.outCanvas.items.append(buttonOK.__dict__)
