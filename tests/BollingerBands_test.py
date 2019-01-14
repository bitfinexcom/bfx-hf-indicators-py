
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import BollingerBands

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
  {
    "top": None,
    "middle": 1.9291467585,
    "bottom": None
  },
  {
    "top": None,
    "middle": 18.305988257,
    "bottom": None
  },
  {
    "top": None,
    "middle": 20.425342303,
    "bottom": None
  },
  {
    "top": None,
    "middle": 22.741084812,
    "bottom": None
  },
  {
    "top": None,
    "middle": 22.791749098,
    "bottom": None
  },
  {
    "top": None,
    "middle": 22.792249098,
    "bottom": None
  },
  {
    "top": None,
    "middle": 22.871671511,
    "bottom": None
  },
  {
    "top": None,
    "middle": 22.896392083499997,
    "bottom": None
  },
  {
    "top": None,
    "middle": 22.9473820115,
    "bottom": None
  },
  {
    "top": None,
    "middle": 23.024717124,
    "bottom": None
  },
  {
    "top": None,
    "middle": 23.1048384805,
    "bottom": None
  },
  {
    "top": None,
    "middle": 23.346112686,
    "bottom": None
  },
  {
    "top": None,
    "middle": 23.385967264,
    "bottom": None
  },
  {
    "top": None,
    "middle": 23.738820392500003,
    "bottom": None
  },
  {
    "top": None,
    "middle": 23.857518251000002,
    "bottom": None
  },
  {
    "top": None,
    "middle": 24.538030632,
    "bottom": None
  },
  {
    "top": None,
    "middle": 24.639568505000003,
    "bottom": None
  },
  {
    "top": None,
    "middle": 24.745217673000003,
    "bottom": None
  },
  {
    "top": None,
    "middle": 25.167904573500003,
    "bottom": None
  },
  {
    "top": 170.5596700836552,
    "middle": 25.2000099115,
    "bottom": -120.1596502606552
  }
]

class BollingerBandsTest(unittest.TestCase):
  def test_add(self):
    indicator = BollingerBands([20, 2])
    for i in range(len(expected)):
      indicator.add(candles[i]['vol'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
