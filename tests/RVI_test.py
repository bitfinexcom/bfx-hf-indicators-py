
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import RVI

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
  0,
  3.8067290654807318,
  3.672417873494655,
  4.3103861416304445,
  4.276172964199174,
  5.993897393627449,
  5.865887016913476,
  8.201486636552422,
  10.993049696872273,
  10.591741358096257
]

class RVITest(unittest.TestCase):
  def test_add(self):
    indicator = RVI([10])
    for i in range(len(expected)):
      indicator.add(candles[i]['vol'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
