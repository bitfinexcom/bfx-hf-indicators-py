
import unittest
import sys
import json

sys.path.append('../')
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
  8.101138019286388,
  12.674335747378446,
  14.84159938049618,
  14.13451462312009,
  11.343080911496997,
  7.174926186735459,
  2.055655949360892,
  -3.610187970331106,
  -9.510120226656642,
  -15.440573190534202,
  -20.970099480746743,
  -26.451844515524982,
  -31.08506736704478,
  -35.50958921151133,
  -38.2239437262261,
  -41.13411032479489,
  -44.08309034249847,
  -45.93774644942222,
  -48.240515983117
]

class PPOTest(unittest.TestCase):
  def test_add(self):
    indicator = PPO([10, 21])
    for i in range(len(expected)):
      indicator.add(candles[i]['vol'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
