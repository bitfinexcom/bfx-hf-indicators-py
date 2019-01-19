
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import StdDeviation

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
  19.278673791469522,
  15.11402276730208,
  7.255885088743505,
  4.885380984981626,
  3.6142262766664794,
  3.34022927041643,
  3.0174710568531817,
  2.7336884664457384,
  2.33565047853787,
  2.289995403350819,
  2.4852141705864828,
  2.553897949574687,
  2.965077437526037,
  3.3137830186565354,
  3.5063063486418518,
  3.775861700188078,
  3.7293148799322586,
  4.2650939398551895,
  5.54230381510686,
  6.60155484077725,
  7.556273099742661
]

class StdDeviationTest(unittest.TestCase):
  def test_add(self):
    indicator = StdDeviation([20])
    for i in range(len(expected)):
      indicator.add(candles[i]['close'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
