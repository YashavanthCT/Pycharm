from selenium import webdriver

from PageObjects.AccountSettings import Login__01
import time


class TestData:
    BASE_URL = "https://phoenixnew-app-dev.azurewebsites.net/login"
    USER_NAME = "lakshmi.halaharvi+15Org06@jenesystech.com"
    PASSWORD = "Testing@1"
    FirstName = "Yashwanth"
    MiddleName = "Sundra"
    LastName = "CT"
    PreferredName = "Rocky Bhai"
    DateOfBirth = "15-04-1998"
    CountryCode = "(+91) India"
    PhoneNumber = "8073987857"
    PhoneNumberOtp = "789051"
    CurrentPassword = "Testing@1"
    NewPassword = "Testing@123"
    VerifyPassword = "Testing@123"
    EmergencyContactFirstName = "Jamuna Madam"
    EmergencyContactLastName = "Kumaraswamy"
    EmergencyContactEmailName = "jamuna.kumaraswamy@jenesystech.com"
    EmergencyContactCountryCode = "(+91) India"
    EmergencyContactPhoneNumber = "9071085815"
    EmergencyContactRelation = "Sister"

