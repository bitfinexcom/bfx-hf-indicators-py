
import unittest
import sys
import json

sys.path.append('../')
from tests.util import assertFloatEqual
from bfxhfindicators import EOM

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
  1393.9762788520325,
  7476.69218739003,
  8850.82719798626,
  9132.795333996592,
  9132.79176256802,
  9512.767266819841,
  20227.150221139134,
  23213.56602578869,
  23238.75649329301,
  24076.290362484124,
  24668.38491548906,
  25887.101334251,
  25652.347897848787,
  25531.91457812839,
  24013.032416043057,
  18204.66874705949,
  16073.310546593935,
  15992.859352149131,
  16560.19181182319,
  16163.755454723878,
  5170.087562028681,
  1920.4018950013071,
  -2250.668153885587,
  -3474.7321721263515,
  -4163.815397263225,
  -2954.457860280487,
  -2138.7218300350373,
  -1046.676858750305,
  -1186.1130768833452,
  -3233.542807889437,
  -2634.286951377156,
  -2824.576800031396,
  -3391.9056882768878
]

class EOMTest(unittest.TestCase):
  def test_add(self):
    indicator = EOM([10000, 14])
    for i in range(len(expected)):
      indicator.add(candles[i])
      assertFloatEqual(self, indicator.v(), expected[i], 'candles[%d]' % i)

if __name__ == '__main__':
    unittest.main()
  
