
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import DC

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
  None,
  None,
  {
    "upper": 6439.50026496,
    "middle": 6402.75013248,
    "lower": 6366
  }
]

class DCTest(unittest.TestCase):
  def test_add(self):
    indicator = DC([20])
    for i in range(len(expected)):
      indicator.add(candles[i])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
