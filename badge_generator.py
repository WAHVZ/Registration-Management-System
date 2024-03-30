from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import win32api

def generate_badge(name, designation, company, name_x, name_y, desig_x, desig_y, comp_x, comp_y):
    filename = name + "_badge.pdf"
    c = canvas.Canvas(filename, pagesize=(4*inch, 5.5*inch))          #Size of the page is set to 4 * 5.5. Change it according to your needs.

    # Set font properties
    c.setFont("Times-Bold", 25)

    # Write text to canvas at specified locations
    c.drawString(name_x, name_y, name)
    c.drawString(desig_x, desig_y, designation)
    c.drawString(comp_x, comp_y, company)

    # Save the PDF
    c.save()

    # Print the generated PDF directly
    win32api.ShellExecute(0, "print", filename, None, ".", 0)

if __name__ == "__main__":
    # Get inputs from user
    # Take inputs as you please
    
    '''name = input("Enter your name (for filename): ")
    designation = input("Enter your designation: ")
    company = input("Enter your company: ")'''
    name = "Wali"
    designation = "Student"
    company = "NED"

    # Manaully set the exact location of entries                               
    # Increasing the x values will move the variable to right hand side and y values to the left. Same goes to y ones.
    
    name_x = 1.25 * inch  # Adjust as needed
    name_y = 3.25 * inch  # Adjust as needed
    desig_x = 1 * inch  # Adjust as needed
    desig_y = 2.5 * inch  # Adjust as needed
    comp_x = 1.25 * inch  # Adjust as needed
    comp_y = 1.75 * inch  # Adjust as needed

    # Generate the badge
    generate_badge(name, designation, company, name_x, name_y, desig_x, desig_y, comp_x, comp_y)

    print("Badge generated successfully and sent to the printer.")
