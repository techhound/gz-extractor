# GZ Extractor Web App

A lightweight Streamlit app that extracts `.gz` files directly in the browser and returns the uncompressed version with its original name (minus `.gz`).

## 🔧 Features

- Accepts any valid `.gz` file
- Automatically decompresses and renames the output to match the uploaded filename (without `.gz`)
- Clean, single-page UI powered by Streamlit
- Built with modern dependency management using `uv`

---

## ⚙️ Setup Instructions

This project was bootstrapped using [`uv`](https://github.com/astral-sh/uv) — a lightning-fast Python package manager written in Rust.

### ✅ Recommended: Setup with `uv`

If you don’t have `uv`, install it (only once):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
