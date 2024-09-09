# OTP Generator and Discount Application

## Project Overview
This project is an OTP (One-Time Password) generator and discount application written in Python. The program takes a phone number and a total purchase amount as inputs. If the phone number is new (not previously used), it generates a one-time password (OTP) that allows the user to receive a 25% discount on their total. Returning users do not get the discount.

## Features
- **OTP Generation**: Generates a random OTP for new phone numbers.
- **Phone Number Validation**: Ensures the phone number is valid (10 digits long).
- **Discount Calculation**: Offers a 25% discount for new users with valid OTPs.
- **Returning Users**: If a phone number is recognized, no OTP is required, and no discount is applied.
- **Input Handling**: Manages cases like invalid phone numbers or incorrect OTPs.

## How to Use
1. **Input Total Amount**: Enter the total amount you want to pay.
2. **Enter Phone Number**: Provide a 10-digit phone number.
3. **For New Users**: 
   - If the phone number is new, an OTP will be generated.
   - Input the OTP to receive a 25% discount.
4. **For Returning Users**: 
   - If the phone number is recognized, no OTP is generated, and no discount is given.
5. **Error Handling**:
   - Invalid phone numbers or OTPs will trigger appropriate error messages.

### Example Usage
```bash
WHAT IS YOUR TOTAL AND GET 25% DISCOUNT ON TOTAL BY ENTERING YOUR AMOUNT--- 1000
PHONE NUMBER   9876543210
NEW NUMBER DETECTED
One time password is here 4532
GIVE YOUR OTP--- 4532
THE AMOUNT TO BE PAID AFTER DISCOUNT IS 750.0

Future Enhancements
Add functionality to send OTPs via SMS using an API.
Improve phone number validation with regular expressions.
Store phone numbers in a database instead of a set.
