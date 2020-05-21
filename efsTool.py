# -*- coding: UTF-8 -*-


from EfcBuild.faceBuild import faceBuild
from EfcBuild.javaBuild import javaBuild
from EfcBuild.messageBuild import messageBuild
from EfcBuild.EfcDef import *
from optparse import OptionParser
import json


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-t", "--trxno", dest="trxno", default="", help="trade number", metavar="TRADENO")
    parser.add_option("-c", "--catalog", dest="catalog", default="", help="efc trade catalog", metavar="CATALOG")
    (options, args) = parser.parse_args()
    trxno = options.trxno
    catalog = options.catalog
    if not trxno and not catalog:
        print('efsTool useage:python efsTool.py -cD001 -t0100')
        exit(0)
    if not catalog:
        print(u'请设定需要生成的交易分组')
        exit(0)
    fbuild = faceBuild()
    fbuild.createFace(trxno+'.xls')
    jbuild = javaBuild(catalog, trxno)
    jbuild.createJava(trxno+'.xls')
    mbuild = messageBuild(trxno)

    with open(os.path.join(fbuild.faceDir,'T'+trxno+'.face'), 'w') as fw:
        fw.write(json.dumps(fbuild.inCanvas.__dict__, encoding='UTF-8', ensure_ascii=False).encode("utf-8"))
    with open(os.path.join(fbuild.faceDir,'T'+trxno+'2.face'), 'w') as fw:
        fw.write(json.dumps(fbuild.outCanvas.__dict__, encoding='UTF-8', ensure_ascii=False).encode("utf-8"))

    with open(os.path.join(jbuild.javaDir,'T'+trxno+'.java'), 'w') as fw:
        fw.write(jbuild.javaInBuff)
    with open(os.path.join(jbuild.javaDir, 'T' + trxno + '2.java'), 'w') as fw:
        fw.write(jbuild.javaOutBuff)

    mbuild.writePacket()

