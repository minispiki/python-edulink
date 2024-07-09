[![Package Validation](https://github.com/Richy-Z/python-edulink/actions/workflows/python-package.yml/badge.svg)](https://github.com/Richy-Z/python-edulink/actions/workflows/python-package.yml)

# 🏫 edulink for Python
A Python PyPI package that provides semless integration between the EduLink One API and Python.

It handles all authentication and the little things in the background for you. 😌

Overnet Data says:
> EduLink One is a whole school solution designed for teachers, parents and students to effectively colaborate in a user-friendly mobile and web app.

The EduLink One API is completely proprietary and undocumented, so the creation of this package required some reverse engineering.

Please note that this is **NOT** a full-fledged integration of the EduLink API. This library is incredibly limited and does not provide certain API methods such as teacher methods. **Only the student calls have been implemented**.

If you require an additional feature in this library, please create an issue and it will be added on-demand.

## 📥 Installation
Installing the package is incredibly easy, thanks to `pip`.

**COMING SOON TO PIP**

Type the following into your terminal to install the package:
```zsh
pip install edulink
```
Please note that macOS and most Linux distributions use `pip3`, as opposed to just regular `pip` on Windows.

Now you have the EduLink package installed!

## 🔨 Usage
Using this package is incredibly easy. Simply import it, create a student object, authenticate, and start creating API calls!

```py
from edulink import Student

me = Student()

me.authenticate("Username", "Password", "School Postcode")

print(me.timetable()) # Prints timetable in dictionary form
```

Documentation for this package will be created at a later date.

## ⚖️ Why the GPL License?
The research I put into this project is not worth putting into closed-source projects, and the EduLink One API is already proprietary enough without documentation.

## ⚠️ Disclaimer
This package is the result of ***reverse engineering efforts***...

...to understand the communication protocol between the client application and the EduLink One API itself. The EduLink One API is proprietary and undocumented. Although the intention behind this package is to facilitate seamless integration with Python and to explore for educational purposes how applications are built, it is important to be aware of potential legal implications.

Please use this package at ***your own risk***.

***Unauthorised access of certain school systems can become problematic***. Please stay within your student boundaries when using the API and do not attempt to access things you should not.

----------

I, the author, its contributors, and maintainers are not responsible for any actions, legal consequences, or issues that may arise as a result of using this package. Users are advised to review the Terms of Service and licensing agreements of EduLink One by Overnet Data Ltd. before incorporating this package into proper production projects.
