from bfxhfindicators.indicator import Indicator
from bfxhfindicators.ema import EMA
from bfxhfindicators.stddev import StdDeviation
from math import isfinite

class RVI(Indicator):
  def __init__(self, period, cache_size=None):
    self._stddev = StdDeviation(period, cache_size)
    self._uEMA = EMA(period, cache_size)
    self._dEMA = EMA(period, cache_size)
    self._prevInputValue = None

    super().__init__({
      'args': [period, cache_size],
      'id': 'rvi',
      'name': 'RVI(%f)' % period,
      'seed_period': period,
      'cache_size': cache_size
    })

  def reset(self):
    super().reset()
    self._prevInputValue = None
    self._stddev.reset()
    self._uEMA.reset()
    self._dEMA.reset()

  def ud(candlePrice, prevCandlePrice, stddev):
    if prevCandlePrice == None:
      return [0, 0]
    elif candlePrice > prevCandlePrice:
      return [stddev, 0]
    elif candlePrice < prevCandlePrice:
      return [0, stddev]
    else:
      return [0, 0]

  def update(self, v):
    if self._prevInputValue == None:
      return self.v()

    self._stddev.update(v)
    stddev = self._stddev.v()

    if not isfinite(stddev):
      return self.v()
    
    [u, d] = RVI.ud(v, self._prevInputValue, stddev)

    self._uEMA.update(u)
    self._dEMA.update(d)

    uSum = self._uEMA.v()
    dSum = self._dEMA.v()

    if uSum == dSum:
      return super().update(0)
    else:
      return super().update(100 * (uSum / (uSum + dSum)))

  def add(self, v):
    if self._prevInputValue == None:
      self._prevInputValue = v
      return self.v()

    self._stddev.add(v)
    stddev = self._stddev.v()

    if not isfinite(stddev):
      return self.v()
    
    [u, d] = RVI.ud(v, self._prevInputValue, stddev)

    self._uEMA.add(u)
    self._dEMA.add(d)

    uSum = self._uEMA.v()
    dSum = self._dEMA.v()

    if uSum == dSum:
      super().add(0)
    else:
      super().add(100 * (uSum / (uSum + dSum)))
    
    self._prevInputValue = v

    return self.v()
