import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg

def create_pdf(filename, syllabus_content):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 50, "Python Programming Syllabus")
    
    # Subtitle
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 80, "A Comprehensive Guide to Python Programming")
    
    # Content
    text_object = c.beginText(100, height - 120)
    text_object.setFont("Helvetica", 10)
    text_object.setTextOrigin(100, height - 120)
    
    # Add syllabus content line by line
    for line in syllabus_content:
        text_object.textLine(line)
    
    # Write content to PDF
    c.drawText(text_object)
    
    # Save PDF
    c.save()

def generate_diagram():
    # Create a simple diagram using matplotlib
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
    ax.set_title('Sample Plot: Python Programming')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')

    # Save the plot as an image
    diagram_filename = "python_diagram.png"
    fig.savefig(diagram_filename, bbox_inches='tight')

    # Return the filename of the diagram
    return diagram_filename

def create_syllabus_content():
    # Define the syllabus content
    syllabus = [
        "1. Introduction to Python",
        "   - Python is a high-level programming language.",
        "   - Learn syntax, data types, variables, and basic operations.",
        "",
        "2. Control Flow: Conditionals and Loops",
        "   - Use 'if', 'else', and 'elif' for decision-making.",
        "   - Learn loops: 'for', 'while'.",
        "",
        "3. Functions and Modules",
        "   - Define functions with 'def'.",
        "   - Learn about modules and importing libraries.",
        "",
        "4. Object-Oriented Programming (OOP)",
        "   - Understand the concepts of classes and objects.",
        "   - Learn about inheritance, polymorphism, and encapsulation.",
        "",
        "5. Data Structures",
        "   - Work with lists, dictionaries, sets, and tuples.",
        "   - Learn about advanced data structures like stacks and queues.",
        "",
        "6. Error Handling and Debugging",
        "   - Learn about exceptions and try-except blocks.",
        "   - Understand debugging techniques in Python.",
        "",
        "7. Working with Files and Databases",
        "   - Reading and writing to files.",
        "   - Basics of working with databases using SQLite.",
        "",
        "8. Libraries and Frameworks",
        "   - Explore popular Python libraries like numpy, pandas, matplotlib.",
        "   - Introduction to web frameworks like Flask or Django.",
        "",
        "9. Final Project",
        "   - Build a real-world application using Python.",
        "   - Apply all the concepts learned in the course."
    ]
    return syllabus

def main():
    # Generate syllabus content
    syllabus_content = create_syllabus_content()

    # Generate the diagram and save it as a file
    diagram_filename = generate_diagram()

    # Create PDF with the syllabus
    pdf_filename = "python_syllabus.pdf"
    create_pdf(pdf_filename, syllabus_content)

    # Inform the user
    print(f"PDF Syllabus has been created: {pdf_filename}")
    print(f"Diagram has been created: {diagram_filename}")

if __name__ == "__main__":
    main()
