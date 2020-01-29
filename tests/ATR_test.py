
import unittest
import sys
import json

sys.path.append('../')
from tests.util import assertFloatEqual
from bfxhfindicators import ATR

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
  9.574312137142897,
  9.304737338775567,
  8.782970386005884,
  8.39847250129115,
  7.984295894056094,
  7.685417615909179,
  7.515030643344185,
  7.071099883105263,
  6.730307034312043,
  6.434985240432659,
  6.353914866116054,
  6.242920947107778,
  5.889855165171521,
  5.704865510516425,
  5.868803688336681,
  5.93531771059836,
  5.997080731269919,
  6.397289250464951,
  6.276054304003155,
  5.863478996574359,
  5.516087639676191
]

class ATRTest(unittest.TestCase):
  def test_add(self):
    indicator = ATR([14])
    for i in range(len(expected)):
      indicator.add(candles[i])
      assertFloatEqual(self, indicator.v(), expected[i], 'candles[%d]' % i)

if __name__ == '__main__':
    unittest.main()
  
