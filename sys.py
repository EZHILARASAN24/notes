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
        "1.INTRODUCTION TO DRONE TECHNOLOGY",
        "   - Drone Concept."
        "   - Vocabulary Terminology."
        "   - History of drone."
        "   - Types of current generation of drones based on their method of propulsion.",
        "   - Drone technology impact on the businessesDrone business through entrepreneurship."
        "   - Opportunities/applications for entrepreneurship and employability.",
        "",
        "2. DRONE DESIGN, FABRICATION AND PROGRAMMING",
        "   -Classifications of the UAV."
        "   -Overview of the main drone parts."
        "   - Technical characteristics of the parts."
        "   -Function of the component parts."
        "   -Assembling a drone."
        "   - The energy sources."
        "   - Level of autonomy."
        "   - Drones configurations."
        "   -The methods of programming drone."
        "   - Download program."
        "   -Install program on computer."
        "   - Running Programs." 
        "   -Multi rotor stabilization."
        "   - Flight modes -Wi-Ficonnection",
        "",
        "3.DRONE FLYING AND OPERATION",
        "   -Concept of operation for drone."
        "   -Flight modes."
        "   - Operate a small drone in a controlled environment."
        "   - Drone controls Flight operations."
        "   –management tool."
        "   –Sensors-Onboard storage capacity."
        "   -Removable storage devices."
        "   - Linked mobile devices and applications",
        "",
        "4.DRONE COMMERCIAL APPLICATIONS",
        "   -Choosing a drone based on the application."
        "   -Drones in the insurance sector."
        "   - Drones in delivering mail, parcels and other cargo."
        "   - Drones in agriculture."
        "   - Drones in inspection of transmission lines and power distribution."
        "   -Drones in filming and panoramic picturing",
        "",
        "5.FUTURE DRONES AND SAFETY",
        "   - The safety risks."
        "   - Guidelines to fly safely."
        "   -Specific aviation regulation and standardizationDrone license."
        "   - Miniaturization of drones."
        "   - Increasing autonomy of drones."
        "   -The use of drones in swarms.",
        "",
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
