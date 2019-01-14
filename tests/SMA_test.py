
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import SMA

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
  1.9291467585,
  18.305988257,
  20.425342303,
  22.741084812,
  22.791749098,
  22.792249098,
  22.871671511,
  22.896392083499997,
  22.9473820115,
  23.024717124,
  23.1048384805,
  23.346112686,
  23.385967264,
  23.738820392500003,
  23.857518251000002,
  24.538030632,
  24.639568505000003,
  24.745217673000003,
  25.167904573500003,
  25.2000099115
]

class SMATest(unittest.TestCase):
  def test_add(self):
    indicator = SMA([20])
    for i in range(len(expected)):
      indicator.add(candles[i]['vol'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
