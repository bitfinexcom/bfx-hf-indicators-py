from math import isfinite
from bfxhfindicators.indicator import Indicator

class AccumulationDistribution(Indicator):
  def moneyFlowVol(candle):
    high = candle['high']
    low = candle['low']
    close = candle['close']
    vol = candle['vol']
    moneyFlowMult = 0

    if high != low:
      moneyFlowMult = ((close - low) - (high - close)) / (high - low)

    return moneyFlowMult * vol
  
  def __init__(self, cache_size=None):
    super().__init__({
      'args': [cache_size],
      'id': 'ad',
      'name': 'Accum/Dist',
      'seed_period': 0,
      'data_type': 'candle',
      'data_key': '*',
      'cache_size': cache_size
    })

  def update(self, candle):
    moneyFlowVol = AccumulationDistribution.moneyFlowVol(candle)
    prev = self.prev()

    if isfinite(prev):
      super().update(prev + moneyFlowVol)
    else:
      super().update(moneyFlowVol)

    return self.v()

  def add(self, candle):
    moneyFlowVol = AccumulationDistribution.moneyFlowVol(candle)
    prev = self.v()

    if isfinite(prev):
      super().add(prev + moneyFlowVol)
    else:
      super().add(moneyFlowVol)

    return self.v()
