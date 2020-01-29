
import unittest
import sys
import json

sys.path.append('../')
from tests.util import assertFloatEqual
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
  60.100000000000364,
  65.30000000000018,
  28.399999999999636,
  17.399999999999636,
  7.299999999999272,
  9.399999999999636,
  6.599999999999454,
  7.699999999999818,
  0.6999999999998181,
  3.699999999999818,
  4.099999999999454,
  -1.199999999999818,
  -0.8999999999996362,
  -2,
  -3.5999999999994543,
  -5.599999999999454,
  -3.899999999999636,
  -1.8999999999996362,
  0.8000000000001819,
  1.7000000000007276
]

class MomentumTest(unittest.TestCase):
  def test_add(self):
    indicator = Momentum([10])
    for i in range(len(expected)):
      indicator.add(candles[i]['close'])
      assertFloatEqual(self, indicator.v(), expected[i], 'candles[%d]' % i)

if __name__ == '__main__':
    unittest.main()
  
