from bfxhfindicators.indicator import Indicator

class DC(Indicator):
  def __init__(self, period, cache_size=None):
    self._p = period
    self._buffer = []

    super().__init__({
      'args': [period, cache_size],
      'id': 'dc',
      'name': 'DC(%f)' % period,
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
      return
    
    maxHigh = max(map(lambda c: c['high'], self._buffer))
    minLow = min(map(lambda c: c['low'], self._buffer))

    super().update({
      'upper': maxHigh,
      'middle': (maxHigh + minLow) / 2,
      'lower': minLow
    })
    return self.v()

  def add(self, candle):
    self._buffer.append(candle)

    if len(self._buffer) > self._p:
      del self._buffer[0]
    elif len(self._buffer) < self._p:
      return
    
    maxHigh = max(map(lambda c: c['high'], self._buffer))
    minLow = min(map(lambda c: c['low'], self._buffer))

    super().add({
      'upper': maxHigh,
      'middle': (maxHigh + minLow) / 2,
      'lower': minLow
    })
    return self.v()
