const appTitle = document.getElementById('appTitle');
const appSubtitle = document.getElementById('appSubtitle');
const tabBin2Dec = document.getElementById('tabBin2Dec');
const tabDec2Bin = document.getElementById('tabDec2Bin');
const swapDirectionBtn = document.getElementById('swapDirectionBtn');
const mathConstraintTag = document.getElementById('mathConstraintTag');

const mainInput = document.getElementById('mainInput');
const mainOutput = document.getElementById('mainOutput');
const inputLabel = document.getElementById('inputLabel');
const outputLabel = document.getElementById('outputLabel');

const errorNotification = document.getElementById('errorNotification');
const errorMessage = document.getElementById('errorMessage');
const digitCounter = document.getElementById('digitCounter');
const unlimitedModeToggle = document.getElementById('unlimitedModeToggle');
const unlimitedModeLabel = document.getElementById('unlimitedModeLabel');

const clearBtn = document.getElementById('clearBtn');
const copyBtn = document.getElementById('copyBtn');
const copyText = document.getElementById('copyText');

const numpad = document.getElementById('numpad');
const decimalNumpad = document.getElementById('decimalNumpad');
const binaryKeyBtns = document.querySelectorAll('#numpad .key-btn[data-val]');
const decimalKeyBtns = document.querySelectorAll('.dec-key');
const randomBtn = document.getElementById('randomBtn');
const backspaceBtn = document.getElementById('backspaceBtn');
const randomDecBtn = document.getElementById('randomDecBtn');
const backspaceDecBtn = document.getElementById('backspaceDecBtn');

const bitVisualizer = document.getElementById('bitVisualizer');
const mathDetails = document.getElementById('mathDetails');
const mathSteps = document.getElementById('mathSteps');
const breakdownTitle = document.getElementById('breakdownTitle');
const mathFormula = document.getElementById('mathFormula');

let currentMode = 'bin2dec';
let isUnlimitedMode = false;

const MODES = {
  bin2dec: {
    title: 'Bin<span class="highlight">2</span>Dec',
    subtitle: 'Convert binary (base 2) into decimal (base 10) with real-time mathematical breakdown.',
    inputLabel: 'Binary Input (0s & 1s only)',
    outputLabel: 'Decimal Result (Base 10)',
    placeholder: 'e.g. 11010010',
    unlimitedPlaceholder: 'e.g. 1011010011010111',
    unlimitedLabel: 'Bonus Mode: Variable length (unlimited digits)',
    constraint: '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg> Single Math Function: <code>Math.pow(2, i)</code>',
    formula: '$$\\sum (\\text{bit}_i \\times 2^i)$$'
  },
  dec2bin: {
    title: 'Dec<span class="highlight">2</span>Bin',
    subtitle: 'Convert decimal (base 10) into binary (base 2) with successive division breakdown.',
    inputLabel: 'Decimal Input (0-9)',
    outputLabel: 'Binary Result (Base 2)',
    placeholder: 'e.g. 210 (max 255 for 8-bit)',
    unlimitedPlaceholder: 'e.g. 46295',
    unlimitedLabel: 'Bonus Mode: Unlimited magnitude (unlimited bits)',
    constraint: '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg> Successive Modulo: <code>n % 2</code>',
    formula: '$$n = 2q + r$$'
  }
};

