import json
import unittest

from api import processData, processInput, processInputFile, validateData

class TestNest(unittest.TestCase):

    def setUp(self):
        with open('input.json', 'r') as json_data:
            self.file = json.loads(json_data.read())

    def test_readFile(self):
        data = processInputFile(from_file=True, file='input.json')
        self.assertEqual(data, self.file)

    def test_oneKey(self):
        output = processData(self.file, ["city"])
        actual_output = {
            "Boston": [
                {
                    "country": "US",
                    "currency": "USD",
                    "amount": 100
                }
            ],
            "Paris": [
                {
                    "country": "FR",
                    "currency": "EUR",
                    "amount": 20
                }
            ],
            "Lyon": [
                {
                    "country": "FR",
                    "currency": "EUR",
                    "amount": 11.4
                }
            ],
            "Madrid": [
                {
                    "country": "ES",
                    "currency": "EUR",
                    "amount": 8.9
                }
            ],
            "London": [
                {
                    "country": "UK",
                    "currency": "GBP",
                    "amount": 12.2
                },
                {
                    "country": "UK",
                    "currency": "FBP",
                    "amount": 10.9
                }
            ]
        }
        self.assertEqual(output, actual_output)

    def test_twoKeys(self):
        output = processData(self.file, ["currency", "country"])
        actual_output = {
            "USD": {
                "US": [
                    {
                        "city": "Boston",
                        "amount": 100
                    }
                ]
            },
            "EUR": {
                "FR": [
                    {
                        "city": "Paris",
                        "amount": 20
                    },
                    {
                        "city": "Lyon",
                        "amount": 11.4
                    }
                ],
                "ES": [
                    {
                        "city": "Madrid",
                        "amount": 8.9
                    }
                ]
            },
            "GBP": {
                "UK": [
                    {
                        "city": "London",
                        "amount": 12.2
                    }
                ]
            },
            "FBP": {
                "UK": [
                    {
                        "city": "London",
                        "amount": 10.9
                    }
                ]
            }
        }
        self.assertEqual(output, actual_output)

    def test_threeKeys(self):
        output = processData(self.file, ["currency", "country", "city"])
        actual_output ={
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

    def test_fourKeys(self):
        output = processData(self.file, ["currency", "country", "city", "amount"])
        actual_output = {
            "USD": {
                "US": {
                    "Boston": {
                        100: [
                            {}
                        ]
                    }
                }
            },
            "EUR": {
                "FR": {
                    "Paris": {
                        20: [
                            {}
                        ]
                    },
                    "Lyon": {
                        11.4: [
                            {}
                        ]
                    }
                },
                "ES": {
                    "Madrid": {
                        8.9: [
                            {}
                        ]
                    }
                }
            },
            "GBP": {
                "UK": {
                    "London": {
                        12.2: [
                            {}
                        ]
                    }
                }
            },
            "FBP": {
                "UK": {
                    "London": {
                        10.9: [
                            {}
                        ]
                    }
                }
            }
        }
        self.assertEqual(output, actual_output)