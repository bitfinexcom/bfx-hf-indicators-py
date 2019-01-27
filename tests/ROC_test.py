
import unittest
import sys
import json

sys.path.append('../')
from tests.util import assertFloatEqual
from bfxhfindicators import ROC

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
  0.9428190446309572,
  1.024651257669196,
  0.44308537194208114,
  0.2710280373831719,
  0.11356388357367296,
  0.14623522090851954,
  0.10267419610770606,
  0.11976606731785944,
  0.01088054713608173,
  0.05750073818514955,
  0.06371802443041454,
  -0.018638749961166448,
  -0.013979496738111778,
  -0.03106844378165098,
  -0.055940578674199805,
  -0.08699164258861426,
  -0.06060888619515496,
  -0.029517314235107523,
  0.01243355817351313,
  0.026404075546730986
]

class ROCTest(unittest.TestCase):
  def test_add(self):
    indicator = ROC([10])
    for i in range(len(expected)):
      indicator.add(candles[i]['close'])
      assertFloatEqual(self, indicator.v(), expected[i], 'candles[%d]' % i)

if __name__ == '__main__':
    unittest.main()
  
