from bfxhfindicators.indicator import Indicator
from bfxhfindicators.sma import SMA
from math import isfinite

class EOM(Indicator):
  def __init__(self, divisor, length, cache_size=None):
    self._d = divisor
    self._sma = SMA(length, cache_size)
    self._lastCandle = None

    super().__init__({
      'args': [divisor, length, cache_size],
      'id': 'eom',
      'name': 'EOM(%f, %f)' % (divisor, length),
      'seed_period': length,
      'data_type': 'candle',
      'data_key': '*',
      'cache_size': cache_size
    })

  def reset(self):
    super().reset()
    self._lastCandle = None
    self._sma.reset()

  def calcEOM(candle, lastCandle, divisor):
    high = candle['high']
    low = candle['low']
    vol = candle['vol']
    lastHigh = lastCandle['high']
    lastLow = lastCandle['low']

    moved = ((high + low) / 2) - ((lastHigh + lastLow) / 2)

    if high == low:
      boxRatio = 1
    else:
      boxRatio = (vol / divisor) / (high - low)

    return moved / boxRatio
 
  def update(self, candle):
    if self._lastCandle == None:
      return
    
    eom = EOM.calcEOM(candle, self._lastCandle, self._d)
    self._sma.update(eom)

    v = self._sma.v()

    if isfinite(v):
      super().update(v)
    return self.v()

  def add(self, candle):
    if self._lastCandle == None:
      self._lastCandle = candle
      return
    
    eom = EOM.calcEOM(candle, self._lastCandle, self._d)
    self._sma.add(eom)

    v = self._sma.v()

    if isfinite(v):
      super().add(v)
    
    self._lastCandle = candle
    return self.v()
