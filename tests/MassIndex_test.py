
import unittest
import sys
import json

sys.path.append('../')
from tests.util import assertFloatEqual
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
  7.5038004937498535,
  7.686316320543908,
  7.858479834148806,
  8.061833047617014,
  8.258171602592954,
  8.369879526305187,
  8.39590145670369,
  8.553193846902495,
  8.743585054464694,
  9.009386648062453,
  9.434420049851653,
  9.83087305876229,
  9.98982800380342,
  9.9718400757883,
  9.770821314411071,
  9.8612352281208,
  10.468524180802467,
  10.956794215594165,
  11.10283621345571,
  10.937392793251085
]

class MassIndexTest(unittest.TestCase):
  def test_add(self):
    indicator = MassIndex([10])
    for i in range(len(expected)):
      indicator.add(candles[i])
      assertFloatEqual(self, indicator.v(), expected[i], 'candles[%d]' % i)

if __name__ == '__main__':
    unittest.main()
  
