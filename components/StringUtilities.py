import re

class StringUtilities:

    @staticmethod
    def custom_split(input_string, start_char, end_char):
        """Defines and returns all sub-strings based on the beginning and end inputs specified"""
        matches = []
        start_index = 0

        while True:
            start_pos = input_string.find(start_char, start_index)
            if start_pos == -1:
                break

            end_pos = input_string.find(end_char, start_pos + 1)
            if end_pos == -1:
                break

            match = input_string[start_pos:end_pos + 1]
            matches.append(match)

            start_index = end_pos + 1

        return matches

        
