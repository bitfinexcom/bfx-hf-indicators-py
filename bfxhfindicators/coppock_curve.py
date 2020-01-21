from bfxhfindicators.indicator import Indicator
from bfxhfindicators.wma import WMA
from bfxhfindicators.roc import ROC
from math import isfinite

class CoppockCurve(Indicator):
  def __init__(self, wmaLength, longROCLength, shortROCLength, cache_size=None):
    self._wma = WMA([wmaLength])
    self._shortROC = ROC([shortROCLength])
    self._longROC = ROC([longROCLength])

    super().__init__({
      'args': [wmaLength, longROCLength, shortROCLength, cache_size],
      'id': 'coppockcurve',
      'name': 'Coppock Curve(%f, %f, %f)' % (wmaLength, longROCLength, shortROCLength),
      'seed_period': max([longROCLength + wmaLength, shortROCLength + wmaLength]),
      'cache_size': cache_size
    })
  
  def reset(self):
    super().reset()
    self._wma.reset()
    self._shortROC.reset()
    self._longROC.reset()

  def update(self, v):
    self._shortROC.update(v)
    self._longROC.update(v)

    short = self._shortROC.v()
    long = self._longROC.v()

    if not isfinite(short) or not isfinite(long):
      return
    
    self._wma.update(short + long)
    super().update(self._wma.v())
    return self.v()

  def add(self, v):
    self._shortROC.add(v)
    self._longROC.add(v)

    short = self._shortROC.v()
    long = self._longROC.v()

    if not isfinite(short) or not isfinite(long):
      return
    
    self._wma.add(short + long)
    super().add(self._wma.v())
    return self.v()
