
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import RSI

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
  84.02829296710175,
  83.6167831636752,
  83.76114871577761,
  83.17500150225884,
  83.23998958875134,
  83.31456847476579,
  83.32362390517964,
  83.90651640142453,
  79.87993755462685,
  81.47401788221298,
  76.25871115053226,
  79.832645605281,
  67.71208124255648,
  67.7521964981491,
  70.96225281377895,
  62.165708544579196
]

class RSITest(unittest.TestCase):
  def test_add(self):
    indicator = RSI([14])
    for i in range(len(expected)):
      indicator.add(candles[i]['vol'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
