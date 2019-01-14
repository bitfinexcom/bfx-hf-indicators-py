
import unittest
import sys
import json

sys.path.append('../')
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
  2655.4901641035294
]

class AOTest(unittest.TestCase):
  def test_add(self):
    indicator = AO([])
    for i in range(len(expected)):
      indicator.add(candles[i])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
