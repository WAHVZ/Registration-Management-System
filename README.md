# Badge Generator

Assalam o Alaikum.

This Python script generates a badge (ID card) in PDF format for attendees at an event or expo. The generated badge includes the attendee's name, designation, and company details.

## Usage

1. Ensure you have Python installed on your system.
2. Install the required libraries using pip:
   pip install reportlab

If you're using Windows and want to print directly from the script, install `pywin32` as well:
   pip install pywin32

3. Clone this repository or download the `badge_generator.py` file.
4. Run the script:
   python badge_generator.py

Follow the prompts to enter attendee details (name, designation, and company).
5. The script will generate a PDF file named `Name_badge.pdf` with the attendee's information and print it.

## Note

- The badge layout is set to a default size of 4" (width) by 5.5" (length). You can adjust the layout and font sizes in the script as needed.
- If you encounter any issues with printing, ensure that your default printer is properly configured.
