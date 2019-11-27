# -*- coding: UTF-8 -*-
# @Anthor : alexuh
# @Email : alexuh@zamplus.com
# @Created: 2019/08/01

class strategyContext:

    def __init__(self, strategy):
        self.strategy = strategy

    def createExe(self, **kwargs):
        self.strategy.create()

    def listExe(self, **kwargs):
        self.list(**kwargs)

    def deleteExe(self, **kwargs):
        self.delete(**kwargs)

    def saveExe(self, **kwargs):
        self.save(**kwargs)