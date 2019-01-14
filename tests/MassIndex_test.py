
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import MassIndex

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
  10.06645210616107,
  9.664293209724569,
  8.584115000905877,
  7.754378889801893,
  7.264276751232576,
  6.99627912434242,
  6.9303955314836,
  6.959763449065621,
  7.04598917333618,
  7.30463471914714,
  7.5038004937498535
]

class MassIndexTest(unittest.TestCase):
  def test_add(self):
    indicator = MassIndex([10])
    for i in range(len(expected)):
      indicator.add(candles[i])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
