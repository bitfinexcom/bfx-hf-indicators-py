from bfxhfindicators.indicator import Indicator
from bfxhfindicators.ema import EMA

class PPO(Indicator):
  def __init__(self, shortPeriod, longPeriod, cache_size=None):

    self._shortEMA = EMA(shortPeriod, cache_size)
    self._longEMA = EMA(longPeriod, cache_size)
    self._signalEMA = EMA(9, cache_size)

    super().__init__({
      'args': [shortPeriod, longPeriod, cache_size],
      'id': 'ppo',
      'name': 'PPO(%f, %f)' % (shortPeriod, longPeriod),
      'seed_period': longPeriod,
      'cache_size': cache_size
    })

  def reset(self):
    super().reset()
    self._shortEMA.reset()
    self._longEMA.reset()
    self._signalEMA.reset()

  def update(self, v):
    self._shortEMA.update(v)
    self._longEMA.update(v)

    short = self._shortEMA.v()
    long = self._longEMA.v()
    ppo = 0 if long == 0 else ((short - long) / long) * 100

    self._signalEMA.update(ppo)

    return super().update(self._signalEMA.v())

  def add(self, v):
    self._shortEMA.add(v)
    self._longEMA.add(v)

    short = self._shortEMA.v()
    long = self._longEMA.v()
    ppo = 0 if long == 0 else ((short - long) / long) * 100

    self._signalEMA.add(ppo)

    return super().add(self._signalEMA.v())
