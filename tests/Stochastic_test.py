
import unittest
import sys
import json

sys.path.append('../')
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
  }
]

class StochasticTest(unittest.TestCase):
  def test_add(self):
    indicator = Stochastic([14, 1, 3])
    for i in range(len(expected)):
      indicator.add(candles[i])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
