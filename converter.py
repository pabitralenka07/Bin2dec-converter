#!/usr/bin/env python3
"""
Bin2Dec & Dec2Bin - Base Converter (Python CLI & Core Engine)

CHALLENGE CONSTRAINTS HONORED:
1. Arrays may NOT be used to contain the binary digits entered by the user.
   -> Uses direct string character indexing without creating lists or arrays of digits.
2. Determining the decimal equivalent of each binary digit must use a single mathematical function.
   -> Uses pow(2, power) for calculating the decimal weight of each bit.
"""

import sys
import math


def validate_binary_string(binary_str: str) -> tuple[bool, str]:
    """
    Validates that the input contains only '0' and '1' characters
    WITHOUT converting the string into an array.
    """
    if not binary_str:
        return False, "Input cannot be empty."

    for i in range(len(binary_str)):
        ch = binary_str[i]
        if ch != '0' and ch != '1':
            return False, f"Invalid character '{ch}'. Only 0 and 1 are permitted."

    return True, ""


def bin_to_dec(binary_str: str, max_bits: int = 8) -> tuple[int, list[str]]:
    """
    Converts a binary string to its decimal equivalent.
    
    Constraints enforced:
    - No arrays/lists used to store the binary digits.
    - Uses single mathematical function: pow(2, power).
    
    Returns:
        (decimal_value, step_explanations)
    """
    binary_str = binary_str.strip()
    
    # Check max length if not unlimited (max_bits is None or 0 for unlimited)
    if max_bits and len(binary_str) > max_bits:
        raise ValueError(f"Binary string exceeds maximum limit of {max_bits} digits (got {len(binary_str)}).")

    is_valid, err_msg = validate_binary_string(binary_str)
    if not is_valid:
        raise ValueError(err_msg)

    decimal_total = 0
    str_len = len(binary_str)
    steps = []

    for i in range(str_len):
        # Character extracted directly by index (no array creation)
        ch = binary_str[i]
        power = str_len - 1 - i
        bit = 1 if ch == '1' else 0

        # Mathematical function per constraint:
        weight = pow(2, power)
        contribution = bit * weight
        decimal_total += contribution

        steps.append(
            f"Bit at index {i} (2^{power} = {weight}): {bit} * {weight} = {contribution}"
        )

    return decimal_total, steps


def dec_to_bin(decimal_num: int, max_bits: int = 8) -> tuple[str, list[str]]:
    """
    Converts a non-negative decimal integer to a binary string.
    
    Constraints enforced:
    - Zero arrays used for digit storage.
    - Uses repeated modulo (decimal_num % 2) and integer division (// 2).
    
    Returns:
        (binary_string, step_explanations)
    """
    if decimal_num < 0:
        raise ValueError("Decimal number must be non-negative.")

    if max_bits and decimal_num >= pow(2, max_bits):
        max_val = pow(2, max_bits) - 1
        raise ValueError(f"Decimal value {decimal_num} exceeds 8-bit maximum of {max_val}.")

    if decimal_num == 0:
        return "0", ["0 / 2 = 0, Remainder: 0"]

    binary_result = ""
    current = decimal_num
    steps = []

    while current > 0:
        remainder = current % 2
        quotient = current // 2
        steps.append(f"{current} // 2 = {quotient}, Remainder = {remainder}")
        # Prepend directly to string without list/array
        binary_result = str(remainder) + binary_result
        current = quotient

    return binary_result, steps


# ANSI Terminal Colors
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


def print_banner():
    print(f"{CYAN}{BOLD}")
    print("=" * 60)
    print("      Bin2Dec & Dec2Bin Converter (Python Edition)")
    print("  Tier 1 Challenge · Zero Array Storage · pow(2, i)")
    print("=" * 60 + f"{RESET}\n")


def cli_interactive():
    print_banner()

    while True:
        print(f"{BOLD}Select an option:{RESET}")
        print("  1) Binary to Decimal (Standard: up to 8 bits)")
        print("  2) Binary to Decimal (Bonus: unlimited bits)")
        print("  3) Decimal to Binary (Standard: 0 to 255)")
        print("  4) Decimal to Binary (Bonus: unlimited magnitude)")
        print("  5) Launch Desktop GUI")
        print("  6) Exit")

        choice = input(f"\n{CYAN}Enter choice (1-6): {RESET}").strip()

        if choice == "1":
            raw = input(f"{BOLD}Enter binary digits (up to 8 bits): {RESET}").strip()
            try:
                dec_val, steps = bin_to_dec(raw, max_bits=8)
                print(f"\n{GREEN}{BOLD}Decimal Result: {dec_val}{RESET}")
                print(f"{YELLOW}Mathematical Breakdown:{RESET}")
                for s in steps:
                    print(f"  • {s}")
                print(f"  {CYAN}Total = {dec_val}{RESET}\n")
            except ValueError as e:
                print(f"{RED}Error: {e}{RESET}\n")

        elif choice == "2":
            raw = input(f"{BOLD}Enter binary digits (unlimited length): {RESET}").strip()
            try:
                dec_val, steps = bin_to_dec(raw, max_bits=0)
                print(f"\n{GREEN}{BOLD}Decimal Result: {dec_val}{RESET}")
                print(f"{YELLOW}Mathematical Breakdown ({len(steps)} bits):{RESET}")
                # Print breakdown summary
                if len(steps) > 16:
                    for s in steps[:8]:
                        print(f"  • {s}")
                    print("    ...")
                    for s in steps[-4:]:
                        print(f"  • {s}")
                else:
                    for s in steps:
                        print(f"  • {s}")
                print(f"  {CYAN}Total = {dec_val}{RESET}\n")
            except ValueError as e:
                print(f"{RED}Error: {e}{RESET}\n")

        elif choice == "3":
            raw = input(f"{BOLD}Enter decimal integer (0 to 255): {RESET}").strip()
            try:
                num = int(raw)
                bin_str, steps = dec_to_bin(num, max_bits=8)
                print(f"\n{GREEN}{BOLD}Binary Result: {bin_str}{RESET}")
                print(f"{YELLOW}Successive Division Steps:{RESET}")
                for s in steps:
                    print(f"  • {s}")
                print(f"  {CYAN}Resulting Binary = {bin_str}{RESET}\n")
            except ValueError as e:
                print(f"{RED}Error: {e}{RESET}\n")

        elif choice == "4":
            raw = input(f"{BOLD}Enter decimal integer (unlimited): {RESET}").strip()
            try:
                num = int(raw)
                bin_str, steps = dec_to_bin(num, max_bits=0)
                print(f"\n{GREEN}{BOLD}Binary Result: {bin_str}{RESET}")
                print(f"{YELLOW}Successive Division Steps ({len(steps)} steps):{RESET}")
                if len(steps) > 16:
                    for s in steps[:6]:
                        print(f"  • {s}")
                    print("    ...")
                    for s in steps[-4:]:
                        print(f"  • {s}")
                else:
                    for s in steps:
                        print(f"  • {s}")
                print(f"  {CYAN}Resulting Binary = {bin_str}{RESET}\n")
            except ValueError as e:
                print(f"{RED}Error: {e}{RESET}\n")

        elif choice == "5":
            try:
                import gui
                print(f"{GREEN}Launching Desktop GUI...{RESET}")
                gui.launch_gui()
            except Exception as e:
                print(f"{RED}Failed to launch GUI: {e}{RESET}\n")

        elif choice == "6" or choice.lower() in ("exit", "q", "quit"):
            print(f"{CYAN}Goodbye!{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}Invalid selection. Please choose 1-6.{RESET}\n")


if __name__ == "__main__":
    cli_interactive()
