# Divera iCalendar API Integration

Welcome! This application allows you to import the calendar from the Divera app as a `.ics` file, making it easy to integrate Divera events with your calendar applications.

## 📍 Current Route for Calendar Integration

You can access the Divera calendar as an `.ics` file at:
```
http://SERVERIP:1312/DiveraCalendar.ics
```

## 🚀 Getting Started

Follow these steps to set up and run the application on your local machine.

### Prerequisites

- **Python 3.x** installed
- **Pip** package manager for Python

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/divera-icalendar-api.git
   cd divera-icalendar-api
   ```

2. **Install Requirements**
   Install the required dependencies with:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Setup**
   Create a `.env` file in the project root and add your Divera access key:
   ```
   DIVERA_ACCESS_KEY=your_actual_access_key_here
   ```
   > **Note**: For an example of the `.env` file, see this blurred sample image: [`.env` Blurred Image](https://i.imgur.com/nDsjWqn.png)

### Running the Application

To start the Flask server, run:
```bash
python main.py
```

## 🤝 Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.
