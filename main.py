import sys
from parser import ResumeParser
# from database import insert_into_db  # Comment this out if not needed

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_resume>")
        return

    resume_path = sys.argv[1]
    parser = ResumeParser()
    parsed_data = parser.parse_resume(resume_path)

    if parsed_data:
        # insert_into_db(parsed_data)  # Comment out this line
        print("Parsed Resume Data:")
        print(parsed_data)
    else:
        print("Failed to parse resume.")

if __name__ == "__main__":
    main()