function setMode(mode, transferValue = false) {
  currentMode = mode;

  tabBin2Dec.classList.toggle('active', mode === 'bin2dec');
  tabDec2Bin.classList.toggle('active', mode === 'dec2bin');

  const config = MODES[mode];
  appTitle.innerHTML = config.title;
  appSubtitle.textContent = config.subtitle;
  inputLabel.textContent = config.inputLabel;
  outputLabel.textContent = config.outputLabel;
  mathConstraintTag.innerHTML = config.constraint;
  mathFormula.textContent = config.formula;
  unlimitedModeLabel.textContent = config.unlimitedLabel;

  numpad.classList.toggle('hidden', mode !== 'bin2dec');
  decimalNumpad.classList.toggle('hidden', mode !== 'dec2bin');

  if (mode === 'bin2dec') {
    if (isUnlimitedMode) {
      mainInput.removeAttribute('maxlength');
      mainInput.placeholder = config.unlimitedPlaceholder;
    } else {
      mainInput.setAttribute('maxlength', '8');
      mainInput.placeholder = config.placeholder;
    }
  } else {
    if (isUnlimitedMode) {
      mainInput.removeAttribute('maxlength');
      mainInput.placeholder = config.unlimitedPlaceholder;
    } else {
      mainInput.setAttribute('maxlength', '3');
      mainInput.placeholder = config.placeholder;
    }
  }

  if (transferValue) {
    const rawPrevOutput = mainOutput.value.replace(/,/g, '').trim();
    if (rawPrevOutput && rawPrevOutput !== '0' && rawPrevOutput !== 'Error') {
      mainInput.value = rawPrevOutput;
    } else {
      mainInput.value = '';
    }
  } else {
    mainInput.value = '';
  }

  hideError();
  processConversion();
  mainInput.focus();
}

function showError(message) {
  errorMessage.textContent = message;
  errorNotification.classList.remove('hidden');
  mainInput.classList.add('invalid');
}

function hideError() {
  errorNotification.classList.add('hidden');
  mainInput.classList.remove('invalid');
}

function updateCounter() {
  const len = mainInput.value.length;
  if (currentMode === 'bin2dec') {
    if (isUnlimitedMode) {
      digitCounter.textContent = `${len} bit${len === 1 ? '' : 's'}`;
    } else {
      digitCounter.textContent = `${len} / 8 bits`;
    }
  } else {
    if (isUnlimitedMode) {
      digitCounter.textContent = `${len} digit${len === 1 ? '' : 's'}`;
    } else {
      const val = parseInt(mainInput.value, 10) || 0;
      digitCounter.textContent = `${val} / 255 (8-bit max)`;
    }
  }
}

function processConversion() {
  clearBtn.classList.toggle('visible', mainInput.value.length > 0);
  updateCounter();

  if (currentMode === 'bin2dec') {
    convertBinaryToDecimal();
  } else {
    convertDecimalToBinary();
  }
}

function convertBinaryToDecimal() {
  const inputStr = mainInput.value;

  if (inputStr.length === 0) {
    hideError();
    mainOutput.value = '0';
    renderEmptyVisualizer('Bit pills will display here as you type.');
    renderEmptyMath('Enter binary digits above to inspect the formula.');
    return;
  }

  for (let i = 0; i < inputStr.length; i++) {
    const char = inputStr.charAt(i);
    if (char !== '0' && char !== '1') {
      showError(`Invalid character "${char}"! Only 0 and 1 are allowed in binary.`);
      mainOutput.value = 'Error';
      renderEmptyVisualizer('Invalid input.');
      renderEmptyMath('Fix errors above to compute.');
      return;
    }
  }

  hideError();

  let decimalTotal = 0;
  const len = inputStr.length;
  let mathHtml = '';
  let pillsHtml = '';

  for (let i = 0; i < len; i++) {
    const char = inputStr.charAt(i);
    const power = len - 1 - i;
    const bit = char === '1' ? 1 : 0;
    
    const weight = Math.pow(2, power);
    const contribution = bit * weight;
    decimalTotal += contribution;

    const isActive = bit === 1;
    pillsHtml += `
      <div class="bit-pill ${isActive ? 'active' : ''}">
        <span class="bit-val">${bit}</span>
        <span class="bit-weight">2<sup>${power}</sup> (${weight})</span>
      </div>
    `;

    mathHtml += `
      <div class="step-item">
        <span class="step-calc">
          <span class="${isActive ? 'calc-active' : ''}">${bit}</span> × 2<sup>${power}</sup>
          <span style="color: var(--text-muted);">(${bit} × ${weight})</span>
        </span>
        <span class="step-res">= ${contribution}</span>
      </div>
    `;
  }

  mainOutput.value = decimalTotal.toLocaleString('en-US');
  bitVisualizer.innerHTML = pillsHtml;

  mathHtml += `
    <div class="step-item" style="margin-top: 8px; padding-top: 8px; border-top: 1px solid var(--border-color); font-weight: bold;">
      <span class="step-calc" style="color: var(--accent-cyan);">Total Decimal (Base 10):</span>
      <span class="step-res" style="color: var(--accent-cyan); font-size: 1.05rem;">${decimalTotal.toLocaleString('en-US')}</span>
    </div>
  `;
  mathSteps.innerHTML = mathHtml;
}

