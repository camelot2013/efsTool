# -*- coding: UTF-8 -*-


from configparser import *
import os
import sys
import xlrd


def getDefTable(defDir, defFile, sheet_name):
    defFilePath = os.path.join(defDir, defFile)
    if os.path.exists(defFilePath):
        data = xlrd.open_workbook(defFilePath)
        try:
            table = data.sheet_by_name(sheet_name)
        except xlrd.biffh.XLRDError, err1:
            print err1.message
            exit(0)
    return table


def getDefDir(section, key):
    try:
        conf = ConfigParser()
        conf.read(os.environ['EFCBUILD'], encoding='UTF-8')
    except KeyError:
        exit(0)
    return conf.get(section, key)