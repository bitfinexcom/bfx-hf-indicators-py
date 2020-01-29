
import unittest
import sys
import json

sys.path.append('../')
from tests.util import assertFloatEqual
from bfxhfindicators import AO

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
  1087.0820588235292,
  2176.705882352941,
  3270.696764705882,
  4366.564117647059,
  5463.113823529411,
  5285.145,
  5104.30705882353,
  4918.727855081412,
  4731.508149199059,
  4543.574437364706,
  4355.769437364706,
  4168.047672658823,
  3979.950106255059,
  3791.1283641487066,
  3602.1716611877646,
  3412.9563670701186,
  3223.542249423059,
  3033.928720011294,
  2844.4719288094116,
  2655.4901641035294,
  2466.6313405741175,
  2277.6268648555297,
  2088.7115707378825,
  1899.1603942672937,
  1708.6215707378824,
  1518.0601001496489,
  1327.9061081929412,
  1138.4855199576468,
  949.9608140752953,
  761.8511081929419,
  572.6314023105888,
  382.6508140752949,
  191.89728466352972,
  0.8437552517652875,
  -2.2621271011757926,
  -2.5547741600003064,
  0.013167016472834803,
  3.626696428235846,
  7.470433087706624,
  11.088668381824391,
  13.570138970059816,
  14.05190911594218,
  13.888085586529996,
  13.743592087354045,
  13.648886205000963,
  13.449252883059671,
  13.481899941883967,
  13.147547269324605,
  12.705894989204353,
  11.571483224501208,
  10.43717908673716,
  9.03541438085449,
  7.85339226502947,
  7.462388244558497
]

class AOTest(unittest.TestCase):
  def test_add(self):
    indicator = AO([])
    for i in range(len(expected)):
      indicator.add(candles[i])
      assertFloatEqual(self, indicator.v(), expected[i], 'candles[%d]' % i)

if __name__ == '__main__':
    unittest.main()
  
