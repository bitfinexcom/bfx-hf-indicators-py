from bfxhfindicators.indicator import Indicator

class VWAP(Indicator):
  def __init__(self, args=None):
    if not args:
        args = []

    self._totalNum = 0
    self._totalDen = 0
    self._lastNum = 0
    self._lastDen = 0

    super().__init__({
      'args': args,
      'id': 'vwap',
      'name': 'VWAP',
      'seed_period': 0,
      'data_type': 'candle',
      'data_key': '*'
    })
  
  def reset(self):
    super().reset()
    self._totalNum = 0
    self._totalDen = 0
    self._lastNum = 0
    self._lastDen = 0

  def update(self, candle):
    typ = (candle['high'] + candle['low'] + candle['close']) / 3

    self._totalDen = self._lastDen
    self._totalNum = self._lastNum
    self._totalNum += typ * candle['vol']
    self._totalDen += candle['vol']

    return super().update(self._totalNum / self._totalDen)

  def add(self, candle):
    typ = (candle['high'] + candle['low'] + candle['close']) / 3

    self._lastDen = self._totalDen
    self._lastNum = self._totalNum
    self._totalNum += typ * candle['vol']
    self._totalDen += candle['vol']

    return super().add(self._totalNum / self._totalDen)

