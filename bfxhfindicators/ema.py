from bfxhfindicators.indicator import Indicator

class EMA(Indicator):
  def __init__(self, period, cache_size=None):
    super().__init__({
      'args': [period, cache_size],
      'id': 'ema',
      'name': 'EMA(%f)' % (period),
      'seed_period': period,
      'cache_size': cache_size
    })

    self._a = 2 / (period + 1)

  def update(self, v):
    if self.l() < 2:
      super().update(v)
    else:
      super().update((self._a * v) + ((1 - self._a) * self.prev()))

    return self.v()

  def add(self, v):
    if self.l() == 0:
      super().add(v)
    else: 
      super().add((self._a * v) + ((1 - self._a) * self.v()))

    return self.v()
