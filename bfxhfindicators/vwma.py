from bfxhfindicators.indicator import Indicator

class VWMA(Indicator):
  def __init__(self, period, cache_size=None):
    self._p = period
    self._buffer = []

    super().__init__({
      'args': [period, cache_size],
      'id': 'vwma',
      'name': 'VWMA(%f)' % period,
      'seed_period': period,
      'data_type': 'candle',
      'data_key': '*',
      'cache_size': cache_size
    })
  
  def reset(self):
    super().reset()
    self._buffer = []

  def update(self, candle):
    if len(self._buffer) == 0:
      self._buffer.append(candle)
    else:
      self._buffer[-1] = candle

    if len(self._buffer) < self._p:
      return self.v()
    
    volSum = 0
    _sum = 0

    for i in range(len(self._buffer)):
      volSum += self._buffer[i]['vol']

    for i in range(len(self._buffer)):
      c = self._buffer[i]
      _sum += (c['close'] * c['vol']) / volSum

    super().update(_sum)

  def add(self, candle):
    self._buffer.append(candle)

    if len(self._buffer) > self._p:
      del self._buffer[0]
    elif len(self._buffer) < self._p:
      return self.v()
    
    volSum = 0
    _sum = 0

    for i in range(len(self._buffer)):
      volSum += self._buffer[i]['vol']

    for i in range(len(self._buffer)):
      c = self._buffer[i]
      _sum += (c['close'] * c['vol']) / volSum

    super().add(_sum)
