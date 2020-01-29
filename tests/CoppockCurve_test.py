
import unittest
import sys
import json

sys.path.append('../')
from tests.util import assertFloatEqual
from bfxhfindicators import CoppockCurve

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
  0.21456535784189373,
  0.11713399819171508,
  0.039290680130712026,
  -0.025425788987278125,
  -0.04418566348541261,
  -0.05564320201249877,
  -0.032516609579306154,
  -0.05184443682639938,
  -0.0975155635547694,
  -0.12546098833412425,
  -0.15545316736099435,
  -0.1821161889376515,
  -0.1713009837645869,
  -0.09696307621982704,
  0.016417737453165066,
  0.12241487736642244,
  0.22521855843139696,
  0.3070947273681803,
  0.38581011356849343,
  0.4641257036726619,
  0.514018550441063
]

class CoppockCurveTest(unittest.TestCase):
  def test_add(self):
    indicator = CoppockCurve([10, 14, 11])
    for i in range(len(expected)):
      indicator.add(candles[i]['close'])
      assertFloatEqual(self, indicator.v(), expected[i], 'candles[%d]' % i)

if __name__ == '__main__':
    unittest.main()
  
