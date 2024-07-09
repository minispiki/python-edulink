import os

from edulink import Student

me = Student()

me.authenticate(os.getenv("username"), os.getenv("password"), os.getenv("postcode"))

print(me.timetable())  # Prints timetable in dictionary form
