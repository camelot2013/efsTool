# -*- coding: UTF-8 -*-


from EfcDef import *
from jinja2 import PackageLoader,Environment, FileSystemLoader


class messageBuild(object):
    @property
    def ioDir(self):
        return self.__ioDir

    @property
    def trxno(self):
        return self.__trxno

    @property
    def tableIn(self):
        return self.__tableIn

    @property
    def tableOut(self):
        return self.__tableOut

    @property
    def tablePrt(self):
        return self.__tablePrt

    @property
    def reqTemplate(self):
        return self.__req_template

    @property
    def resTemplate(self):
        return self.__res_template

    def __init__(self, trxno):
        self.__ioDir = getDefDir('IO', 'defDir')
        self.__trxno =trxno
        self.__tableIn = getDefTable(self.ioDir, self.trxno+'.xls', 'req')
        self.__tableOut = getDefTable(self.ioDir, self.trxno+'.xls', 'res')
        self.__tablePrt = getDefTable(self.ioDir, self.trxno + '.xls', 'prt')
        tempDir = getDefDir('TEMPLATE', 'tempDir')
        env = Environment(loader=FileSystemLoader(tempDir))
        self.__req_template = env.get_template('reqTemplate')
        self.__res_template = env.get_template('resTemplate')

    #obj = {'objName': '', 'fields': [], 'grids': [{'GridName':'','columns':[]}]}
    def __createPrt(self, obj, objName, dataName, dataLabel, dataType, isGrid=False, gridName=''):

        obj['objName'] = objName
        if isGrid:
            isFlag = False
            for grid in obj['grids']:
                if not grid['GridName']:
                    grid['GridName'] = gridName
                    grid['columns'].append({'fieldDescription':dataLabel,'fieldName':dataName})
                    isFlag = True
                    break
                if grid['GridName'] == gridName:
                    grid['columns'].append({'fieldDescription': dataLabel, 'fieldName': dataName})
                    isFlag = True
                    break
            if not isFlag:
                obj['grids'].append({'GridName':gridName,'columns':[{'fieldDescription': dataLabel, 'fieldName': dataName}]})
        else:
            obj['fields'].append({'fieldDescription':dataLabel,'fieldName':dataName})

        # print dataName, objName, isGrid, gridName, obj

    def createResPacket(self):
        isGrid = False
        fields = []
        grids = []
        gridName = ''
        for iIndex in range(1, self.tableOut.nrows):
            rowValue = self.tableOut.row_values(iIndex)
            dataName = rowValue[1].strip()
            dataLabel = rowValue[2].strip()
            dataType = rowValue[3].strip().lower()

            if '/' == dataName:
                isGrid = False
                gridName = ''
                continue
            if isGrid:
                for grid in grids:
                    if grid['GridName'] == gridName:
                        grid['columns'].append({'fieldDescription':dataLabel,'fieldName':dataName})
            else:
                if dataType == 'grid':
                    isGrid = True
                    gridName =dataName
                    grids.append({'GridName':dataName,'columns':[]})
                else:
                    fields.append({'fieldDescription':dataLabel,'fieldName':dataName})
        objName =''
        objects=[]
        isGrid = False
        gridName = ''
        # obj = {'objName': '', 'fields': [], 'grids': [{'GridName':'','columns':[]}]}
        obj = {'objName': '', 'fields': [], 'grids': []}
        for iIndex in range(1, self.tablePrt.nrows):
            rowValue = self.tablePrt.row_values(iIndex)
            # objName = rowValue[0].strip() if rowValue[0].strip() else objName
            dataName = rowValue[1].strip()
            dataLabel = rowValue[2].strip()
            dataType = rowValue[3].strip().lower()
            if rowValue[0].strip() and rowValue[0].strip() != objName:
                # obj = {'objName': '', 'fields': [], 'grids': [{'GridName': '', 'columns': []}]}
                obj = {'objName': '', 'fields': [], 'grids': []}
                objName = rowValue[0].strip()
                objects.append(obj)
            if '/' == dataName:
                isGrid = False
                gridName = ''
                continue
            if dataType == 'grid':
                isGrid = True
                gridName = dataName
                continue
            self.__createPrt(obj, objName, dataName, dataLabel, dataType, isGrid, gridName)

        return self.resTemplate.render({'fields': fields, 'grids': grids, 'objects':objects})

    def createReqPacket(self):
        isGrid = False
        fields=[]
        grids=[]
        gridName =''
        for iIndex in range(1, self.tableIn.nrows):
            rowValue = self.tableIn.row_values(iIndex)
            dataName = rowValue[1].strip()
            dataLabel = rowValue[2].strip()
            dataType = rowValue[3].strip().lower()

            if '/' == dataName:
                isGrid = False
                gridName = ''
                continue

            if isGrid:
                for grid in grids:
                    if grid['GridName'] == gridName:
                        grid['columns'].append({'fieldDescription':dataLabel,'fieldName':dataName})
            else:
                if dataType == 'grid':
                    isGrid = True
                    gridName =dataName
                    grids.append({'GridName':dataName,'columns':[]})
                else:
                    fields.append({'fieldDescription':dataLabel,'fieldName':dataName})

        return self.reqTemplate.render({'fields':fields,'grids':grids})

    def writePacket(self):
        outDir =getDefDir('SOAP','outDir')
        reqFile = os.path.join(outDir, self.trxno + '_req.packet')
        resFile = os.path.join(outDir, self.trxno + '_res.packet')
        with open(reqFile, 'w') as fw:
            fw.write(self.createReqPacket())

        with open(resFile, 'w') as fw:
            fw.write(self.createResPacket())
