from mMrs.Robot import Robot
from mMrs.sensor.Sensor import Sensor


class Csa:
    '''
    Class Collective Self-awareness
    '''
    def __init__(self ,robots:list[Robot] ,publicMemLen:float ):
        '''
        Parameters
        ----------
        robots
        publicMemLen: public mem value between
        '''
        pass

    def choosePrdCoupledGpsMdl(self):
        pass

    def choosePrdCoupledLidarMdl(self):
        pass

    def updatePrdCoupledMdl(self):
        pass

    def createPrdCoupledMdl(self):
        pass

    def addSensorVal(self, robot:Robot, sensor:Sensor, sensorVal):
        '''
         - compute abn
         - Either update or create a prd model
         - Am I being controlled?
        '''
        pass

