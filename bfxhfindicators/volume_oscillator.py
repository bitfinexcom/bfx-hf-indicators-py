from bfxhfindicators.indicator import Indicator
from bfxhfindicators.ema import EMA

class VO(Indicator):
  def __init__(self, shortPeriod, longPeriod, cache_size=None):
    self._shortEMA = EMA(shortPeriod, cache_size)
    self._longEMA = EMA(longPeriod, cache_size)

    super().__init__({
      'args': [shortPeriod, longPeriod, cache_size],
      'id': 'vo',
      'name': 'VO(%f, %f)' % (shortPeriod, longPeriod),
      'seed_period': longPeriod,
      'data_type': 'candle',
      'data_key': '*',
      'cache_size': cache_size
    })
  
  def reset(self):
    super().reset()
    self._shortEMA.reset()
    self._longEMA.reset()

  def update(self, candle):
    vol = candle['vol']

    self._shortEMA.update(vol)
    self._longEMA.update(vol)

    short = self._shortEMA.v()
    long = self._longEMA.v()

    if long == 0:
      return super().update(0)
    
    return super().update(((short - long) / long) * 100)

  def add(self, candle):
    vol = candle['vol']

    self._shortEMA.add(vol)
    self._longEMA.add(vol)

    short = self._shortEMA.v()
    long = self._longEMA.v()

    if long == 0:
      return super().add(0)
    
    return super().add(((short - long) / long) * 100)
