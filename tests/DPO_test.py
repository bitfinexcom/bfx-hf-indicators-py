
import unittest
import sys
import json

sys.path.append('../')
from tests.util import assertFloatEqual
from bfxhfindicators import DPO

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
  6134.652380952381,
  5830.980952380953,
  5525.161904761904,
  5217.447619047619,
  4913.3476190476185,
  4604.552380952381,
  4300.652380952381,
  3991.8,
  3689.642857142857,
  3383.5285714285715,
  3075.419047619048,
  2768.9380952380957,
  2460.6666666666665,
  2150.52380952381,
  1844.0761904761912,
  1536.5333333333347,
  1234.3190476190484,
  927.8000000000011,
  626.5095238095255,
  312.81904761904934,
  1.7142857142871435,
  -1.7619047619018602,
  -3.9190476190460686,
  -6.047619047617445,
  -3.1095238095222157,
  8.214285714287143,
  15.180952380953386,
  15.652380952379644,
  16.67619047619064,
  16.161904761904225
]

class DPOTest(unittest.TestCase):
  def test_add(self):
    indicator = DPO([21])
    for i in range(len(expected)):
      indicator.add(candles[i]['close'])
      assertFloatEqual(self, indicator.v(), expected[i], 'candles[%d]' % i)

if __name__ == '__main__':
    unittest.main()
  
