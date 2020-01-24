from bfxhfindicators.indicator import Indicator

class WilliamsR(Indicator):
  def __init__(self, period, cache_size=None):
    self._p = period
    self._buffer = []

    super().__init__({
      'args': [period, cache_size],
      'id': 'wir',
      'name': 'WR(%f)' % period,
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

    if len(self._buffer) == self._p:
      close = candle['close']
      high = max(map(lambda c: c['high'], self._buffer))
      low = min(map(lambda c: c['low'], self._buffer))

      super().update(((high - close) / (high - low)) * -100)

    return self.v()

  def add(self, candle):
    self._buffer.append(candle)

    if len(self._buffer) > self._p:
      del self._buffer[0]
    elif len(self._buffer) < self._p:
      return self.v()

    close = candle['close']
    high = max(map(lambda c: c['high'], self._buffer))
    low = min(map(lambda c: c['low'], self._buffer))

    return super().add(((high - close) / (high - low)) * -100)
