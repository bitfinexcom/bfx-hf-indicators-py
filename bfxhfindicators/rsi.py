from bfxhfindicators.indicator import Indicator
from bfxhfindicators.ema import EMA
from math import isfinite

class RSI(Indicator):
  def __init__(self, period, cache_size=None):
    self._p = period
    self._uEMA = EMA(period, cache_size)
    self._dEMA = EMA(period, cache_size)
    self._prevInputValue = None
 
    super().__init__({
      'args': [period, cache_size],
      'id': 'rsi',
      'name': 'RSI(%f)' % (period),
      'seed_period': period,
      'cache_size': cache_size
    })

  def reset(self):
    super().reset()

    self._prevInputValue = None
    self._uEMA.reset()
    self._dEMA.reset()

  def _ud (self, v):
    delta = 0
    
    if self._prevInputValue != None:
      delta = v - self._prevInputValue

    return {
      'u': delta if delta > 0 else 0,
      'd': -delta if delta < 0 else 0
    }

  def _rs (self):
    uAvg = self._uEMA.v()
    dAvg = self._dEMA.v()

    if not isfinite(uAvg) or not isfinite(dAvg) or dAvg == 0:
      return None
    else:
      return uAvg / dAvg


  def update(self, v):
    if self._prevInputValue == None:
      return

    ud = self._ud(v)
    self._uEMA.update(ud['u'])
    self._dEMA.update(ud['d'])
    rs = self._rs()

    if rs is not None:
      super().update(100 - (100 / (1 + rs)))

    return self.v()

  def add(self, v):
    if self._prevInputValue == None:
      self._prevInputValue = v
    
    ud = self._ud(v)
    self._uEMA.add(ud['u'])
    self._dEMA.add(ud['d'])
    rs = self._rs()

    if rs is not None:
      super().add(100 - (100 / (1 + rs)))
      self._prevInputValue = v

    return self.v()
