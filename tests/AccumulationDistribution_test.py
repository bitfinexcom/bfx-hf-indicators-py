
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import AccumulationDistribution

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
  22.45872345716793,
  -199.7166087602493,
  -220.4592228274817,
  -266.7740730074817,
  -265.7607872874817,
  -265.7607872874817,
  -267.1048588920963,
  -267.59927034209625,
  -268.6190689020963,
  -267.3069627561312,
  -268.1972000505752,
  -263.3717159405752,
  -262.90283855233986,
  -260.9564739723507,
  -263.3304311423507,
  -249.72018352235068,
  -251.75094098235067,
  -249.63795762235068,
  -254.58259683574818,
  -253.9404900757482
]

class AccumulationDistributionTest(unittest.TestCase):
  def test_add(self):
    indicator = AccumulationDistribution([])
    for i in range(len(expected)):
      indicator.add(candles[i])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
