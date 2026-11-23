<div align="center">

# ⚡ Bin2Dec & Dec2Bin Base Converter ⚡

**A dual-engine, constraint-compliant bidirectional base converter built with modern Web technologies and Python.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![JavaScript: ES6+](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Tests: 13 Passed](https://img.shields.io/badge/Tests-13%20Passed-10B981?logo=checkmarx&logoColor=white)](#-automated-testing)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/pabitralenka07/Bin2dec-converter/pulls)

<p align="center">
  <a href="#-about-the-project">About</a> •
  <a href="#-challenge-constraints">Constraints</a> •
  <a href="#-features">Features</a> •
  <a href="#-mathematical-breakdown">Math</a> •
  <a href="#-getting-started">Getting Started</a> •
  <a href="#-project-structure">Structure</a> •
  <a href="#-author">Author</a>
</p>

---

</div>

## 📖 Table of Contents

- [💡 About The Project](#-about-the-project)
- [🎯 Challenge Constraints & Compliance](#-challenge-constraints--compliance)
- [✨ Features](#-features)
- [🧮 Mathematical Breakdown](#-mathematical-breakdown)
  - [1. Binary to Decimal (Base 2 ➔ Base 10)](#1-binary-to-decimal-base-2--base-10)
  - [2. Decimal to Binary (Base 10 ➔ Base 2)](#2-decimal-to-binary-base-10--base-2)
- [🚀 Getting Started](#-getting-started)
  - [🌐 1. Web Application](#-1-web-application)
  - [💻 2. Python Terminal CLI](#-2-python-terminal-cli)
  - [🖥️ 3. Python Tkinter Desktop App](#️-3-python-tkinter-desktop-app)
- [🧪 Automated Testing](#-automated-testing)
- [📁 Project Structure](#-project-structure)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👤 Author](#-author)

---

## 💡 About The Project

Binary is the fundamental language of digital computing. The **Bin2Dec** challenge from [florinpop17/app-ideas](https://github.com/florinpop17/app-ideas) (Tier 1 - Beginner) provides hands-on practice understanding how binary arithmetic works under strict algorithmic constraints.

This repository takes the challenge to the next level by:
1. Supporting **full bidirectional conversion** (**Bin ➔ Dec** and **Dec ➔ Bin**).
2. Providing **two complete implementations**:
   - A **sleek, responsive Web Application** with live visual bit weights and dark-mode styling.
   - A **Python Suite** featuring an interactive colored CLI and a native desktop GUI with `tkinter`.
3. Honoring all constraints with zero compromises.

---

## 🎯 Challenge Constraints & Compliance

The challenge outlines two non-negotiable rules. Here is how both the Web and Python implementations strictly follow them:

| Challenge Constraint | How It Is Strictly Honored |
| :--- | :--- |
| 🚫 **No Arrays for Binary Digits**<br>*(Arrays/lists may not be used to contain user binary digits)* | <ul><li>**JavaScript:** Never calls `.split('')` or `Array.from()`. Digits are inspected directly using `string.charAt(i)` and string concatenation.</li><li>**Python:** Avoids `list(s)` or digit arrays. Accesses characters via direct string indexing `s[i]`.</li></ul> |
| 📐 **Single Mathematical Function**<br>*(Decimal weight must be calculated using a single math function)* | <ul><li>**JavaScript:** Uses base-2 power exponentiation via `Math.pow(2, power)`.</li><li>**Python:** Uses built-in exponentiation `pow(2, power)`.</li></ul> |

---

## ✨ Features

- 🔄 **Bidirectional Base Conversion:**
  - **Bin ➔ Dec:** Enter binary digits (`0` & `1`) to compute decimal values with instant power breakdown.
  - **Dec ➔ Bin:** Enter any non-negative integer to compute binary representations via successive division.
  - **Instant Swap Button (`⇄`):** Flips the direction on the fly and transfers the result for round-trip verification.

- 🛡️ **Real-Time Input Validation:**
  - Rejects non-binary inputs instantly with animated alert banners.
  - Capped at **8 bits** ($0$ to $255$) by default, matching standard byte architectures.

- 🌟 **Bonus Mode (Unlimited Digits):**
  - Toggle switch unlocks variable-length strings (e.g. 16-bit, 32-bit, or arbitrary length).

- 💊 **Interactive Bit Weight Pills (Web):**
  - Displays each bit position ($2^7, 2^6, \dots, 2^0$) with glowing highlights for active bits.

- ⌨️ **Dynamic On-Screen Dial Pads:**
  - Binary keypad (`0`, `1`, `🎲 Random`, `⌫ Backspace`).
  - Decimal keypad (`0` through `9`, `🎲 Random Decimal`, `⌫ Backspace`).

- 📋 **One-Click Clipboard Copy:**
  - Easily copy results with visual feedback.

- 🎨 **Modern Cyber Dark Theme:**
  - High-contrast, accessibility-focused UI styled with CSS custom properties and grid backgrounds.

---

## 🧮 Mathematical Breakdown

### 1. Binary to Decimal (Base 2 ➔ Base 10)

For any $n$-bit binary number $b_{n-1}b_{n-2}\dots b_1b_0$:

$$\text{Decimal} = \sum_{i=0}^{n-1} b_i \times 2^i$$

#### Example: `1101`
- Position 0 ($2^0 = 1$): $1 \times 1 = 1$
- Position 1 ($2^1 = 2$): $0 \times 2 = 0$
- Position 2 ($2^2 = 4$): $1 \times 4 = 4$
- Position 3 ($2^3 = 8$): $1 \times 8 = 8$
- **Total:** $8 + 4 + 0 + 1 = 13_{10}$

---

### 2. Decimal to Binary (Base 10 ➔ Base 2)

Calculated via **successive division by 2** where remainders are read from bottom to top:

$$n = 2q + r \quad (r \in \{0, 1\})$$

#### Example: `13`
- $13 \div 2 = 6$, Remainder: **`1`**  *(Least Significant Bit)*
- $6 \div 2 = 3$, Remainder: **`0`**
- $3 \div 2 = 1$, Remainder: **`1`**
- $1 \div 2 = 0$, Remainder: **`1`**  *(Most Significant Bit)*
- **Result:** **`1101₂`**

---

## 🚀 Getting Started

Clone the repository to your local machine:

```bash
git clone https://github.com/pabitralenka07/Bin2dec-converter.git
cd Bin2dec-converter
```

### 🌐 1. Web Application

No build tools or npm dependencies required! 

Option A — Open directly:
* Double-click [index.html](index.html) in your file manager.

Option B — Run with a lightweight Python server:
```bash
python3 -m http.server 8000
```
Open your browser and navigate to: **`http://localhost:8000`**

---

### 💻 2. Python Terminal CLI

Run the interactive terminal interface:

```bash
python3 converter.py
```

```text
============================================================
      Bin2Dec & Dec2Bin Converter (Python Edition)
  Tier 1 Challenge · Zero Array Storage · pow(2, i)
============================================================

Select an option:
  1) Binary to Decimal (Standard: up to 8 bits)
  2) Binary to Decimal (Bonus: unlimited bits)
  3) Decimal to Binary (Standard: 0 to 255)
  4) Decimal to Binary (Bonus: unlimited magnitude)
  5) Launch Desktop GUI
  6) Exit
```

---

### 🖥️ 3. Python Tkinter Desktop App

Launch the native desktop window:

```bash
python3 gui.py
```

* Features real-time calculation as you type.
* Includes tab toggles, direction swap, and clipboard integration.

---

## 🧪 Automated Testing

A dedicated test suite built with Python's standard `unittest` framework covers all conversions, constraint validations, edge cases, and round-trip consistency.

Run the tests:
```bash
python3 -m unittest test_converter.py -v
```

### Test Coverage Highlights:
- ✅ Single-bit and multi-bit conversions (`0`, `1`, `1101`, `11111111`).
- ✅ Leading zero handling (`00001101` $\to$ `13`).
- ✅ 8-bit boundary constraint enforcement ($>8$ bits or $>255$).
- ✅ Bonus mode unlimited conversions (e.g. $1024 \leftrightarrow 10000000000_2$).
- ✅ Rejection of invalid characters (`102`, `abc`, `1 0`, negatives).
- ✅ Empty string validation.
- ✅ Full bidirectional roundtrip consistency across all integers $0 \le n \le 512$.

---

## 📁 Project Structure

```text
Bin2dec-converter/
│
├── 🌐 Web Interface
│   ├── index.html         # HTML5 layout, UI controls & formula cards
│   ├── style.css          # Responsive dark cyber theme styling
│   └── app.js             # Pure JavaScript conversion engine & DOM updates
│
├── 🐍 Python Suite
│   ├── converter.py       # Core conversion logic & interactive CLI
│   ├── gui.py             # Tkinter desktop graphical interface
│   └── test_converter.py  # 13 automated unit tests
│
├── ⚙️ Configuration & Documentation
│   ├── .gitignore         # Git ignore rules for Python & OS files
│   └── README.md          # Comprehensive documentation
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'feat: add amazing feature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 👤 Author

**Pabitra Lenka**
- GitHub: [@pabitralenka07](https://github.com/pabitralenka07)
- Repository: [Bin2dec-converter](https://github.com/pabitralenka07/Bin2dec-converter)

<div align="center">
  <sub>Built with ❤️ for clean code & computer science fundamentals.</sub>
</div>
