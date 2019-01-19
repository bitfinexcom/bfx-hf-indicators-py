
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
  100,
  100,
  93.13109003438899,
  87.52982776181736,
  81.94836218339076,
  83.1268060373516,
  78.35161611790534,
  79.25488639482829,
  75.6454732385416,
  76.97221776521556,
  78.39225777547142,
  73.09464599551877,
  75.08386461366096,
  68.73791176500312,
  60.09089538593927,
  60.09089538593927,
  47.82958652466752,
  58.06609219255229,
  58.06609219255229,
  68.19421535150916
]

class RVITest(unittest.TestCase):
  def test_add(self):
    indicator = RVI([10])
    for i in range(len(expected)):
      indicator.add(candles[i]['close'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
