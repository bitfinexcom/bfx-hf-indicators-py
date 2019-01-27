
import unittest
import sys
import json

sys.path.append('../')
from tests.util import assertFloatEqual
from bfxhfindicators import PPO

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
  -0.0004563741926094606,
  0.00930983778991804,
  0.027451246865763522,
  0.051608521660731946,
  0.07757717373744064,
  0.10271262451185614,
  0.12569769678914838,
  0.14671943672008175,
  0.16506708105201315,
  0.1800621551849513,
  0.19251590560548187,
  0.20195801285261683,
  0.20815939726303503,
  0.2107771336814332,
  0.21096133483796825,
  0.20822388311907228,
  0.20385743650787957,
  0.19736553403336932,
  0.1905617059457534,
  0.18346506576822752,
  0.1755643717647672,
  0.167142207381887,
  0.15791969209741652,
  0.14727625149260484,
  0.13598662875469672,
  0.12430818209008421,
  0.11392726678829485,
  0.10461093755902724,
  0.09762380984173424,
  0.09014400381505953,
  0.08128359444192074,
  0.07176271289520277,
  0.062479655220909175,
  0.053475507902400424,
  0.04603045249136131,
  0.0430914870716204,
  0.04488571626313121,
  0.04945627535774317,
  0.055586058710218975,
  0.06200684925071821
]

class PPOTest(unittest.TestCase):
  def test_add(self):
    indicator = PPO([10, 21])
    for i in range(len(expected)):
      indicator.add(candles[i]['close'])
      assertFloatEqual(self, indicator.v(), expected[i], 'candles[%d]' % i)

if __name__ == '__main__':
    unittest.main()
  
