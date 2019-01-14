
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import TRIX

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
  87.34991236364786,
  146.9817397364359,
  185.01919237023935,
  192.9217827751284,
  179.67491673259283,
  153.0768193984544,
  118.05421209897472,
  78.52479500238817,
  37.14401180869187,
  -4.463981013987928,
  -44.41119206500477,
  -83.4184147965178,
  -119.29271044166856,
  -153.50784376492288,
  -182.77579051135694,
  -211.11668861023668,
  -238.29944984365304,
  -262.3157823316946,
  -285.9094403002893
]

class TRIXTest(unittest.TestCase):
  def test_add(self):
    indicator = TRIX([18])
    for i in range(len(expected)):
      indicator.add(candles[i]['vol'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
