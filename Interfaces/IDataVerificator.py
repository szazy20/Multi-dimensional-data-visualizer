from abc import ABCMeta, abstractmethod

# base interface for data verificator
class IDataVerificator:

    @abstractmethod
    def verifyData(self):
        raise NotImplementedError