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
        self.__fakeres_template = env.get_template('fakeResTemplate')

    def __createPrt(self, obj, objName, dataName, dataLabel, dataType, isGrid=False, gridName=''):
        if isGrid:
            for grid in obj['grids']:
                if grid['GridName'] ==gridName:
                    grid['columns'].append({'fieldDescription': dataLabel, 'fieldName': dataName})
        else:
            if 'fields' in obj.keys():
                obj['fields'].append({'fieldDescription': dataLabel, 'fieldName': dataName})
            else:
                obj['fields'] = [{'fieldDescription': dataLabel, 'fieldName': dataName}]

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
        output_object ={'object_name': 'O'+self.trxno+'2'}
        if fields:
            output_object['output_fields'] = fields
        if grids:
            output_object['output_grids'] = grids

        objName =''
        objects=[]
        isGrid = False
        gridName = ''
        for iIndex in range(1, self.tablePrt.nrows):
            rowValue = self.tablePrt.row_values(iIndex)
            objName = rowValue[0].strip()
            if objName:
                obj = self.__getRptObj(objects, objName)
                if not obj:
                    obj = {'objName': objName}
                    objects.append(obj)
            dataName = rowValue[1].strip()
            dataLabel = rowValue[2].strip()
            dataType = rowValue[3].strip().lower()
            if '/' == dataName:
                isGrid = False
                gridName = ''
                continue
            if dataType == 'grid':
                isGrid = True
                gridName = dataName
                if 'grids' in obj.keys():
                    obj['grids'].append({'GridName':dataName,'columns':[]})
                else:
                    obj['grids'] =[{'GridName': dataName, 'columns': []}]
                continue
            self.__createPrt(obj, objName, dataName, dataLabel, dataType, isGrid, gridName)
        # print self.__fakeres_template.render({'output_object': output_object, 'print_objects':objects})
        return self.resTemplate.render({'fields': fields, 'grids': grids, 'objects':objects}), self.__fakeres_template.render({'output_object': output_object, 'print_objects':objects, 'trxno':self.trxno})

    def __getObjRptGrid(self, obj, gridName):
        if 'grids' not in obj.keys():
            obj['grids'] = [{'GridName':gridName,'columns':[]}]
        rptGrids = obj['grids']
        if isinstance(rptGrids, list):
            if rptGrids.__len__()>0:
                for grid in rptGrids:
                    if 'GridName' in grid.keys():
                        if grid['GridName'] == gridName:
                            return grid

    def __getRptObj(self, rptObjs, objName):
        if isinstance(rptObjs, list):
            if rptObjs.__len__() >0:
                for obj in rptObjs:
                    if 'objName' in obj.keys():
                        if obj['objName'] == objName:
                            return obj

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
        fakresFile = os.path.join(outDir, self.trxno + '.xml')
        with open(reqFile, 'w') as fw:
            fw.write(self.createReqPacket())

        respacket, fakeres = self.createResPacket()
        with open(resFile, 'w') as fw:
            fw.write(respacket)

        with open(fakresFile, 'w') as fw:
            fw.write(fakeres)
