
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import StochasticRSI

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
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  {
    "v": 0.08195377756769605,
    "signal": 0.02731792585589868
  },
  {
    "v": 6.7718476399514005,
    "signal": 2.2846004725063653
  },
  {
    "v": 6.7718476399514005,
    "signal": 4.541883019156832
  }
]

class StochasticRSITest(unittest.TestCase):
  def test_add(self):
    indicator = StochasticRSI([14, 14, 3, 3])
    for i in range(len(expected)):
      indicator.add(candles[i]['vol'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
