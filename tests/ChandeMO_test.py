
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import ChandeMO

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
  -95.1276504645981,
  -99.66761914433926,
  -99.24161809625339,
  -65.57468395807716,
  -43.93446173712572,
  -10.947774662411431,
  -21.25955658866002,
  0.31819051733966247,
  5.02793296089244,
  26.633165829144996,
  4.166666666666982,
  14.932126696830272
]

class ChandeMOTest(unittest.TestCase):
  def test_add(self):
    indicator = ChandeMO([9])
    for i in range(len(expected)):
      indicator.add(candles[i])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
