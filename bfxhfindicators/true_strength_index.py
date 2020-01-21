from bfxhfindicators.indicator import Indicator
from bfxhfindicators.ema import EMA

class TSI(Indicator):
  def __init__(self, long, short, signal, cache_size=None):
    self._pcEMA = EMA(long, cache_size)
    self._pc2EMA = EMA(short, cache_size)
    self._apcEMA = EMA(long, cache_size)
    self._apc2EMA = EMA(short, cache_size)
    self._sEMA = EMA(signal, cache_size)
    self._lastPrice = None

    super().__init__({
      'args': [short, signal, cache_size],
      'id': 'tsi',
      'name': 'TSI(%f, %f, %f)' % (long, short, signal),
      'seed_period': max([long, short, signal]),
      'cache_size': cache_size
    })
  
  def reset(self):
    super().reset()
    self._pcEMA.reset()
    self._pc2EMA.reset()
    self._apcEMA.reset()
    self._apc2EMA.reset()
    self._sEMA.reset()
    self._lastPrice = None

  def update(self, v):
    if self._lastPrice == None:
      return self.v()
    
    pc = v - self._lastPrice
    apc = abs(v - self._lastPrice)

    self._pcEMA.update(pc)
    self._apcEMA.update(apc)

    if self._pcEMA.ready():
      self._pc2EMA.update(self._pcEMA.v())
    else:
      return self.v()
    
    if self._apcEMA.ready():
      self._apc2EMA.update(self._apcEMA.v())
    else:
      return self.v()
    
    if not self._pc2EMA.ready() or not self._apc2EMA.ready():
      return self.v()
    
    tsi = 100 * (self._pc2EMA.v() / self._apc2EMA.v())
    self._sEMA.update(tsi)

    return super().update({
      'v': tsi,
      'signal': self._sEMA.v()
    })

  def add(self, v):
    if self._lastPrice == None:
      self._lastPrice = v
      return self.v()
    
    pc = v - self._lastPrice
    apc = abs(v - self._lastPrice)

    self._pcEMA.add(pc)
    self._apcEMA.add(apc)

    if self._pcEMA.ready():
      self._pc2EMA.add(self._pcEMA.v())
    else:
      return self.v()
    
    if self._apcEMA.ready():
      self._apc2EMA.add(self._apcEMA.v())
    else:
      return self.v()
    
    if not self._pc2EMA.ready() or not self._apc2EMA.ready():
      return self.v()
    
    tsi = 100 * (self._pc2EMA.v() / self._apc2EMA.v())
    self._sEMA.add(tsi)

    super().add({
      'v': tsi,
      'signal': self._sEMA.v()
    })

    self._lastPrice = v
    return self.v()
