
import unittest
import sys
import json

sys.path.append('../')
from tests.util import assertFloatEqual
from bfxhfindicators import NetVolume

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
  38.58293517,
  -327.53682997,
  -42.38708092,
  -46.31485018,
  1.01328572,
  0.01,
  -1.58844826,
  -0.49441145,
  -1.01979856,
  1.54670225,
  -1.60242713,
  4.82548411,
  -0.79709156,
  7.05706257,
  -2.37395717,
  13.61024762,
  -2.03075746,
  2.11298336,
  -8.45373801,
  0.64210676
]

class NetVolumeTest(unittest.TestCase):
  def test_add(self):
    indicator = NetVolume([])
    for i in range(len(expected)):
      indicator.add(candles[i])
      assertFloatEqual(self, indicator.v(), expected[i], 'candles[%d]' % i)

if __name__ == '__main__':
    unittest.main()
  
