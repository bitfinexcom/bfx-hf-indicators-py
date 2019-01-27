PRECISION = 0.00000001

def assertFloatEqual(self, actual, expected, message):
  if type(expected) == type(actual) == float:
    return self.assertTrue(abs(actual - expected) < PRECISION, message)
  elif type(expected) == type(actual) == dict:
    for k in expected.keys():
      assertFloatEqual(self, actual[k], expected[k], '%s[%s]' % (message, k))
  else:
    return self.assertEqual(actual, expected, message)
