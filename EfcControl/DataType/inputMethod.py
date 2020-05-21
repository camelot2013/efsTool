# -*- coding: UTF-8 -*-


class inputMethod(object):
    @property
    def normal(self):
        return "normal"
    
    @property
    def notempty(self):
        return "notempty"

    @property
    def readonly(self):
        return "readonly"