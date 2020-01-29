
import unittest
import sys
import json

sys.path.append('../')
from tests.util import assertFloatEqual
from bfxhfindicators import Stochastic

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
  {
    "k": 97.14250695403145,
    "d": 32.380835651343816
  },
  {
    "k": 94.4214283278681,
    "d": 63.85464509396652
  },
  {
    "k": 93.73060194446757,
    "d": 95.09817907545569
  },
  {
    "k": 75.38359109557324,
    "d": 87.8452071226363
  },
  {
    "k": 77.38952129325169,
    "d": 82.16790477776415
  },
  {
    "k": 53.911801350355724,
    "d": 68.89497124639355
  },
  {
    "k": 90.43269903930587,
    "d": 73.9113405609711
  },
  {
    "k": 92.23063714275311,
    "d": 78.85837917747158
  },
  {
    "k": 60.93497729193699,
    "d": 81.19943782466532
  },
  {
    "k": 62.497412607120694,
    "d": 71.88767568060359
  },
  {
    "k": 46.751638011161305,
    "d": 56.72800930340633
  },
  {
    "k": 9.411471333714436,
    "d": 39.55350731733214
  },
  {
    "k": 14.444019212520695,
    "d": 23.535709519132144
  },
  {
    "k": 3.333235202890946,
    "d": 9.062908583042026
  },
  {
    "k": 51.13636363636258,
    "d": 22.971206017258073
  },
  {
    "k": 39.82300884955688,
    "d": 31.43086922960347
  },
  {
    "k": 84.95575221239123,
    "d": 58.638374899436904
  },
  {
    "k": 33.83458646616495,
    "d": 52.87111584270435
  },
  {
    "k": 1.481481481480134,
    "d": 40.090606720012104
  },
  {
    "k": 0,
    "d": 11.772022649215026
  },
  {
    "k": 6.521739130432061,
    "d": 2.6677402039707316
  }
]

class StochasticTest(unittest.TestCase):
  def test_add(self):
    indicator = Stochastic([14, 1, 3])
    for i in range(len(expected)):
      indicator.add(candles[i])
      assertFloatEqual(self, indicator.v(), expected[i], 'candles[%d]' % i)

if __name__ == '__main__':
    unittest.main()
  
