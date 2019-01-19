
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import Acceleration

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
  -0.8791010202005427,
  -1.0432900076303624,
  -0.4570648686801929,
  -0.30209648116482285,
  -0.16950446224787277,
  -0.23322686349713379,
  -0.16328308230286104,
  -0.14928338155296697,
  0.0015530110374314,
  -0.031096662638418565
]

class AccelerationTest(unittest.TestCase):
  def test_add(self):
    indicator = Acceleration([10])
    for i in range(len(expected)):
      indicator.add(candles[i]['close'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
