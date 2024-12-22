# Python URL Shortener

A lightweight URL Shortener API built with Flask and pyshorteners. This project allows you to shorten long URLs into concise and shareable links.

---

## Features

- Simple POST API to shorten URLs.
- Returns both the original and shortened URLs.
- Ideal for social media, emails, and quick sharing.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rghvgrv/python-url-shortner.git
   cd python-url-shortner
   ```

2. **Create a virtual environment (optional):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install Flask pyshorteners
   ```

---

## Usage

1. **Run the application:**
   ```bash
   python app.py
   ```

2. **Access the API Endpoint:**
   - **URL:** `http://127.0.0.1:5000/api/shorten`
   - **Method:** `POST`
   - **Request Body (JSON):**
     ```json
     {
         "url": "https://example.com"
     }
     ```

3. **Example Response (JSON):**
   ```json
   {
       "original_url": "https://example.com",
       "short_url": "https://tinyurl.com/xyz123"
   }
   ```

---

## Example Usage with cURL

### Request:
```bash
curl -X POST http://127.0.0.1:5000/api/shorten \
-H "Content-Type: application/json" \
-d '{"url": "https://example.com"}'
```

### Response:
```json
{
    "original_url": "https://example.com",
    "short_url": "https://tinyurl.com/xyz123"
}
```

---

## Requirements

- Python 3.7+
- Flask
- pyshorteners

---

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.

