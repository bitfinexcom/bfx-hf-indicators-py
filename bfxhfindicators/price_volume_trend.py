from bfxhfindicators.indicator import Indicator

class PVT(Indicator):
  def __init__(self, args=None):
    if not args:
        args = []

    self._lastCandle = None

    super().__init__({
      'args': args,
      'id': 'pvt',
      'name': 'PVT',
      'seed_period': 0,
      'data_type': 'candle',
      'data_key': '*'
    })
  
  def reset(self):
    super().reset()
    self._lastCandle = None

  def update(self, candle):
    if self._lastCandle == None:
      return self.v()
    
    close = candle['close']
    vol = candle['vol']
    pvt = ((close - self._lastCandle['close']) / self._lastCandle['close']) * vol
    v = self.prev() if self.l() > 1 else 0

    return super().update(pvt + v)

  def add(self, candle):
    if self._lastCandle == None:
      self._lastCandle = candle
      return self.v()
    
    close = candle['close']
    vol = candle['vol']
    pvt = ((close - self._lastCandle['close']) / self._lastCandle['close']) * vol
    v = self.v() if self.l() > 0 else 0

    super().add(pvt + v)

    self._lastCandle = candle

    return self.v()
