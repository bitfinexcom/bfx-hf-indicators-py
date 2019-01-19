
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import ChaikinOsc

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
  -70.69215116008729,
  -99.78503100514357,
  -117.35184045310811,
  -113.54750427517467,
  -101.66868454100421,
  -87.99421883840236,
  -74.55795752702869,
  -62.607790393555035,
  -51.60998002945826,
  -42.702316744245536,
  -33.64086257036351,
  -26.726455551122,
  -20.848858899515562,
  -17.304386741629713,
  -9.950716003255565,
  -6.68393571089743,
  -4.067582184851176,
  -4.200769838926789,
  -3.6690608338734876,
  -1.7373063068271222,
  -1.3594187859206954,
  -1.2355461199357478,
  -0.6515390986297973,
  0.9636831235980594,
  2.29841801918235,
  1.911018883813881,
  -4.292905581001747,
  -8.826524511971655,
  -6.1516837040923065
]

class ChaikinOscTest(unittest.TestCase):
  def test_add(self):
    indicator = ChaikinOsc([3, 10])
    for i in range(len(expected)):
      indicator.add(candles[i])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
