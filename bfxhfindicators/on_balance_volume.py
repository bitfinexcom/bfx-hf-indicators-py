from bfxhfindicators.indicator import Indicator

class OBV(Indicator):
  def __init__(self, args=None):
    if not args:
        args = []

    self._lastCandle = None

    super().__init__({
      'args': args,
      'id': 'obv',
      'name': 'OBV',
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
    v = self.prev() if self.l() > 1 else 0
    obv = v

    if close > self._lastCandle['close']:
      obv = v + vol
    elif close < self._lastCandle['close']:
      obv = v - vol

    return super().update(obv)

  def add(self, candle):
    if self._lastCandle == None:
      self._lastCandle = candle
      return self.v()
    
    close = candle['close']
    vol = candle['vol']
    v = self.v() if self.l() > 0 else 0
    obv = v

    if close > self._lastCandle['close']:
      obv = v + vol
    elif close < self._lastCandle['close']:
      obv = v - vol

    super().add(obv)

    self._lastCandle = candle

    return self.v()
