import unittest

from demographic_data_analyzer import calculate_demographic_data


class DemographicAnalyzerTests(unittest.TestCase):

    def test_return_keys(self):
        result = calculate_demographic_data(False)

        expected = [
            "race_count",
            "average_age_men",
            "percentage_bachelors",
            "higher_education_rich",
            "lower_education_rich",
            "min_work_hours",
            "rich_percentage",
            "highest_earning_country",
            "highest_earning_country_percentage",
            "top_IN_occupation",
        ]

        self.assertEqual(
            sorted(result.keys()),
            sorted(expected),
        )


if __name__ == "__main__":
    unittest.main()
