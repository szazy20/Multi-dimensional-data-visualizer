from abc import ABCMeta, abstractmethod

# base interface for all kinds of plots
class IPlot:

    @abstractmethod
    def createPlot(self):
        raise NotImplementedError