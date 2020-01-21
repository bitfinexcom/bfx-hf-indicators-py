from bfxhfindicators.indicator import Indicator
from bfxhfindicators.ema import EMA
from math import isfinite

class TRIX(Indicator):
  def __init__(self, period, cache_size=None):
    self._emaFirst = EMA(period, cache_size)
    self._emaSecond = EMA(period, cache_size)
    self._emaThird = EMA(period, cache_size)

    super().__init__({
      'args': [period, cache_size],
      'id': 'trix',
      'name': 'TRIX(%f)' % (period),
      'seed_period': (period * 3) + 1,
      'cache_size': cache_size
    })
  
  def reset(self):
    super().reset()
    self._emaFirst.reset()
    self._emaSecond.reset()
    self._emaThird.reset()

  def update(self, v):
    self._emaFirst.update(v)
    self._emaSecond.update(self._emaFirst.v())
    self._emaThird.update(self._emaSecond.v())

    curr = self._emaThird.v()

    if not isfinite(curr) or self._emaThird.l() < 2:
      return self.v()

    prev = self._emaThird.prev()
   
    return super().update(((curr / prev) - 1) * 10000)

  def add(self, v):
    self._emaFirst.add(v)
    self._emaSecond.add(self._emaFirst.v())
    self._emaThird.add(self._emaSecond.v())

    curr = self._emaThird.v()

    if not isfinite(curr) or self._emaThird.l() < 2:
      return self.v()

    prev = self._emaThird.prev()
   
    return super().add(((curr / prev) - 1) * 10000)
