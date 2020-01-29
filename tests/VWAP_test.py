
import unittest
import sys
import json

sys.path.append('../')
from tests.util import assertFloatEqual
from bfxhfindicators import VWAP

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
  6373.2,
  6381.609396309267,
  6384.752379792012,
  6388.616615731393,
  6388.704310127057,
  6388.705172167694,
  6388.843244885121,
  6388.888019073672,
  6388.988111421011,
  6389.14154513006,
  6389.300916672515,
  6389.795248576168,
  6389.876263412353,
  6390.574728697805,
  6390.801063874797,
  6392.061959913012,
  6392.241239651144,
  6392.427355145854,
  6393.146267846356,
  6393.2038371098515
]

class VWAPTest(unittest.TestCase):
  def test_add(self):
    indicator = VWAP([])
    for i in range(len(expected)):
      indicator.add(candles[i])
      assertFloatEqual(self, indicator.v(), expected[i], 'candles[%d]' % i)

if __name__ == '__main__':
    unittest.main()
  
