from bfxhfindicators.indicator import Indicator
from bfxhfindicators.sma import SMA
from bfxhfindicators.stddev import StdDeviation

class BollingerBands(Indicator):
  def __init__(self, period, mul, cache_size=None):
    self._p = period
    self._m = mul
    self._sma = SMA(period, cache_size)
    self._stddev = StdDeviation([period])

    super().__init__({
      'args': [period, mul, cache_size],
      'id': 'bbands',
      'name': 'BBANDS(%f, %f)' % (period, mul),
      'seed_period': period
    })

  def reset(self):
    super().reset()
    self._sma.reset()
    self._stddev.reset()

  def update(self, v):
    self._sma.update(v)
    self._stddev.update(v)

    middle = self._sma.v()
    stddev = self._stddev.v()

    super().update({
      'top': middle + (self._m * stddev),
      'middle': middle,
      'bottom': middle - (self._m * stddev)
    })

    return self.v()

  def add(self, v):
    self._sma.add(v)
    self._stddev.add(v)

    middle = self._sma.v()
    stddev = self._stddev.v()

    super().add({
      'top': middle + (self._m * stddev),
      'middle': middle,
      'bottom': middle - (self._m * stddev)
    })

    return self.v()
