
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import EMA

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
  38.58293517,
  66.10235372238094,
  63.843756312630376,
  62.17433668095129,
  56.34947468467022,
  50.98381042898735,
  46.279490222417124,
  41.91900652980597,
  38.02384386601493,
  34.54983037877541,
  31.41198245032061,
  28.879934989337695,
  26.205378472257916,
  24.381729338709544,
  22.285751036927685,
  21.459512616267904,
  19.60915498233763,
  17.942852923067377,
  17.039127693251437,
  15.477506651989396
]

class EMATest(unittest.TestCase):
  def test_add(self):
    indicator = EMA([20])
    for i in range(len(expected)):
      indicator.add(candles[i]['vol'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
