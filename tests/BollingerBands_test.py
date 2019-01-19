
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import BollingerBands

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
  {
    "top": None,
    "middle": 318.725,
    "bottom": None
  },
  {
    "top": None,
    "middle": 637.37,
    "bottom": None
  },
  {
    "top": None,
    "middle": 957.85,
    "bottom": None
  },
  {
    "top": None,
    "middle": 1278.85,
    "bottom": None
  },
  {
    "top": None,
    "middle": 1600.2549999999999,
    "bottom": None
  },
  {
    "top": None,
    "middle": 1921.655,
    "bottom": None
  },
  {
    "top": None,
    "middle": 2243.06,
    "bottom": None
  },
  {
    "top": None,
    "middle": 2564.5199999999995,
    "bottom": None
  },
  {
    "top": None,
    "middle": 2886.1949999999997,
    "bottom": None
  },
  {
    "top": None,
    "middle": 3207.9299999999994,
    "bottom": None
  },
  {
    "top": None,
    "middle": 3529.66,
    "bottom": None
  },
  {
    "top": None,
    "middle": 3851.5699999999997,
    "bottom": None
  },
  {
    "top": None,
    "middle": 4173.469999999999,
    "bottom": None
  },
  {
    "top": None,
    "middle": 4495.339999999999,
    "bottom": None
  },
  {
    "top": None,
    "middle": 4817.109999999999,
    "bottom": None
  },
  {
    "top": None,
    "middle": 5138.979999999999,
    "bottom": None
  },
  {
    "top": None,
    "middle": 5460.714999999998,
    "bottom": None
  },
  {
    "top": None,
    "middle": 5782.559999999999,
    "bottom": None
  },
  {
    "top": None,
    "middle": 6104.269999999999,
    "bottom": None
  },
  {
    "top": 6464.7473475829365,
    "middle": 6426.189999999998,
    "bottom": 6387.632652417059
  },
  {
    "top": 6459.628045534602,
    "middle": 6429.399999999998,
    "bottom": 6399.171954465393
  },
  {
    "top": 6447.116770177485,
    "middle": 6432.604999999998,
    "bottom": 6418.093229822511
  },
  {
    "top": 6443.750761969961,
    "middle": 6433.979999999998,
    "bottom": 6424.209238030035
  },
  {
    "top": 6441.978452553331,
    "middle": 6434.749999999998,
    "bottom": 6427.521547446665
  },
  {
    "top": 6441.615458540832,
    "middle": 6434.9349999999995,
    "bottom": 6428.254541459167
  },
  {
    "top": 6441.159942113705,
    "middle": 6435.124999999999,
    "bottom": 6429.090057886293
  },
  {
    "top": 6440.727376932891,
    "middle": 6435.26,
    "bottom": 6429.792623067109
  },
  {
    "top": 6440.221300957076,
    "middle": 6435.55,
    "bottom": 6430.878699042924
  },
  {
    "top": 6440.204990806702,
    "middle": 6435.625,
    "bottom": 6431.045009193298
  },
  {
    "top": 6440.865428341173,
    "middle": 6435.895,
    "bottom": 6430.9245716588275
  },
  {
    "top": 6440.92279589915,
    "middle": 6435.8150000000005,
    "bottom": 6430.707204100851
  },
  {
    "top": 6441.260154875052,
    "middle": 6435.33,
    "bottom": 6429.399845124948
  },
  {
    "top": 6441.457566037313,
    "middle": 6434.83,
    "bottom": 6428.202433962687
  },
  {
    "top": 6441.417612697284,
    "middle": 6434.405000000001,
    "bottom": 6427.392387302717
  },
  {
    "top": 6441.586723400376,
    "middle": 6434.035,
    "bottom": 6426.483276599623
  },
  {
    "top": 6441.198629759864,
    "middle": 6433.74,
    "bottom": 6426.281370240135
  },
  {
    "top": 6442.685187879711,
    "middle": 6434.155000000001,
    "bottom": 6425.624812120291
  },
  {
    "top": 6445.899607630215,
    "middle": 6434.8150000000005,
    "bottom": 6423.730392369786
  },
  {
    "top": 6448.853109681554,
    "middle": 6435.65,
    "bottom": 6422.446890318445
  },
  {
    "top": 6451.452546199485,
    "middle": 6436.34,
    "bottom": 6421.227453800515
  }
]

class BollingerBandsTest(unittest.TestCase):
  def test_add(self):
    indicator = BollingerBands([20, 2])
    for i in range(len(expected)):
      indicator.add(candles[i]['close'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
