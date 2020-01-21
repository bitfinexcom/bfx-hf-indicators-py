from math import isfinite
from collections import deque


class Indicator:
  def __init__(self, params=None):
    if not params:
        raise

    self._name = params['name']
    self._seed_period = params['seed_period']
    self._id = params['id']
    self._args = params['args']
    self._data_type = params.get('data_type') or '*'
    self._data_key = params.get('data_key') or 'close'
    self._cache_size = params.get('cache_size')
    self.reset()

  def reset(self):
    if self._cache_size:
        self._values = deque(maxlen=self._cache_size)
    else:
        self._values = []

  def l(self):
    return len(self._values)

  def v(self):
    if len(self._values) == 0:
      return None

    return self._values[-1]

  def prev(self, n = 1):
    if len(self._values) <= n:
      return None

    return self._values[-1 - n]

  def add(self, v):
    self._values.append(v)
    return v

  def update(self, v):
    if len(self._values) == 0:
      return self.add(v)

    self._values[-1] = v
    return v

  def crossed(self, target):
    if self.l() < 2:
      return False
    
    v = self.v()
    prev = self.prev()

    return (
      (v >= target and prev <= target) or
      (v <= target and prev >= target)
    )

  def ready(self):
    return len(self._values) > 0

  def get_seed_period(self):
    return self._seed_period

  def get_data_key(self):
    return self._data_key
  
  def get_data_type(self):
    return self._data_type
