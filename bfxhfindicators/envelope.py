from bfxhfindicators.indicator import Indicator
from bfxhfindicators.sma import SMA
from math import isfinite

class Envelope(Indicator):
  def __init__(self, length, percent, cache_size=None):
    self._sma = SMA(length, cache_size)
    self._p = percent / 100

    super().__init__({
      'args': [length, percent, cache_size],
      'id': 'env',
      'name': 'Env(%f, %f)' % (length, percent),
      'seed_period': length,
      'cache_size': cache_size
    })
  
  def reset(self):
    super().reset()
    self._sma.reset()

  def update(self, v):
    self._sma.update(v)
    basis = self._sma.v()

    if not isfinite(basis):
      return
    
    delta = basis * self._p
    super().update({
      'upper': basis + delta,
      'basis': basis,
      'lower': basis - delta
    })

    return self.v()

  def add(self, v):
    self._sma.add(v)
    basis = self._sma.v()

    if not isfinite(basis):
      return
    
    delta = basis * self._p
    super().add({
      'upper': basis + delta,
      'basis': basis,
      'lower': basis - delta
    })

    return self.v()
