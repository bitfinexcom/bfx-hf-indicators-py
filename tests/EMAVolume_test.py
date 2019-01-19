
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import EMAVolume

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
  38.58293517,
  66.10235372238094,
  63.843756312630376,
  62.17433668095129,
  56.34947468467022,
  50.98381042898735,
  46.279490222417124,
  41.91900652980597,
  38.02384386601493,
  34.54983037877541,
  31.41198245032061,
  28.879934989337695,
  26.205378472257916,
  24.381729338709544,
  22.285751036927685,
  21.459512616267904,
  19.60915498233763,
  17.942852923067377,
  17.039127693251437,
  15.477506651989396,
  14.912644972752311,
  13.809858244871139,
  12.771746026311984,
  11.807422139044176,
  11.07713360199235,
  10.25012133989784,
  9.49077045038376,
  10.344407390347213,
  10.07337685602843,
  10.273348438311436,
  10.468956679424632,
  9.674314457574669,
  9.358871260662797,
  9.310277052980627,
  9.257237080315805,
  16.852034572666682,
  17.40551488003176,
  17.06121032860016,
  16.263019231590622,
  15.262694892391515
]

class EMAVolumeTest(unittest.TestCase):
  def test_add(self):
    indicator = EMAVolume([20])
    for i in range(len(expected)):
      indicator.add(candles[i])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
