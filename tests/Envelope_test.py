
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import Envelope

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
    "upper": 350.5975,
    "basis": 318.725,
    "lower": 286.8525
  },
  {
    "upper": 701.107,
    "basis": 637.37,
    "lower": 573.633
  },
  {
    "upper": 1053.635,
    "basis": 957.85,
    "lower": 862.065
  },
  {
    "upper": 1406.735,
    "basis": 1278.85,
    "lower": 1150.965
  },
  {
    "upper": 1760.2804999999998,
    "basis": 1600.2549999999999,
    "lower": 1440.2295
  },
  {
    "upper": 2113.8205,
    "basis": 1921.655,
    "lower": 1729.4895
  },
  {
    "upper": 2467.366,
    "basis": 2243.06,
    "lower": 2018.754
  },
  {
    "upper": 2820.9719999999993,
    "basis": 2564.5199999999995,
    "lower": 2308.0679999999998
  },
  {
    "upper": 3174.8144999999995,
    "basis": 2886.1949999999997,
    "lower": 2597.5755
  },
  {
    "upper": 3528.7229999999995,
    "basis": 3207.9299999999994,
    "lower": 2887.1369999999993
  },
  {
    "upper": 3882.6259999999997,
    "basis": 3529.66,
    "lower": 3176.694
  },
  {
    "upper": 4236.727,
    "basis": 3851.5699999999997,
    "lower": 3466.4129999999996
  },
  {
    "upper": 4590.816999999999,
    "basis": 4173.469999999999,
    "lower": 3756.1229999999996
  },
  {
    "upper": 4944.873999999999,
    "basis": 4495.339999999999,
    "lower": 4045.805999999999
  },
  {
    "upper": 5298.820999999999,
    "basis": 4817.109999999999,
    "lower": 4335.3989999999985
  },
  {
    "upper": 5652.877999999999,
    "basis": 5138.979999999999,
    "lower": 4625.0819999999985
  },
  {
    "upper": 6006.786499999998,
    "basis": 5460.714999999998,
    "lower": 4914.643499999998
  },
  {
    "upper": 6360.815999999999,
    "basis": 5782.559999999999,
    "lower": 5204.303999999998
  },
  {
    "upper": 6714.696999999998,
    "basis": 6104.269999999999,
    "lower": 5493.842999999999
  },
  {
    "upper": 7068.8089999999975,
    "basis": 6426.189999999998,
    "lower": 5783.570999999998
  },
  {
    "upper": 7072.339999999997,
    "basis": 6429.399999999998,
    "lower": 5786.459999999998
  },
  {
    "upper": 7075.865499999998,
    "basis": 6432.604999999998,
    "lower": 5789.344499999997
  },
  {
    "upper": 7077.377999999998,
    "basis": 6433.979999999998,
    "lower": 5790.581999999998
  },
  {
    "upper": 7078.2249999999985,
    "basis": 6434.749999999998,
    "lower": 5791.274999999998
  },
  {
    "upper": 7078.4285,
    "basis": 6434.9349999999995,
    "lower": 5791.441499999999
  },
  {
    "upper": 7078.637499999999,
    "basis": 6435.124999999999,
    "lower": 5791.612499999999
  },
  {
    "upper": 7078.786,
    "basis": 6435.26,
    "lower": 5791.734
  },
  {
    "upper": 7079.1050000000005,
    "basis": 6435.55,
    "lower": 5791.995
  },
  {
    "upper": 7079.1875,
    "basis": 6435.625,
    "lower": 5792.0625
  },
  {
    "upper": 7079.4845000000005,
    "basis": 6435.895,
    "lower": 5792.3055
  },
  {
    "upper": 7079.396500000001,
    "basis": 6435.8150000000005,
    "lower": 5792.2335
  },
  {
    "upper": 7078.863,
    "basis": 6435.33,
    "lower": 5791.797
  },
  {
    "upper": 7078.313,
    "basis": 6434.83,
    "lower": 5791.347
  },
  {
    "upper": 7077.845500000001,
    "basis": 6434.405000000001,
    "lower": 5790.9645
  },
  {
    "upper": 7077.4385,
    "basis": 6434.035,
    "lower": 5790.6314999999995
  },
  {
    "upper": 7077.114,
    "basis": 6433.74,
    "lower": 5790.366
  },
  {
    "upper": 7077.570500000001,
    "basis": 6434.155000000001,
    "lower": 5790.739500000001
  },
  {
    "upper": 7078.2965,
    "basis": 6434.8150000000005,
    "lower": 5791.333500000001
  },
  {
    "upper": 7079.215,
    "basis": 6435.65,
    "lower": 5792.084999999999
  },
  {
    "upper": 7079.974,
    "basis": 6436.34,
    "lower": 5792.706
  }
]

class EnvelopeTest(unittest.TestCase):
  def test_add(self):
    indicator = Envelope([20, 10])
    for i in range(len(expected)):
      indicator.add(candles[i]['close'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
