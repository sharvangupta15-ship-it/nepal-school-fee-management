def validate_student_record(student_record):
    """
    Validates the student record dictionary.
    Requires the following keys:
    - 'name': str, the name of the student
    - 'age': int, the age of the student
    - 'class': str, the class of the student
    - 'roll_number': int, the roll number of the student
    """
    if not isinstance(student_record, dict):
        return False, "The student record must be a dictionary."
    
    required_keys = ['name', 'age', 'class', 'roll_number']
    for key in required_keys:
        if key not in student_record:
            return False, f"Missing key: {key}"
    
    if not isinstance(student_record['name'], str):
        return False, "Name must be a string."
    if not isinstance(student_record['age'], int) or student_record['age'] <= 0:
        return False, "Age must be a positive integer."
    if not isinstance(student_record['class'], str):
        return False, "Class must be a string."
    if not isinstance(student_record['roll_number'], int) or student_record['roll_number'] <= 0:
        return False, "Roll number must be a positive integer."
    
    return True, "Validation successful!"


def validate_fee_record(fee_record):
    """
    Validates the fee record dictionary.
    Requires the following keys:
    - 'student_roll_number': int, roll number of the student
    - 'amount': float, amount of fee
    - 'due_date': str, date due in 'YYYY-MM-DD' format
    """
    if not isinstance(fee_record, dict):
        return False, "The fee record must be a dictionary."
    
    required_keys = ['student_roll_number', 'amount', 'due_date']
    for key in required_keys:
        if key not in fee_record:
            return False, f"Missing key: {key}"
    
    if not isinstance(fee_record['student_roll_number'], int) or fee_record['student_roll_number'] <= 0:
        return False, "Student roll number must be a positive integer."
    if not isinstance(fee_record['amount'], (int, float)) or fee_record['amount'] < 0:
        return False, "Amount must be a non-negative number."
    
    from datetime import datetime
    try:
        datetime.strptime(fee_record['due_date'], '%Y-%m-%d')
    except ValueError:
        return False, "Due date must be in 'YYYY-MM-DD' format."
    
    return True, "Validation successful!"