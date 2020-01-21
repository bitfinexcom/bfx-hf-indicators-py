from bfxhfindicators.indicator import Indicator
from bfxhfindicators.roc import ROC
from math import isfinite

class Acceleration(Indicator):
  def __init__(self, period, cache_size=None):
    self._p = period
    self._roc = ROC(period, cache_size)
    self._buffer = []
 
    super().__init__({
      'args': [period, cache_size],
      'id': 'acc',
      'name': 'Acceleration(%f)' % (period),
      'seed_period': period,
      'cache_size': cache_size
    })

  def reset(self):
    super().reset()

    self._buffer = []
    self._roc.reset()

  def update(self, v):
    self._roc.update(v)
    roc = self._roc.v()

    if not isfinite(roc):
      return

    if len(self._buffer) == 0:
      self._buffer.append(roc)
    else:
      self._buffer[-1] = roc

    if len(self._buffer) < self._p:
      return
    
    super().update(roc - self._buffer[0])
    return self.v()

  def add(self, v):
    self._roc.add(v)
    roc = self._roc.v()

    if not isfinite(roc):
      return

    if len(self._buffer) == self._p:
      super().add(roc - self._buffer[0])

    self._buffer.append(roc)

    if len(self._buffer) > self._p:
      del self._buffer[0]

    return self.v()
