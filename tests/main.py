import json
import unittest

from unittest.mock import patch

from api import processData

json = [
    {
        "country": "US",
        "city": "Boston",
        "currency": "USD",
        "amount": 100
    },
    {
        "country": "FR",
        "city": "Paris",
        "currency": "EUR",
        "amount": 20
    },
    {
        "country": "FR",
        "city": "Lyon",
        "currency": "EUR",
        "amount": 11.4
    },
    {
        "country": "ES",
        "city": "Madrid",
        "currency": "EUR",
        "amount": 8.9
    },
    {
        "country": "UK",
        "city": "London",
        "currency": "GBP",
        "amount": 12.2
    },
    {
        "country": "UK",
        "city": "London",
        "currency": "FBP",
        "amount": 10.9
    }
]

class TestNest(unittest.TestCase):


    def test_three_outputs(self):
        output = processData(json, ["currency", "country", "city"])
        actual_output = {
                          "EUR": {
                            "ES": {
                              "Madrid": [
                                {
                                  "amount": 8.9
                                }
                              ]
                            },
                            "FR": {
                              "Lyon": [
                                {
                                  "amount": 11.4
                                }
                              ],
                              "Paris": [
                                {
                                  "amount": 20
                                }
                              ]
                            }
                          },
                          "FBP": {
                            "UK": {
                              "London": [
                                {
                                  "amount": 10.9
                                }
                              ]
                            }
                          },
                          "GBP": {
                            "UK": {
                              "London": [
                                {
                                  "amount": 12.2
                                }
                              ]
                            }
                          },
                          "USD": {
                            "US": {
                              "Boston": [
                                {
                                  "amount": 100
                                }
                              ]
                            }
                          }
                        }


        self.assertEqual(output, actual_output)
