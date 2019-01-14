
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import WMA

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
  19.107696475454542,
  11.026422454,
  4.203531666000001,
  2.5156848845454545,
  2.722196275090909,
  2.791011913090909,
  4.878049970181818,
  4.6124489505454545,
  4.3537561090909085,
  5.218499169272727,
  4.5277831030909095
]

class WMATest(unittest.TestCase):
  def test_add(self):
    indicator = WMA([10])
    for i in range(len(expected)):
      indicator.add(candles[i]['vol'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
