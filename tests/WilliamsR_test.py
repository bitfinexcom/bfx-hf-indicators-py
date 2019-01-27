
import unittest
import sys
import json

sys.path.append('../')
from tests.util import assertFloatEqual
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
  -9.567300960694123,
  -7.7693628572468825,
  -39.06502270806301,
  -37.50258739287931,
  -53.2483619888387,
  -90.58852866628555,
  -85.5559807874793,
  -96.66676479710905,
  -48.86363636363742,
  -60.176991150443115,
  -15.044247787608766,
  -66.16541353383505,
  -98.51851851851987,
  -100,
  -93.47826086956795
]

class WilliamsRTest(unittest.TestCase):
  def test_add(self):
    indicator = WilliamsR([14])
    for i in range(len(expected)):
      indicator.add(candles[i])
      assertFloatEqual(self, indicator.v(), expected[i], 'candles[%d]' % i)

if __name__ == '__main__':
    unittest.main()
  
