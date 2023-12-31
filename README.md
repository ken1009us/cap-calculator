# Capacity Calculator

![image](https://github.com/ken1009us/cap-calculator/blob/main/doc/homepage.png "homepage")

## Overview

Link: [Capacity Calculator](https://ken1009.pythonanywhere.com/)

This Capacity Calculator is a web-based tool dedicated to the employees of Physiq. It is designed to efficiently calculate the available working hours considering various factors like sprint days, daily working hours, meeting hours, and PTO hours. The calculator is built using Flask, a lightweight web application framework in Python.

## Features

- Easy-to-use interface for inputting data related to sprint days, working hours, meeting hours, and PTO hours.
- Instant calculation of available working capacity in hours.
- Responsive design for accessibility across various devices.

## Installation

To set up the Capacity Calculator on your local machine, follow these steps:

### Clone the repository:

```bash
$ git clone https://github.com/ken1009us/cap-calculator
```

### Navigate to the project directory:

```bash
$ cd cap-calculator
```

### Install the required packages (ensure you have Python installed):

```bash
$ pip install -r requirements.txt
```

### Run the application:

```bash
$ python app.py
```

## Usage

After starting the application, navigate to http://localhost:5000 on your web browser. Follow these steps to use the calculator:

- Enter the sprint days in the respective field.
- Input the number of working hours per day.
- Specify the total meeting hours.
- Enter the PTO (Paid Time Off) hours.
- Click the "Calculate" button to see the total available working hours.

## Technologies Used

Frontend: HTML, CSS
Backend: Flask (Python)
Deployment: pythonanywhere

## License

This project is licensed under the MIT License.

## Contact

For any queries or feedback, please contact [Ken Wu](https://www.ken-wu.com/).

