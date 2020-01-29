
import unittest
import sys
import json

sys.path.append('../')
from tests.util import assertFloatEqual
from bfxhfindicators import VO

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
  0,
  48.0475085725853,
  26.50574349499176,
  12.003448110752274,
  -8.46495800662531,
  -25.41200282735928,
  -38.379591385220216,
  -49.442519585652974,
  -57.87374167602187,
  -63.88686470658549,
  -68.27092453356289,
  -65.92447466406658,
  -70.61202464128804,
  -59.88830193188514,
  -61.285650088778134,
  -35.20420021899919,
  -42.18893632643142,
  -46.54965307188941,
  -30.517593190987363,
  -41.23939619103368,
  -20.2538681827325,
  -24.222798426985282,
  -27.469779419132657,
  -29.750371046201778,
  -24.291503857968472,
  -26.901308377655457,
  -28.266873644897757,
  20.071980496324105,
  14.664480072178163,
  18.6795655166791
]

class VOTest(unittest.TestCase):
  def test_add(self):
    indicator = VO([5, 10])
    for i in range(len(expected)):
      indicator.add(candles[i])
      assertFloatEqual(self, indicator.v(), expected[i], 'candles[%d]' % i)

if __name__ == '__main__':
    unittest.main()
  
