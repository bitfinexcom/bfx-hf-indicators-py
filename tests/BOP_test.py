
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import BOP

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
  0.22388059701493146,
  -0.8368298368298567,
  -0.7375886524822247,
  -1,
  0,
  1,
  -0.8704364307685556,
  -1,
  -0.923076923076654,
  0.9241624869832157,
  -0.777777777777628,
  1,
  -0.205882352941145,
  0.6034207099394012,
  -1,
  0.7647058823528625,
  -0.961538461538327,
  1,
  -0.7924528301887537,
  1
]

class BOPTest(unittest.TestCase):
  def test_add(self):
    indicator = BOP([])
    for i in range(len(expected)):
      indicator.add(candles[i])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
