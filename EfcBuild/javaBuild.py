# -*- coding: UTF-8 -*-


from configparser import *
import os
from EfcDef import *
from string import Template
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


class javaBuild(object):
    @property
    def javaDir(self):
        return self.__javaDir

    @property
    def ioDir(self):
        return self.__ioDir

    @property
    def tempDir(self):
        return self.__tempDir

    @property
    def inTemplate(self):
        return self.__inTemplate

    @property
    def outTemplate(self):
        return self.__outTemplate

    @property
    def catalog(self):
        return self.__catalog

    @property
    def trxno(self):
        return self.__trxno

    @property
    def javaInBuff(self):
        return self.__javaInBuff

    @property
    def javaOutBuff(self):
        return self.__outJavaBuff

    def __init__(self, catalog, trxno):
        self.__ioDir =getDefDir('IO','defDir')
        self.__javaDir=getDefDir('JAVA','outDir')
        self.__tempDir=getDefDir('TEMPLATE','tempDir')
        self.__catalog = catalog
        self.__trxno = trxno
        self.javaInDefInfo=[]
        self.javaOutDefInfo = []
        self.__inTemplate = Template('')
        self.__outTemplate = Template('')
        self.gridValues=[]
        self.__javaInBuff=''
        self.__outJavaBuff=''

    def __genJavaDefArray(self, table, isOut):
        isGrid = False
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
            if dataType not in ('select', 'grid', 'char', 'int', 'double', 'money'):
                continue
            if isGrid:
                aClassName = 'GridColumnColumn'
                fieldName = dataName
            else:
                if dataType == 'grid':
                    aClassName = 'GridPanel'
                    fieldName = 'grid_' + dataName
                    isGrid = True
                    if isOut:
                        self.gridValues.append('int iZBISHU = GridUtil.getBISHU(outputMap);')
                        self.gridValues.append(Template('	    	List < Map < String, Object >> dataList = SysUtil.getFormLoopList(outputMap, "FORM", "${gridName}");').substitute({'gridName':dataName}))
                        self.gridValues.append(Template('	    	TranUtil.flushList(grid_${gridName}, "1", dataList, iZBISHU);').substitute({'gridName':dataName}))
                elif dataType == 'char':
                    aClassName = 'FormFieldFText'
                    fieldName = 'text_' + dataName + '_' + dataLabel
                elif dataType == 'select':
                    aClassName = 'FormFieldComboBox'
                    fieldName = 'combo_' + dataName + '_' + dataLabel
                elif dataType == 'money':
                    aClassName = 'FormFieldMoney'
                    fieldName = 'money_' + dataName + '_' + dataLabel
                elif dataType in ('int', 'double'):
                    aClassName = 'FormFieldNumber'
                    fieldName = 'num_' + dataName + '_' + dataLabel
            # tempStr = Template('	public ${eclass} ${qualifiedId};')
            javaDefStr = Template('	public ${eclass} ${qualifiedId};').substitute({'eclass':aClassName, 'qualifiedId':fieldName})
            if isOut:
                self.javaOutDefInfo.append(javaDefStr)
            else:
                self.javaInDefInfo.append(javaDefStr)
    def createJava(self, defFile):
        tableIn = getDefTable(self.ioDir, defFile, 'req')
        tableOut = getDefTable(self.ioDir, defFile, 'res')
        self.__genJavaDefArray(tableIn, False)
        self.__genJavaDefArray(tableOut, True)

        sInFile ="javaInTemplate"
        sOutFile="javaOutTemplate"

        if not os.path.exists(os.path.join(self.tempDir,sInFile)):
            print '获取模板文件失败：', sInFile
            exit(0)
        if not os.path.exists(os.path.join(self.tempDir,sOutFile)):
            print '获取模板文件失败：', sOutFile
            exit(0)
        with open(os.path.join(self.tempDir,sInFile), 'r') as fEfcSet:
            self.__inTemplate = Template(fEfcSet.read())

        with open(os.path.join(self.tempDir,sOutFile), 'r') as fEfcSet:
            self.__outTemplate = Template(fEfcSet.read())

        self.__javaInBuff = self.inTemplate.substitute({'catalog': self.catalog, 'trxno': self.trxno, 'controlItems': '\n'.join(self.javaInDefInfo)+ '\n'})
        self.__outJavaBuff = self.outTemplate.substitute(
            {'catalog': self.catalog, 'trxno': self.trxno, 'controlItems': '\n'.join(self.javaOutDefInfo) + '\n', 'gridValues':'\n'.join(self.gridValues)})
