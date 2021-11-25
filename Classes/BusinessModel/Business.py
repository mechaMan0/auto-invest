import math
import requests
import websocket
import socket
import multiprocessing as mp
import json

from Classes.BusinessModel import StockApi, StockData
from DesignPatterns import Singleton


class MarketCalculator:
    currentValue = -1
    previousValue = -1
    dataSamplingInterval = -1  # How quickly we sample the data
    stockSamplingInterval = -1  # How quickly we can perform stock updates
    derivative = -1

    def __init__(self, dataSamplingInterval=-1, stockSamplingInterval=-1):
        self.setDataSamplingInterval(dataSamplingInterval)
        self.setStockSamplingInterval(stockSamplingInterval)

    def calculateDerivative(self):
        self.derivative = (self.currentValue - self.currentValue) / self.dataSamplingInterval
        return self.derivative

    def getDerivative(self):
        return self.derivative

    def isDerivativePositive(self):
        if self.derivative > 0:
            return True
        return False

    def setDataSamplingInterval(self, interval):
        self.dataSamplingInterval = interval

    def setStockSamplingInterval(self, interval):
        self.stockSamplingInterval = interval

    def updateAttributes(self, curr, prev):
        self.currentValue = curr
        self.previousValue = prev
        self.derivative = self.calculateDerivative()


class Business(StockData.StockData):

    def __init__(self, name="", symbol="", maxListSize=100, tradingStartHours=None, tradingEndHours=None):
        super().__init__(symbol=symbol, maxListSize=maxListSize)
        print("INIT  ")
        self.name = name
        self.tradingStartHours = tradingStartHours
        self.tradingEndHours = tradingEndHours


class EmaModel:
    """
    Class stores an erray of emas at different lengths
    """
    def __init__(self):
        self.length = -1
        self.emaArray = None # emas should be appended to this

    def checkCrossover(self, ema1, ema2):
        """
        Checks for crossover between two ema lines
        @return: -1 if negative crossover, 1 if positive crossover, 0 if no crossover
        """
        pass

    def addEma(self, ema):
        self.emaArray.append(ema)


class Ema:
    def __init__(self, length, smoothingFactor=2):
        self.emaLength = length
        self.emaArray = []
        self.smoothingFactor = smoothingFactor

    def updateEma(self, stockUpdateValue):
        """

        @param stockUpdateValue: The value of the stock price to be used to update the ema
        @return:
        """

        # check if there is a previous ema value
        if len(self.emaArray) < 2:
            emaYester = 0
        else:
            emaYester = self.emaArray[-1]

        ema = (stockUpdateValue * (self.smoothingFactor/(1+self.emaLength))) + emaYester * (1 - (self.smoothingFactor / (1 - self.emaLength)))
        self.emaArray.append(ema)


class SupportResistanceEstimator:
    def __init__(self):
        self.resistanceMinPeriod = -1
        self.resistanceMaxPeriod = -1

    def checkForSR(self, barList):
        """
        Checks a list of bars for any potential support/resistance lines
        @param barList:
        @return:
        """
        pass


class SupportResistLine:
    def __int__(self):
        self.length = -1  # Length of the support/resistance line
        self.occurrences = -1  # Number of
        self.barList = "" # An array of bars of which there are suffecient hits within the range




    """
        We can calulate the suport and resistance by looking at how many times we diverge/get close 
        to a horizontal line(within some reasonable range)
    """


class BusinessAnalyzer:
    """
    Business Analyzer analyzers business
    """
    def __init__(self):
        self.businessesList = []  # List of all of the businesses we should analyze
        self.lastHourlyVolumeAverage = -1
        self.lastThreeMinuteVolume = -1
        self.lastVolume = -1

    def analyzeBusiness(self, business):
        pass

    def updateEmas(self):
        pass


