from bfxhfindicators.indicator import Indicator

class Momentum(Indicator):
  def __init__(self, period, cache_size=None):
    self._p = period
    self._buffer = []

    super().__init__({
      'args': [period, cache_size],
      'id': 'mo',
      'name': 'MO(%f)' % period,
      'seed_period': period,
      'cache_size': cache_size
    })

  def reset(self):
    super().reset()
    self._buffer = []
    self._values = [0]

  def update(self, v):
    if len(self._buffer) == 0:
      self._buffer.append(v)
    else:
      self._buffer[-1] = v

    if len(self._buffer) < self._p:
      return self.v()
    
    return super().update(v - self._buffer[0])

  def add(self, v):
    if len(self._buffer) == self._p:
      super().add(v - self._buffer[0])
    
    self._buffer.append(v)

    if len(self._buffer) > self._p:
      del self._buffer[0]
    
    return self.v()
