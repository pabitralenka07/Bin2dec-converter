# Bin2Dec & Dec2Bin Converter

An interactive, constraint-compliant base converter built for both **Web** (HTML5, CSS3, JavaScript) and **Python** (Terminal CLI & Tkinter Desktop GUI).

Based on the [florinpop17/app-ideas](https://github.com/florinpop17/app-ideas) **Tier-1 (Beginner)** project specification, with full bidirectional support (Binary to Decimal and Decimal to Binary).

---

## 📌 Core Constraints & Challenge Rules

This implementation strictly complies with all original challenge constraints:

1. **Zero Array Storage:** Arrays/lists are **never** used to contain or split the user's input digits. Digits are extracted directly through string indexing (`charAt(i)` / `str[i]`).
2. **Single Mathematical Function:** Determining the decimal equivalent of each binary digit uses a single mathematical function: base-2 exponentiation (`Math.pow(2, power)` in JavaScript and `pow(2, power)` in Python).
3. **Strict Validation:** Only binary digits (`0` and `1`) are accepted in binary mode; any other character triggers an immediate warning notification.
4. **Limits & Bonus Mode:** Default 8-bit mode ($0$ to $255$), with a toggleable **Bonus Mode** supporting arbitrary-length binary numbers and unlimited decimal values.

---

## ✨ Features

- **Bidirectional Conversion:**
  - **Bin ➔ Dec:** Live power-of-2 breakdown ($\sum \text{bit}_i \times 2^i$).
  - **Dec ➔ Bin:** Step-by-step successive division ($n = 2q + r$).
- **Dual Implementations:**
  - **Web App:** Modern dark-mode UI, interactive bit weight visualizer, quick dial pads, copy to clipboard, and instant direction swap.
  - **Python Suite:**
    - Interactive colored terminal CLI (`converter.py`).
    - Native dark-mode desktop window with Tkinter (`gui.py`).
    - Comprehensive test suite (`test_converter.py`).

---

## 🚀 Getting Started

### 1. Web Application

Simply open `index.html` in any web browser, or serve it locally:

```bash
python3 -m http.server 8000
```
Then visit `http://localhost:8000` in your browser.

---

### 2. Python Suite

#### Terminal CLI:
```bash
python3 converter.py
```

#### Native Desktop GUI (Tkinter):
```bash
python3 gui.py
```

#### Run Automated Tests:
```bash
python3 -m unittest test_converter.py -v
```

---

## 📁 Project Structure

```text
├── index.html         # Web application layout & components
├── style.css          # Responsive dark-theme styling
├── app.js             # Web converter engine & visualizer
├── converter.py       # Python core engine & CLI runner
├── gui.py             # Python Tkinter desktop GUI
├── test_converter.py  # Unit test suite
└── README.md          # Project documentation
```

---

## 📄 License

MIT License. Free to use, modify, and learn from!
