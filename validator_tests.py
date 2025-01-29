import validator
import unittest
import os

#test fixture mock configuration data to be used then cleaned up after
def setUp(self, file):
    make_file(file)

def tearDown(self, file):
    close_file(file)

def make_file(test_file_name):
    file = open(test_file_name, "x")
    content = file.read()
    return content


def close_file(test_file_name):
    try:
        os.path.exists(test_file_name)
        os.remove(test_file_name)
    except FileExistsError as e:
        print(f"The file does not exist: {e}")


class TestValidatorMethods(unittest.TestCase):
    
    # test case: does the program correctly load rules when the configuration file is valid?
    def test_config_accuracy(self):
        config = validator.read_config("tests/test_rules.json")
        self.assertEqual(config['minimum_length'], 7)
        self.assertEqual(config['maximum_length'], 42)
        self.assertFalse(config["upper_case"])
        self.assertTrue(config['lower_case'])
        self.assertFalse(config['special_char'])
        self.assertTrue(config['numbers'])
        self.assertFalse(config['pattern_check'])
        self.assertEqual(config['blacklist'], ['andrew', 'trigger', 'sunshine', 'iloveyou'])

    #tests for malformed configuration file
    # test case: does the program handle malformed json gracefully?
    def test_malformedjson_handling(self):
        try:
            config = validator.read_config("tests/malformed_rules.json")
        except EOFError as e:
            print(f"Configuration file error: {e}")

    #tests for configurations that have no value paired
    #tests for missing configurations
    def test_missing_config(self):
        test_case = ''
        try:
            config = validator.read_config(test_case)
        except FileNotFoundError as e:
            print(f"File Error: {e}")

        self.assertTrue(config, config)

if __name__ == '__main__':
    unittest.main()