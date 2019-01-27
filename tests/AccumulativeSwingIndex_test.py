
import unittest
import sys
import json

sys.path.append('../')
from tests.util import assertFloatEqual
from bfxhfindicators import AccumulativeSwingIndex

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
  -77.55673133450911,
  -4.460822087345136,
  8.728341410753723,
  26.146925481550184,
  25.813592148216852,
  23.484673748216853,
  19.892991090906612,
  29.236793821847023,
  32.02513408367348,
  27.819526607037965,
  47.2761740058819,
  48.670404775112665,
  52.17861740506774,
  33.289728516178855,
  40.46921569566604,
  19.25492998138032,
  28.385648935628687,
  11.496760046739798,
  20.910553150188072
]

class AccumulativeSwingIndexTest(unittest.TestCase):
  def test_add(self):
    indicator = AccumulativeSwingIndex([10])
    for i in range(len(expected)):
      indicator.add(candles[i])
      assertFloatEqual(self, indicator.v(), expected[i], 'candles[%d]' % i)

if __name__ == '__main__':
    unittest.main()
  
