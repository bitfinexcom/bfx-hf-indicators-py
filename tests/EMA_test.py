
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import EMA

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
  6374.5,
  6374.347619047619,
  6377.704988662132,
  6381.733084980024,
  6386.148981648593,
  6390.134792920156,
  6393.75052692776,
  6397.126667220355,
  6400.590794151749,
  6403.83928994682,
  6406.768881380456,
  6409.762321248983,
  6412.4516239871755,
  6414.82765979792,
  6416.786930293356,
  6418.750079789226,
  6420.2691198093,
  6421.853013160795,
  6423.028916669291,
  6424.492829367454,
  6425.84589323722,
  6426.908189119389,
  6427.878837774686,
  6428.595138939001,
  6428.900363801954,
  6429.1765196303395,
  6429.331136808402,
  6429.871028540936,
  6430.359502013228,
  6431.287168488159,
  6431.450295298811,
  6431.169314794163,
  6430.867475289957,
  6430.680096690913,
  6430.424849387016,
  6430.527244683491,
  6431.715126142206,
  6433.466066509615,
  6435.126441127747,
  6436.752494353676
]

class EMATest(unittest.TestCase):
  def test_add(self):
    indicator = EMA([20])
    for i in range(len(expected)):
      indicator.add(candles[i]['close'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
