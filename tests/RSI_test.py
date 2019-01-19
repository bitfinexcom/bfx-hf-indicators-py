
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import RSI

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
  0,
  96.3591808156828,
  97.23146545986896,
  97.72194686962064,
  97.47594808518632,
  97.48325825406619,
  97.57249225051866,
  97.90718493569277,
  97.99614843184341,
  97.59722905016062,
  97.9447569844365,
  97.04499859232207,
  94.05416729088839,
  84.08694825559968,
  85.8207417844136,
  73.36880215033696,
  76.56553671847121,
  65.4415941826253,
  72.58946050556017,
  73.04889039188016,
  65.83403386009387,
  66.06154628161843,
  58.42950917879185,
  45.566585090362814,
  45.566585090362814,
  42.13610305964943,
  57.60398635925704,
  57.60398635925704,
  70.39705696643671,
  47.414546945620074,
  38.27609469421104,
  37.35311268228497,
  40.340985476109
]

class RSITest(unittest.TestCase):
  def test_add(self):
    indicator = RSI([14])
    for i in range(len(expected)):
      indicator.add(candles[i]['close'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
