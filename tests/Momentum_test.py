
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import Momentum

with open('tests/btc_candle_data.json', 'r') as f:
  btcCandleData = json.load(f)
  candles = list(map(lambda candleArray: {
    'mts': candleArray[0],
    'open': candleArray[1],
    'close': candleArray[2],
    'high': candleArray[3],
    'low': candleArray[4],
    'vol': candleArray[5],
    'symbol': 'tBTCUSD',
    'tf': '1min',
  }, btcCandleData))

expected = [
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  -36.98050804,
  -322.71134586,
  -41.589989360000004,
  -39.25778761,
  1.3606714500000001,
  13.600247620000001,
  0.44230919999999974,
  1.61857191,
  7.4339394500000004,
  -0.9045954900000001
]

class MomentumTest(unittest.TestCase):
  def test_add(self):
    indicator = Momentum([10])
    for i in range(len(expected)):
      indicator.add(candles[i]['vol'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
