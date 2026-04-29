Here’s a clean, professional **README.md** for your phone number location tracker project:

````md id="r7k3pl"
# 📱 Phone Number Location Tracker

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Library](https://img.shields.io/badge/Library-phonenumbers-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A simple Python project that takes a phone number with country code and returns its **geographical location (country/region)** using the `phonenumbers` library.

---

## 🚀 Features

- 🌍 Detects country/region of phone numbers
- 📞 Supports international format (+country code required)
- 🔁 Continuous lookup mode (check multiple numbers)
- ⚡ Lightweight and fast execution
- 🧠 Beginner-friendly Python project

---

## 📦 Installation

Install the required library:

```bash id="k2m8qv"
pip install phonenumbers
````

---

## ▶️ Usage

Run the script:

```bash id="v9n3lx"
python main.py
```

Then enter a phone number:

```id="c8p1qz"
Enter the phone number with country code: +8801712345678
```

Example output:

```id="x3m7tw"
Phone Number Location:
Bangladesh
```

---

## 🧾 How it works

* Takes user input (phone number with country code)
* Parses it using `phonenumbers.parse()`
* Uses `geocoder.description_for_number()` to find location
* Displays the result in English

---

## 📌 Requirements

```id="z8q2mv"
phonenumbers
```

---

## 💡 Example Code

```python id="t7n2pl"
import phonenumbers
from phonenumbers import geocoder

while True:
    phone_num1 = input('\nEnter the phone number with country code: ')
    phone_num = phonenumbers.parse(phone_num1)

    print('\nPhone Number Location:')
    print(geocoder.description_for_number(phone_num, 'en') + '\n')
```

---

## 🔥 Future Improvements

* 📡 Carrier (SIM operator) detection
* 🕒 Timezone detection
* 🖥 GUI version using Tkinter
* 🌐 Web-based tracker (Flask)
* 📊 Number validation system

---

## 👨‍💻 Author

Made with Python 💙
Simple beginner-friendly utility project

- Nahian Nir.