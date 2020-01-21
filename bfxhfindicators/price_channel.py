from bfxhfindicators.indicator import Indicator

class PC(Indicator):
  def __init__(self, period, offset, cache_size=None):
    self._p = period
    self._offset = offset
    self._l = period + offset
    self._buffer = []

    super().__init__({
      'args': [period, offset, cache_size],
      'id': 'pc',
      'name': 'PC(%f, %f)' % (period, offset),
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

    if len(self._buffer) < self._l:
      return super().update(0)

    upper = max(map(lambda c: c['high'], self._buffer[0:self._p]))
    lower = min(map(lambda c: c['low'], self._buffer[0:self._p]))

    return super().update({
      'upper': upper,
      'center': (upper + lower) / 2,
      'lower': lower
    })

  def add(self, candle):
    self._buffer.append(candle)

    if len(self._buffer) > self._l:
      del self._buffer[0]
    elif len(self._buffer) < self._l:
      return self.v()

    upper = max(map(lambda c: c['high'], self._buffer[0:self._p]))
    lower = min(map(lambda c: c['low'], self._buffer[0:self._p]))

    return super().add({
      'upper': upper,
      'center': (upper + lower) / 2,
      'lower': lower
    })
