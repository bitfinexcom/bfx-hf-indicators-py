from bfxhfindicators.indicator import Indicator

class NetVolume(Indicator):
  def __init__(self, args=None):
    if not args:
        args = []

    super().__init__({
      'args': args,
      'id': 'nv',
      'name': 'Net Volume',
      'seed_period': 0,
      'data_type': 'candle',
      'data_key': '*'
    })

  def update(self, candle):
    vol = candle['vol']

    if candle['close'] >= candle['open']:
      return super().update(vol)
    else:
      return super().update(-vol)

  def add(self, candle):
    vol = candle['vol']

    if candle['close'] >= candle['open']:
      return super().add(vol)
    else:
      return super().add(-vol)
