
import unittest
import sys
import json

sys.path.append('../')
from tests.util import assertFloatEqual
from bfxhfindicators import StochasticRSI

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
  {
    "v": 28.602126920693006,
    "signal": 9.53404230689767
  },
  {
    "v": 32.75715502402267,
    "signal": 20.453093981571893
  },
  {
    "v": 32.75715502402267,
    "signal": 31.37214565624612
  },
  {
    "v": 8.481836916580741,
    "signal": 24.66538232154203
  },
  {
    "v": 4.326808813251076,
    "signal": 15.18860025128483
  },
  {
    "v": 11.645668378659451,
    "signal": 8.151438036163755
  },
  {
    "v": 15.108139626418145,
    "signal": 10.360205606109558
  },
  {
    "v": 15.509967354795043,
    "signal": 14.087925119957546
  },
  {
    "v": 8.825890554594837,
    "signal": 13.147999178602674
  },
  {
    "v": 1.036610493585064,
    "signal": 8.457489467658315
  },
  {
    "v": 0.6347827652081669,
    "signal": 3.499094604462689
  },
  {
    "v": 0,
    "signal": 0.5571310862644103
  },
  {
    "v": 0,
    "signal": 0.21159425506938898
  },
  {
    "v": 11.802686826265012,
    "signal": 3.934228942088337
  },
  {
    "v": 23.605373652530023,
    "signal": 11.802686826265012
  },
  {
    "v": 50.9666078287284,
    "signal": 28.791556102507812
  },
  {
    "v": 44.27431960140381,
    "signal": 39.61543369422074
  },
  {
    "v": 32.471632775138794,
    "signal": 42.570853401757006
  },
  {
    "v": 5.110398598940417,
    "signal": 27.28545032516101
  },
  {
    "v": 2.7901271854727607,
    "signal": 13.457386186517324
  },
  {
    "v": 3.6815163561074775,
    "signal": 3.8606807135068855
  },
  {
    "v": 16.389731655890824,
    "signal": 7.6204583991570205
  },
  {
    "v": 46.9329378037514,
    "signal": 22.334728605249904
  },
  {
    "v": 79.37488196645002,
    "signal": 47.56585047536408
  },
  {
    "v": 100,
    "signal": 75.43593992340048
  },
  {
    "v": 100,
    "signal": 93.12496065548333
  },
  {
    "v": 99.42895841793016,
    "signal": 99.80965280597673
  },
  {
    "v": 98.85791683586031,
    "signal": 99.42895841793016
  },
  {
    "v": 98.68689501372528,
    "signal": 98.99125675583859
  },
  {
    "v": 99.1988242428384,
    "signal": 98.91454536414132
  },
  {
    "v": 99.76986582490822,
    "signal": 99.21852836049062
  },
  {
    "v": 97.22625863285202,
    "signal": 98.73164956686621
  },
  {
    "v": 94.07638888132225,
    "signal": 97.02417111302749
  },
  {
    "v": 92.18096068022025,
    "signal": 94.49453606479818
  },
  {
    "v": 68.90523220065681,
    "signal": 85.0541939207331
  },
  {
    "v": 38.780880971810014,
    "signal": 66.62235795089569
  },
  {
    "v": 7.342975839578673,
    "signal": 38.34302967068184
  }
]

class StochasticRSITest(unittest.TestCase):
  def test_add(self):
    indicator = StochasticRSI([14, 14, 3, 3])
    for i in range(len(expected)):
      indicator.add(candles[i]['close'])
      assertFloatEqual(self, indicator.v(), expected[i], 'candles[%d]' % i)

if __name__ == '__main__':
    unittest.main()
  
