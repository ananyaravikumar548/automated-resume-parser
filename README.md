# Resume Parser

This project is an automated resume parser that extracts relevant information from resumes and stores it in a PostgreSQL database.

## Project Structure

```
resume-parser
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── parser.py
│   ├── database.py
│   └── utils.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd resume-parser
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Ensure that you have a PostgreSQL database set up and update the database connection details in `src/database.py`.

2. Run the application:
   ```
   python src/main.py
   ```

3. Follow the prompts to input the path of the resume file you wish to parse.

## Functionality

- **Resume Parsing**: The application reads resumes in various formats and extracts key information such as:
  - Name
  - Email
  - Phone number
  - Skills
  - Education

- **Database Storage**: Parsed data is stored in a PostgreSQL database for easy retrieval and management.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.