# FlyCheap

## Overview
The FlyCheap project automates the process of finding affordable flights based on user-defined budgets and destinations. It utilizes various APIs to fetch flight data, manages data from Google Sheets, and sends notifications via Twilio. Additionally, it includes functionality to send email notifications to users using smtplib and supports console sign-in for user authentication.

The project consists of several modules:
- **Data Manager**: Handles data retrieval from Google Sheets using Sheety API. It fetches city names, IATA codes, and expected prices from the Google Sheet.
- **Flight Search**: Communicates with the Flight Search API to find flights from a specified origin to destination within a given price range.
- **Notification Manager**: Sends notifications via Twilio and email, delivering flight details to the specified recipient number and email address.
- **Main Program**: Orchestrates the workflow by taking user inputs, initiating flight searches, and triggering notifications. It also supports user authentication through a console sign-in process.

## Files
1. `main.py`: The main file where the program execution starts. It prompts the user to input the departure IATA code and maximum flight price, searches for flights within the budget, and sends notifications about available flights via Twilio and email.
2. `data_manager.py`: Manages data from Google Sheets using Sheety API. It retrieves city names, IATA codes, and expected prices from the Google Sheet.
3. `flight_search.py`: Handles fetching flight data from the Flight Search API. It searches for flights from a specified origin to destination within a given price range.
4. `notification_manager.py`: Responsible for sending notifications via Twilio and email. It sends a text message containing flight details to the specified recipient number and also sends an email with flight details to the specified email address.

## Installation
1. Clone the repository from GitHub: `git clone https://github.com/your/repository.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables:
   - `TWILIO_ACCOUNT_SID`: Twilio account SID
   - `TWILIO_AUTH_TOKEN`: Twilio authentication token
   - `TWILIO_PHONE_NUMBER`: Twilio phone number for sending text messages
   - `SMTP_EMAIL`: Your SMTP email address for sending emails
   - `SMTP_PASSWORD`: Your SMTP email password
   - `[YOUR SSID]`: Your Twilio SID (replace `[YOUR SSID]` with your actual SID)
   - `[AUTH_TOKEN]`: Your Twilio authentication token (replace `[AUTH_TOKEN]` with your actual token)
4. Run the application: `python main.py`

## Usage
1. Enter the IATA code of the departure city when prompted.
2. Enter the maximum price you are willing to pay for the flight.
3. Receive a text message via Twilio and an email with details of available flights within your budget.

## Contributors
- Mohammed Sadiq Ali (https://github.com/S4DIQ84)
- Contact: info@sad-iq.tech

## License
This project is licensed under the MIT License.
