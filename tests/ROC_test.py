
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import ROC

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
  -95.84679827250167,
  -98.52673541768053,
  -98.11949409419252,
  -84.76285134773592,
  134.28309736764078,
  136002.4762,
  27.845364003231666,
  327.37346798906054,
  728.9615558978629,
  -58.48543182761905
]

class ROCTest(unittest.TestCase):
  def test_add(self):
    indicator = ROC([10])
    for i in range(len(expected)):
      indicator.add(candles[i]['vol'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