function convertDecimalToBinary() {
  const inputStr = mainInput.value.trim();

  if (inputStr.length === 0) {
    hideError();
    mainOutput.value = '0';
    renderEmptyVisualizer('Binary bit pills will display here as you type.');
    renderEmptyMath('Enter a decimal number above to inspect successive division.');
    return;
  }

  for (let i = 0; i < inputStr.length; i++) {
    const char = inputStr.charAt(i);
    if (char < '0' || char > '9') {
      showError(`Invalid character "${char}"! Only digits 0-9 are allowed.`);
      mainOutput.value = 'Error';
      renderEmptyVisualizer('Invalid input.');
      renderEmptyMath('Fix errors above to compute.');
      return;
    }
  }

  const num = parseInt(inputStr, 10);

  if (!isUnlimitedMode && num > 255) {
    showError(`Number exceeds 255 (8-bit limit)! Enable Bonus Mode for unlimited values.`);
    mainOutput.value = 'Error';
    renderEmptyVisualizer('Exceeds 8-bit limit.');
    renderEmptyMath('Enable Bonus Mode above to continue.');
    return;
  }

  hideError();

  if (num === 0) {
    mainOutput.value = '0';
    bitVisualizer.innerHTML = `
      <div class="bit-pill">
        <span class="bit-val">0</span>
        <span class="bit-weight">2<sup>0</sup> (1)</span>
      </div>
    `;
    mathSteps.innerHTML = `
      <div class="step-item">
        <span class="step-calc">0 ÷ 2 = 0</span>
        <span class="step-res">Remainder: 0</span>
      </div>
    `;
    return;
  }

  let current = num;
  let binaryResult = '';
  let divisionStepsHtml = '';

  while (current > 0) {
    const remainder = current % 2;
    const quotient = Math.floor(current / 2);

    divisionStepsHtml = `
      <div class="step-item">
        <span class="step-calc">${current} ÷ 2 = ${quotient}</span>
        <span class="step-res">Remainder: <strong class="${remainder === 1 ? 'calc-active' : ''}">${remainder}</strong></span>
      </div>
    ` + divisionStepsHtml;

    binaryResult = remainder + binaryResult;
    current = quotient;
  }

  mainOutput.value = binaryResult;

  let pillsHtml = '';
  const bitLen = binaryResult.length;
  for (let i = 0; i < bitLen; i++) {
    const bit = binaryResult.charAt(i);
    const power = bitLen - 1 - i;
    const weight = Math.pow(2, power);
    const isActive = bit === '1';

    pillsHtml += `
      <div class="bit-pill ${isActive ? 'active' : ''}">
        <span class="bit-val">${bit}</span>
        <span class="bit-weight">2<sup>${power}</sup> (${weight})</span>
      </div>
    `;
  }
  bitVisualizer.innerHTML = pillsHtml;

  divisionStepsHtml += `
    <div class="step-item" style="margin-top: 8px; padding-top: 8px; border-top: 1px solid var(--border-color); font-weight: bold;">
      <span class="step-calc" style="color: var(--accent-cyan);">Resulting Binary (Base 2):</span>
      <span class="step-res" style="color: var(--accent-cyan); font-size: 1.05rem;">${binaryResult}</span>
    </div>
  `;
  mathSteps.innerHTML = divisionStepsHtml;
}

function renderEmptyVisualizer(msg) {
  bitVisualizer.innerHTML = `
    <span style="font-size: 0.85rem; color: var(--text-muted); align-self: center;">
      ${msg}
    </span>
  `;
}

function renderEmptyMath(msg) {
  mathSteps.innerHTML = `
    <div class="empty-state">${msg}</div>
  `;
}

