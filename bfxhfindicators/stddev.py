from bfxhfindicators.indicator import Indicator
from math import pow, sqrt

class StdDeviation(Indicator):
  def __init__(self, period, cache_size=None):
    self._p = period
    self._buffer = []

    super().__init__({
      'args': [period, cache_size],
      'id': 'stddev',
      'name': 'STDDEV(%f)' % period,
      'seed_period': period,
      'cache_size': cache_size
    })

  def reset(self):
    super().reset()
    self._buffer = []

  def bufferStdDev(buffer, p):
    if len(buffer) < p:
      return 0

    avg = sum(buffer) / len(buffer)
    dev = list(map(lambda v: pow(v - avg, 2), buffer))
    variance = sum(dev) / (p - 1)

    return sqrt(variance)

  def update(self, v):
    if len(self._buffer) == 0:
      self._buffer.append(v)
    else:
      self._buffer[-1] = v

    if len(self._buffer) < self._p:
      return

    super().update(StdDeviation.bufferStdDev(self._buffer, self._p))
    return self.v()

  def add(self, v):
    self._buffer.append(v)

    if len(self._buffer) > self._p:
      del self._buffer[0]
    elif len(self._buffer) <= self._p:
      return

    super().add(StdDeviation.bufferStdDev(self._buffer, self._p))

    return self.v()
