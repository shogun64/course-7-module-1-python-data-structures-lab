# This module contains functions to process student data.

def format_student_data(student):
    """
    Format student data for display.
    The function should return a formatted string containing:
    - Student ID
    - Student Name
    - Major
    """
    sid, name, major = student
    return f"ID: {sid} | Name: {name} | Major: {major}"

def display_students(student_list):
    """
    Display all students in a formatted way.
    Loop through the student_list and print each student using format_student_data().
    """
    print("\nStudent Records:")
    for student in student_list:
        print(format_student_data(student))

def student_generator(student_list, major):
    """Generate student records lazily for memory efficiency"""
    return (student for student in student_list if student[2].lower() == major.lower())

def display_student_details(student_db):
    """Display student details from a dictionary"""
    print("\nStudent Details:")
    for sid, details in student_db.items():
        print(f"ID: {sid} | Name: {details['name']} | Major: {details['major']} | Courses: {details['courses']}")

def add_course(student_db, student_id, new_course):
    """Add a new course to a student's course set"""
    if student_id in student_db:
        student_db[student_id]["courses"].add(new_course)
        print(f"\nAdded {new_course} to {student_db[student_id]['name']}'s courses.")
    else:
        print("\nStudent not found.")