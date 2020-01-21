from bfxhfindicators.indicator import Indicator

class SMA(Indicator):
  def __init__(self, period, cache_size=None):
    self._p = period
    self._buffer = []

    super().__init__({
      'args': [period, cache_size],
      'id': 'sma',
      'name': 'SMA(%f)' % period,
      'seed_period': period,
      'cache_size': cache_size
    })
  
  def reset(self):
    super().reset()
    self._buffer = []

  def update(self, v):
    if len(self._buffer) == 0:
      self._buffer.append(v)
    else:
      self._buffer[-1] = v
    
    if len(self._buffer) < self._p:
      return
    
    super().update(sum(self._buffer) / self._p)
    return self.v()

  def add(self, v):
    self._buffer.append(v)

    if len(self._buffer) > self._p:
      del self._buffer[0]
    
    super().add(sum(self._buffer) / self._p)
    return self.v()
