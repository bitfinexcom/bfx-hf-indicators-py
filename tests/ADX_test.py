
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import ADX

with open('tests/btc_candle_data.json', 'r') as f:
  btcCandleData = json.load(f)
  candles = map(lambda candleArray: {
    'mts': candleArray[0],
    'open': candleArray[1],
    'close': candleArray[2],
    'high': candleArray[3],
    'low': candleArray[4],
    'volume': candleArray[5],
    'symbol': 'tBTCUSD',
    'tf': '1min',
  }, btcCandleData)

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
  None
]

class ADXTest(unittest.TestCase):
  def test_add(self):
    indicator = ADX([14, 14])
    for i in range(len(expected)):
      indicator.add(candles[i])
      self.assertEqual(round(indicator.v(), 13), expected[i])


if __name__ == '__main__':
    unittest.main()
  
