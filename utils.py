def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def validate_email(email):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def format_skills(skills):
    return ', '.join(skill.strip() for skill in skills if skill.strip())

def format_education(education):
    return ', '.join(edu.strip() for edu in education if edu.strip())