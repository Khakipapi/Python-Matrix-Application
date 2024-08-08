import re
import numpy as np
from datetime import date

print("Name: Jose Reyes")
print("Course: SDEV300")
print("Date: ", date.today())

print("*************************Welcome to Python Matrix Application************************")


def play():
    print("Do you want to play the matrix game?")
    ans = ''
    while len(ans) != 1 or ans != 'Y':

        ans = input("Enter y for Yes and n for No: ")
        ans = ans.upper()
        if len(ans) != 1 or ans != 'Y':
            print("Invalid entry: answer must be either Y or N ")
        if ans == 'N':
            print(" Thank you for using this app.")
            break
    phonenum()
    zipcode()


def phonenum():
    """phone number function"""
    phone = ''
    while len(phone) != 12 or phone[3] and phone[7] != '-' or \
            phone[:2].isnumeric() is False or phone[5:7].isnumeric() is False or \
            phone[9:].isnumeric() is False:
        phone = input("Please enter your phone number (xxx-xxx-xxxx): ")

        if len(phone) != 12 or phone[3] and phone[7] != '-' or \
                phone[:2].isnumeric() is False or phone[5:7].isnumeric() is False or \
                phone[9:].isnumeric() is False:
            print("\ninvalid entry: Improper format must be (XXX-XXX-XXXX)\n")


def zipcode():
    """zipcode function"""
    zipcode1 = ""
    while len(zipcode1) != 10 or zipcode1[5] != '-' or \
            zipcode1[:4].isnumeric() is False or zipcode1[6:].isnumeric() is False:
        zipcode1 = input("Please enter your zipcode+4 (xxxxx-xxxx): ")

        if len(zipcode1) != 10 or zipcode1[5] != '-' or \
                zipcode1[:4].isnumeric() is False or zipcode1[6:].isnumeric() is False:
            print("\ninvalid entry: Improper format must be (XXXXX-XXXX)\n")


def matrix():
    """3x3 matrix function"""
    first = np.array(3,)


    print(first)


matrix()
