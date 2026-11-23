#!/usr/bin/env python3
"""
Unit Test Suite for Bin2Dec & Dec2Bin Converter
Verifies all algorithmic constraints and edge cases.
"""

import unittest
from converter import bin_to_dec, dec_to_bin, validate_binary_string


class TestBin2Dec(unittest.TestCase):
    def test_single_digits(self):
        val, _ = bin_to_dec("0")
        self.assertEqual(val, 0)
        val, _ = bin_to_dec("1")
        self.assertEqual(val, 1)

    def test_example_values(self):
        val, _ = bin_to_dec("1101")
        self.assertEqual(val, 13)

        val, _ = bin_to_dec("1010")
        self.assertEqual(val, 10)

        val, _ = bin_to_dec("11111111")
        self.assertEqual(val, 255)

    def test_leading_zeros(self):
        val, _ = bin_to_dec("00001101")
        self.assertEqual(val, 13)

    def test_exceeding_8_bits_raises_error(self):
        with self.assertRaises(ValueError):
            bin_to_dec("100000000", max_bits=8)  # 9 bits

    def test_bonus_unlimited_bits(self):
        # 1024 = 2^10 = '10000000000' (11 bits)
        val, _ = bin_to_dec("10000000000", max_bits=0)
        self.assertEqual(val, 1024)

    def test_invalid_characters_raise_error(self):
        for invalid_input in ["102", "1a0", "hello", "1 0", "1-0"]:
            with self.subTest(invalid_input=invalid_input):
                with self.assertRaises(ValueError):
                    bin_to_dec(invalid_input)

    def test_empty_input_raises_error(self):
        with self.assertRaises(ValueError):
            bin_to_dec("")


class TestDec2Bin(unittest.TestCase):
    def test_single_values(self):
        val, _ = dec_to_bin(0)
        self.assertEqual(val, "0")
        val, _ = dec_to_bin(1)
        self.assertEqual(val, "1")

    def test_example_values(self):
        val, _ = dec_to_bin(13)
        self.assertEqual(val, "1101")

        val, _ = dec_to_bin(255)
        self.assertEqual(val, "11111111")

    def test_8_bit_limit(self):
        with self.assertRaises(ValueError):
            dec_to_bin(256, max_bits=8)

    def test_bonus_unlimited_magnitude(self):
        val, _ = dec_to_bin(1024, max_bits=0)
        self.assertEqual(val, "10000000000")

    def test_negative_raises_error(self):
        with self.assertRaises(ValueError):
            dec_to_bin(-5)


class TestRoundTrip(unittest.TestCase):
    def test_bidirectional_roundtrip(self):
        # Test all values from 0 to 512
        for n in range(513):
            bin_str, _ = dec_to_bin(n, max_bits=0)
            dec_val, _ = bin_to_dec(bin_str, max_bits=0)
            self.assertEqual(dec_val, n, f"Roundtrip failed for {n}")


if __name__ == "__main__":
    unittest.main()
