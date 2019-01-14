
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import ATR

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
  None,
  None,
  9.574312137142897,
  9.304737338775567,
  8.782970386005884,
  8.39847250129115,
  7.984295894056094,
  7.685417615909179,
  7.515030643344185
]

class ATRTest(unittest.TestCase):
  def test_add(self):
    indicator = ATR([14])
    for i in range(len(expected)):
      indicator.add(candles[i])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
