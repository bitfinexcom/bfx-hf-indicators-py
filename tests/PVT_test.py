
import unittest
import sys
import json

sys.path.append('../')
from tests.util import assertFloatEqual
from bfxhfindicators import PVT

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
  -0.08221177001366682,
  0.16188524543676092,
  0.23703415361698793,
  0.238312598216988,
  0.2383124426500242,
  0.238337154041748,
  0.23842175953870662,
  0.23910382477357256,
  0.23939232134620017,
  0.23936741844272386,
  0.24206715778875895,
  0.24204239647162065,
  0.2413847019171002,
  0.24064715036833828,
  0.24487695663368308,
  0.24402520823495075,
  0.2447476293877628,
  0.24120165343241184,
  0.2416207961995002
]

class PVTTest(unittest.TestCase):
  def test_add(self):
    indicator = PVT([])
    for i in range(len(expected)):
      indicator.add(candles[i])
      assertFloatEqual(self, indicator.v(), expected[i], 'candles[%d]' % i)

if __name__ == '__main__':
    unittest.main()
  
