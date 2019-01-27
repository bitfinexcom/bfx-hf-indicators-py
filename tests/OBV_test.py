
import unittest
import sys
import json

sys.path.append('../')
from tests.util import assertFloatEqual
from bfxhfindicators import OBV

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
  -327.53682997,
  -285.14974904999997,
  -238.83489886999996,
  -237.82161314999996,
  -237.83161314999995,
  -236.24316488999995,
  -235.74875343999994,
  -234.72895487999995,
  -233.18225262999994,
  -234.78467975999993,
  -229.95919564999994,
  -230.75628720999995,
  -237.81334977999995,
  -240.18730694999996,
  -226.57705932999997,
  -228.60781678999996,
  -226.49483342999997,
  -234.94857143999997,
  -234.30646467999998
]

class OBVTest(unittest.TestCase):
  def test_add(self):
    indicator = OBV([])
    for i in range(len(expected)):
      indicator.add(candles[i])
      assertFloatEqual(self, indicator.v(), expected[i], 'candles[%d]' % i)

if __name__ == '__main__':
    unittest.main()
  