tabBin2Dec.addEventListener('click', () => setMode('bin2dec', false));
tabDec2Bin.addEventListener('click', () => setMode('dec2bin', false));

swapDirectionBtn.addEventListener('click', () => {
  const nextMode = currentMode === 'bin2dec' ? 'dec2bin' : 'bin2dec';
  setMode(nextMode, true);
});

mainInput.addEventListener('input', () => {
  processConversion();
});

mainInput.addEventListener('keydown', (e) => {
  const allowedKeys = ['Backspace', 'Delete', 'ArrowLeft', 'ArrowRight', 'Home', 'End', 'Tab', 'Enter'];
  if (allowedKeys.includes(e.key) || e.ctrlKey || e.metaKey) {
    return;
  }

  if (currentMode === 'bin2dec') {
    if (e.key !== '0' && e.key !== '1') {
      e.preventDefault();
      showError(`Key "${e.key}" rejected. Only binary digits (0 and 1) are accepted.`);
      setTimeout(hideError, 2500);
    }
  } else {
    if (e.key < '0' || e.key > '9') {
      e.preventDefault();
      showError(`Key "${e.key}" rejected. Only decimal digits (0-9) are accepted.`);
      setTimeout(hideError, 2500);
    }
  }
});

clearBtn.addEventListener('click', () => {
  mainInput.value = '';
  mainInput.focus();
  processConversion();
});

unlimitedModeToggle.addEventListener('change', (e) => {
  isUnlimitedMode = e.target.checked;
  setMode(currentMode, false);
});

binaryKeyBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    const val = btn.getAttribute('data-val');
    if (!isUnlimitedMode && mainInput.value.length >= 8) {
      showError('Limit of 8 bits reached! Enable Bonus Mode for unlimited digits.');
      setTimeout(hideError, 2500);
      return;
    }
    mainInput.value += val;
    processConversion();
    mainInput.focus();
  });
});

decimalKeyBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    const val = btn.getAttribute('data-val');
    const nextValStr = mainInput.value + val;
    if (!isUnlimitedMode && parseInt(nextValStr, 10) > 255) {
      showError('Max 255 for 8-bit mode! Enable Bonus Mode for unlimited numbers.');
      setTimeout(hideError, 2500);
      return;
    }
    mainInput.value = nextValStr;
    processConversion();
    mainInput.focus();
  });
});

function handleBackspace() {
  if (mainInput.value.length > 0) {
    mainInput.value = mainInput.value.slice(0, -1);
    processConversion();
  }
  mainInput.focus();
}
backspaceBtn.addEventListener('click', handleBackspace);
backspaceDecBtn.addEventListener('click', handleBackspace);

randomBtn.addEventListener('click', () => {
  const targetLength = isUnlimitedMode ? Math.floor(Math.random() * 8) + 8 : 8;
  let randomBinary = '';
  for (let i = 0; i < targetLength; i++) {
    randomBinary += Math.random() < 0.5 ? '0' : '1';
  }
  mainInput.value = randomBinary;
  processConversion();
});

randomDecBtn.addEventListener('click', () => {
  const max = isUnlimitedMode ? 65535 : 255;
  const randomDecimal = Math.floor(Math.random() * max) + 1;
  mainInput.value = randomDecimal.toString();
  processConversion();
});

copyBtn.addEventListener('click', async () => {
  const textToCopy = mainOutput.value.replace(/,/g, '');
  if (!textToCopy || textToCopy === 'Error') return;

  try {
    await navigator.clipboard.writeText(textToCopy);
    copyBtn.classList.add('copied');
    copyText.textContent = 'Copied!';
    setTimeout(() => {
      copyBtn.classList.remove('copied');
      copyText.textContent = 'Copy';
    }, 1800);
  } catch (err) {
    const textArea = document.createElement('textarea');
    textArea.value = textToCopy;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand('copy');
    document.body.removeChild(textArea);
    copyBtn.classList.add('copied');
    copyText.textContent = 'Copied!';
    setTimeout(() => {
      copyBtn.classList.remove('copied');
      copyText.textContent = 'Copy';
    }, 1800);
  }
});

setMode('bin2dec', false);
