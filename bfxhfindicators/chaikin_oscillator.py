from bfxhfindicators.indicator import Indicator
from bfxhfindicators.ema import EMA
from bfxhfindicators.accumulation_distribution import AccumulationDistribution
from math import isfinite

class ChaikinOsc(Indicator):
  def __init__(self, short, long, cache_size=None):
    self._shortEMA = EMA(short, cache_size)
    self._longEMA = EMA(long, cache_size)
    self._adl = AccumulationDistribution()

    super().__init__({
      'args': [short, long, cache_size],
      'id': 'chaikinosc',
      'name': 'ChaikinOsc(%f, %f)' % (short, long),
      'seed_period': max([short, long]),
      'data_type': 'candle',
      'data_key': '*',
      'cache_size': cache_size
    })

  def reset(self):
    super().reset()
    self._shortEMA.reset()
    self._longEMA.reset()
    self._adl.reset()

  def update(self, candle):
    self._adl.update(candle)
    adl = self._adl.v()

    if not isfinite(adl):
      return
    
    self._shortEMA.update(adl)
    self._longEMA.update(adl)

    short = self._shortEMA.v()
    long = self._longEMA.v()

    if (isfinite(short) and isfinite(long)):
      super().update(short - long)

    return self.v()

  def add(self, candle):
    self._adl.add(candle)
    adl = self._adl.v()

    if not isfinite(adl):
      return
    
    self._shortEMA.add(adl)
    self._longEMA.add(adl)

    short = self._shortEMA.v()
    long = self._longEMA.v()

    if (isfinite(short) and isfinite(long)):
      super().add(short - long)

    return self.v()
