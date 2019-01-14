
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import WilliamsR

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
  -2.857493045968546,
  -5.578571672131906,
  -6.269398055532433,
  -24.61640890442677,
  -22.610478706748314,
  -46.08819864964427,
  -9.567300960694123
]

class WilliamsRTest(unittest.TestCase):
  def test_add(self):
    indicator = WilliamsR([14])
    for i in range(len(expected)):
      indicator.add(candles[i])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
