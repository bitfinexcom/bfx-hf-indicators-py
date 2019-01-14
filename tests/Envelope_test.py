
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
    "upper": 2.12206143435,
    "basis": 1.9291467585,
    "lower": 1.73623208265
  },
  {
    "upper": 20.1365870827,
    "basis": 18.305988257,
    "lower": 16.475389431299998
  },
  {
    "upper": 22.4678765333,
    "basis": 20.425342303,
    "lower": 18.3828080727
  },
  {
    "upper": 25.0151932932,
    "basis": 22.741084812,
    "lower": 20.4669763308
  },
  {
    "upper": 25.070924007800002,
    "basis": 22.791749098,
    "lower": 20.5125741882
  },
  {
    "upper": 25.0714740078,
    "basis": 22.792249098,
    "lower": 20.5130241882
  },
  {
    "upper": 25.1588386621,
    "basis": 22.871671511,
    "lower": 20.5845043599
  },
  {
    "upper": 25.186031291849996,
    "basis": 22.896392083499997,
    "lower": 20.606752875149997
  },
  {
    "upper": 25.24212021265,
    "basis": 22.9473820115,
    "lower": 20.65264381035
  },
  {
    "upper": 25.327188836399998,
    "basis": 23.024717124,
    "lower": 20.7222454116
  },
  {
    "upper": 25.41532232855,
    "basis": 23.1048384805,
    "lower": 20.79435463245
  },
  {
    "upper": 25.6807239546,
    "basis": 23.346112686,
    "lower": 21.0115014174
  },
  {
    "upper": 25.7245639904,
    "basis": 23.385967264,
    "lower": 21.047370537600003
  },
  {
    "upper": 26.11270243175,
    "basis": 23.738820392500003,
    "lower": 21.364938353250004
  },
  {
    "upper": 26.243270076100004,
    "basis": 23.857518251000002,
    "lower": 21.4717664259
  },
  {
    "upper": 26.9918336952,
    "basis": 24.538030632,
    "lower": 22.084227568800003
  },
  {
    "upper": 27.103525355500004,
    "basis": 24.639568505000003,
    "lower": 22.175611654500003
  },
  {
    "upper": 27.219739440300003,
    "basis": 24.745217673000003,
    "lower": 22.270695905700002
  },
  {
    "upper": 27.684695030850005,
    "basis": 25.167904573500003,
    "lower": 22.65111411615
  },
  {
    "upper": 27.72001090265,
    "basis": 25.2000099115,
    "lower": 22.68000892035
  }
]

class EnvelopeTest(unittest.TestCase):
  def test_add(self):
    indicator = Envelope([20, 10])
    for i in range(len(expected)):
      indicator.add(candles[i]['vol'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
