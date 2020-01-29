
import unittest
import sys
import json

sys.path.append('../')
from tests.util import assertFloatEqual
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
  6425.7527272727275,
  6429.160000000001,
  6432.12909090909,
  6433.874545454546,
  6434.994545454545,
  6435.434545454545,
  6436.105454545454,
  6436.114545454545,
  6436.403636363635,
  6436.061818181819,
  6436.470909090908,
  6436.867272727273,
  6436.879999999999,
  6436.932727272727,
  6436.692727272726,
  6435.834545454547,
  6435.041818181818,
  6434.169090909092,
  6434.130909090908,
  6434.1272727272735,
  6435.036363636364
]

class WMATest(unittest.TestCase):
  def test_add(self):
    indicator = WMA([10])
    for i in range(len(expected)):
      indicator.add(candles[i]['close'])
      assertFloatEqual(self, indicator.v(), expected[i], 'candles[%d]' % i)

if __name__ == '__main__':
    unittest.main()
  
