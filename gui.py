import tkinter as tk
from tkinter import ttk, messagebox
import converter


class BaseConverterGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Bin2Dec & Dec2Bin Base Converter")
        self.geometry("560x650")
        self.minsize(500, 580)
        self.configure(bg="#0a0f1d")

        self.mode = tk.StringVar(value="bin2dec")
        self.is_unlimited = tk.BooleanVar(value=False)

        self._build_styles()
        self._build_ui()
        self._on_mode_change()

    def _build_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure(".", background="#0a0f1d", foreground="#f8fafc")
        style.configure("TFrame", background="#0a0f1d")
        style.configure("Card.TFrame", background="#131b2e", relief="flat")
        
        style.configure(
            "Header.TLabel",
            background="#0a0f1d",
            foreground="#00f2fe",
            font=("Inter", 18, "bold"),
        )
        style.configure(
            "Subheader.TLabel",
            background="#0a0f1d",
            foreground="#94a3b8",
            font=("Inter", 10),
        )
        style.configure(
            "FieldLabel.TLabel",
            background="#131b2e",
            foreground="#94a3b8",
            font=("Inter", 9, "bold"),
        )
        style.configure(
            "Badge.TLabel",
            background="#0e1b30",
            foreground="#38bdf8",
            font=("Inter", 9),
            padding=(6, 3),
        )
        style.configure(
            "Error.TLabel",
            background="#131b2e",
            foreground="#ef4444",
            font=("Inter", 9),
        )

    def _build_ui(self):
        header_frame = ttk.Frame(self)
        header_frame.pack(fill="x", padx=24, pady=(20, 10))

        ttk.Label(
            header_frame,
            text="BASE CONVERTER",
            style="Badge.TLabel"
        ).pack(anchor="center", pady=(0, 6))

        self.title_label = ttk.Label(
            header_frame,
            text="Bin2Dec Converter",
            style="Header.TLabel"
        )
        self.title_label.pack(anchor="center")

        ttk.Label(
            header_frame,
            text="Zero Array Storage · Single Math Function pow(2, i)",
            style="Subheader.TLabel"
        ).pack(anchor="center", pady=(4, 0))

        card = ttk.Frame(self, style="Card.TFrame", padding=18)
        card.pack(fill="both", expand=True, padx=20, pady=10)

        mode_frame = tk.Frame(card, bg="#131b2e")
        mode_frame.pack(fill="x", pady=(0, 12))

        self.btn_bin2dec = tk.Button(
            mode_frame,
            text="Binary ➔ Decimal",
            command=lambda: self._set_mode("bin2dec"),
            font=("Inter", 10, "bold"),
            bg="#1b2640",
            fg="#00f2fe",
            activebackground="#00f2fe",
            activeforeground="#000000",
            relief="flat",
            padx=12,
            pady=6,
            cursor="hand2"
        )
        self.btn_bin2dec.pack(side="left", fill="x", expand=True, padx=(0, 4))

        self.btn_swap = tk.Button(
            mode_frame,
            text="⇄",
            command=self._swap_mode,
            font=("Inter", 12, "bold"),
            bg="#1b2640",
            fg="#f8fafc",
            activebackground="#38bdf8",
            activeforeground="#000",
            relief="flat",
            padx=10,
            pady=4,
            cursor="hand2"
        )
        self.btn_swap.pack(side="left", padx=4)

        self.btn_dec2bin = tk.Button(
            mode_frame,
            text="Decimal ➔ Binary",
            command=lambda: self._set_mode("dec2bin"),
            font=("Inter", 10, "bold"),
            bg="#0e1526",
            fg="#94a3b8",
            activebackground="#00f2fe",
            activeforeground="#000000",
            relief="flat",
            padx=12,
            pady=6,
            cursor="hand2"
        )
        self.btn_dec2bin.pack(side="left", fill="x", expand=True, padx=(4, 0))

        opt_frame = tk.Frame(card, bg="#131b2e")
        opt_frame.pack(fill="x", pady=(0, 10))

        self.unlimited_chk = tk.Checkbutton(
            opt_frame,
            text="Bonus Mode: Unlimited length/magnitude",
            variable=self.is_unlimited,
            command=self._on_input_changed,
            bg="#131b2e",
            fg="#94a3b8",
            activebackground="#131b2e",
            activeforeground="#00f2fe",
            selectcolor="#0a0f1d",
            font=("Inter", 9),
            cursor="hand2"
        )
        self.unlimited_chk.pack(side="left")

        self.counter_lbl = tk.Label(
            opt_frame,
            text="0 / 8 bits",
            bg="#0e1526",
            fg="#64748b",
            font=("Fira Code", 9),
            padx=6,
            pady=2
        )
        self.counter_lbl.pack(side="right")

        self.input_lbl = ttk.Label(card, text="BINARY INPUT (0s & 1s ONLY)", style="FieldLabel.TLabel")
        self.input_lbl.pack(anchor="w", pady=(4, 4))

        input_wrapper = tk.Frame(card, bg="#0e1526", highlightbackground="#1e293b", highlightthickness=1)
        input_wrapper.pack(fill="x", pady=(0, 4))

        self.entry_input = tk.Entry(
            input_wrapper,
            bg="#0e1526",
            fg="#f8fafc",
            insertbackground="#00f2fe",
            font=("Fira Code", 14, "bold"),
            relief="flat",
            bd=8
        )
        self.entry_input.pack(side="left", fill="x", expand=True)
        self.entry_input.bind("<KeyRelease>", lambda e: self._on_input_changed())

        btn_clear = tk.Button(
            input_wrapper,
            text="✕",
            command=self._clear_input,
            bg="#0e1526",
            fg="#64748b",
            activebackground="#0e1526",
            activeforeground="#f8fafc",
            relief="flat",
            bd=0,
            padx=8,
            cursor="hand2"
        )
        btn_clear.pack(side="right")

        self.error_lbl = ttk.Label(card, text="", style="Error.TLabel")
        self.error_lbl.pack(anchor="w", pady=(0, 6))

        self.output_lbl = ttk.Label(card, text="DECIMAL RESULT", style="FieldLabel.TLabel")
        self.output_lbl.pack(anchor="w", pady=(4, 4))

        output_wrapper = tk.Frame(card, bg="#090e1a", highlightbackground="#1e293b", highlightthickness=1)
        output_wrapper.pack(fill="x", pady=(0, 10))

        self.entry_output = tk.Entry(
            output_wrapper,
            bg="#090e1a",
            fg="#00f2fe",
            font=("Fira Code", 14, "bold"),
            relief="flat",
            bd=8,
            state="readonly"
        )
        self.entry_output.pack(side="left", fill="x", expand=True)

        btn_copy = tk.Button(
            output_wrapper,
            text="Copy",
            command=self._copy_output,
            bg="#1b2640",
            fg="#f8fafc",
            activebackground="#10b981",
            activeforeground="#000",
            font=("Inter", 9, "bold"),
            relief="flat",
            padx=10,
            pady=4,
            cursor="hand2"
        )
        btn_copy.pack(side="right", padx=4)

        breakdown_header = tk.Frame(card, bg="#131b2e")
        breakdown_header.pack(fill="x", pady=(6, 4))

        self.breakdown_title = ttk.Label(
            breakdown_header,
            text="MATHEMATICAL BREAKDOWN",
            style="FieldLabel.TLabel"
        )
        self.breakdown_title.pack(side="left")

        self.txt_steps = tk.Text(
            card,
            bg="#0e1526",
            fg="#94a3b8",
            insertbackground="#00f2fe",
            font=("Fira Code", 9),
            relief="flat",
            bd=8,
            height=8,
            wrap="word"
        )
        self.txt_steps.pack(fill="both", expand=True)
        self.txt_steps.config(state="disabled")

    def _set_mode(self, new_mode):
        self.mode.set(new_mode)
        self._on_mode_change()

    def _swap_mode(self):
        current_res = self.entry_output.get().strip()
        new_mode = "dec2bin" if self.mode.get() == "bin2dec" else "bin2dec"
        self.mode.set(new_mode)
        self._on_mode_change()
        
        if current_res and current_res != "Error" and current_res != "0":
            self.entry_input.delete(0, tk.END)
            self.entry_input.insert(0, current_res)
            self._on_input_changed()

    def _on_mode_change(self):
        m = self.mode.get()
        if m == "bin2dec":
            self.btn_bin2dec.config(bg="#1b2640", fg="#00f2fe")
            self.btn_dec2bin.config(bg="#0e1526", fg="#94a3b8")
            self.title_label.config(text="Bin2Dec Converter")
            self.input_lbl.config(text="BINARY INPUT (0s & 1s ONLY)")
            self.output_lbl.config(text="DECIMAL RESULT (BASE 10)")
        else:
            self.btn_bin2dec.config(bg="#0e1526", fg="#94a3b8")
            self.btn_dec2bin.config(bg="#1b2640", fg="#00f2fe")
            self.title_label.config(text="Dec2Bin Converter")
            self.input_lbl.config(text="DECIMAL INPUT (0-9)")
            self.output_lbl.config(text="BINARY RESULT (BASE 2)")

        self._on_input_changed()

    def _clear_input(self):
        self.entry_input.delete(0, tk.END)
        self._on_input_changed()

    def _copy_output(self):
        val = self.entry_output.get().strip()
        if val and val != "Error":
            self.clipboard_clear()
            self.clipboard_append(val)
            messagebox.showinfo("Copied", f"Copied to clipboard: {val}")

    def _set_output_text(self, text):
        self.entry_output.config(state="normal")
        self.entry_output.delete(0, tk.END)
        self.entry_output.insert(0, text)
        self.entry_output.config(state="readonly")

    def _set_steps_text(self, text):
        self.txt_steps.config(state="normal")
        self.txt_steps.delete("1.0", tk.END)
        self.txt_steps.insert("1.0", text)
        self.txt_steps.config(state="disabled")

    def _on_input_changed(self):
        val = self.entry_input.get().strip()
        m = self.mode.get()
        unlimited = self.is_unlimited.get()

        if m == "bin2dec":
            self.counter_lbl.config(text=f"{len(val)} bits" if unlimited else f"{len(val)} / 8 bits")
        else:
            self.counter_lbl.config(text=f"{len(val)} digits" if unlimited else f"{val or 0} / 255 (8-bit)")

        if not val:
            self.error_lbl.config(text="")
            self._set_output_text("0")
            self._set_steps_text("Enter digits above to inspect the formula.")
            return

        max_bits = 0 if unlimited else 8

        try:
            if m == "bin2dec":
                res, steps = converter.bin_to_dec(val, max_bits=max_bits)
                self.error_lbl.config(text="")
                self._set_output_text(str(res))
                breakdown = "\n".join([f"• {s}" for s in steps])
                breakdown += f"\n\nTotal Decimal = {res}"
                self._set_steps_text(breakdown)
            else:
                num = int(val)
                res, steps = converter.dec_to_bin(num, max_bits=max_bits)
                self.error_lbl.config(text="")
                self._set_output_text(res)
                breakdown = "\n".join([f"• {s}" for s in steps])
                breakdown += f"\n\nResulting Binary = {res}"
                self._set_steps_text(breakdown)
        except ValueError as err:
            self.error_lbl.config(text=f"⚠️ {err}")
            self._set_output_text("Error")
            self._set_steps_text(f"Computation paused: {err}")


def launch_gui():
    app = BaseConverterGUI()
    app.mainloop()


if __name__ == "__main__":
    launch_gui()
