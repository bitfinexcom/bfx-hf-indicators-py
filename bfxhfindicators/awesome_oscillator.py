from bfxhfindicators.indicator import Indicator
from bfxhfindicators.sma import SMA

class AO(Indicator):
  def __init__(self, period, cache_size=None):
    self._smaShort = SMA(period, cache_size)
    self._smaLong = SMA(period, cache_size)

    super().__init__({
      'args': [period, cache_size],
      'id': 'ao',
      'name': 'AO',
      'seed_period': None,
      'data_type': 'candle',
      'data_key': '*',
      'cache_size': cache_size
    })

  def reset(self):
    super().reset()

    self._smaShort.reset()
    self._smaLong.reset()

  def update(self, candle):
    v = (candle['high'] + candle['low']) / 2

    self._smaShort.update(v)
    self._smaLong.update(v)

    super().update(self._smaShort.v() - self._smaLong.v())
    return self.v()

  def add(self, candle):
    v = (candle['high'] + candle['low']) / 2

    self._smaShort.add(v)
    self._smaLong.add(v)

    super().add(self._smaShort.v() - self._smaLong.v())
    return self.v()
   