from bfxhfindicators.indicator import Indicator
from bfxhfindicators.sma import SMA
from math import floor

class DPO(Indicator):
  def __init__(self, period, cache_size=None):
    self._pricePeriod = floor(period / 2) + 1
    self._sma = SMA(period, cache_size)

    super().__init__({
      'args': [period, cache_size],
      'id': 'dpo',
      'name': 'DPO(%f)' % period,
      'seed_period': period,
      'cache_size': cache_size
    })
  
  def reset(self):
    super().reset()
    self._sma.reset()

  def update(self, v):
    self._sma.update(v)
    super().update(v - self._sma.prev(self._pricePeriod - 1))
    return self.v()

  def add(self, v):
    self._sma.add(v)

    if self._sma.l() < self._pricePeriod + 1:
      return

    super().add(v - self._sma.prev(self._pricePeriod))
    return self.v()
