from bfxhfindicators.indicator import Indicator

class ROC(Indicator):
  def __init__(self, period, cache_size=None):
    super().__init__({
      'args': [period, cache_size],
      'id': 'roc',
      'name': 'ROC(%f)' % (period),
      'seed_period': period,
      'cache_size': cache_size
    })

    self._p = period
    self._buffer = []
  
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
    
    super().update(((v - self._buffer[0]) / self._buffer[0]) * 100)
    return self.v()

  def add(self, v):
    if len(self._buffer) == self._p:
      super().add(((v - self._buffer[0]) / self._buffer[0]) * 100)
    
    self._buffer.append(v)

    if len(self._buffer) > self._p:
      del self._buffer[0]

    return self.v()
