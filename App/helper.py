import re, os
from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen import canvas

def clean_name(name: str):
    """
    Cleans and standardizes visitor names according to local conventions.
    Returns (cleaned_name, changed) tuple.
    """

    original_name = name.strip()
    name = original_name

    # 1️⃣ Remove unwanted characters and normalize spaces
    name = re.sub(r'[^A-Za-z\s]', ' ', name)
    name = re.sub(r'\s+', ' ', name).strip()

    # 2️⃣ Standardize casing (keep all lowercase temporarily for easier matching)
    name = name.lower()

    # 3️⃣ Common Arabic/Urdu-origin prefix spacing fixes
    name = re.sub(r'\babdul\s*([a-z])', r'abdul \1', name)
    name = re.sub(r'\babdal\s*([a-z])', r'abdul \1', name)
    name = re.sub(r'\bmuhammad\s*([a-z])', r'muhammad \1', name)
    name = re.sub(r'\bmohammad\s*([a-z])', r'mohammad \1', name)
    name = re.sub(r'\bsyed\s*([a-z])', r'syed \1', name)
    name = re.sub(r'\bsheikh\s*([a-z])', r'sheikh \1', name)
    name = re.sub(r'\bmian\s*([a-z])', r'mian \1', name)
    name = re.sub(r'\bchaudhry\s*([a-z])', r'chaudhry \1', name)
    name = re.sub(r'\bghulam\s*([a-z])', r'ghulam \1', name)
    name = re.sub(r'\bgul\s*([a-z])', r'gul \1', name)

    # 4️⃣ Convert Abd Al / Abdal to Abdul
    name = re.sub(r'\babd\s+al\s+', 'abdul ', name)
    name = re.sub(r'\babdal\b', 'abdul ', name)

    # 5️⃣ Common suffix-based spacing fixes (last names)  These are pakistani names. You can edit them and make your own list of names as needed.
    suffixes = [
        "ahmed", "ahmad", "khan", "raza", "malik", "hasan",
        "hussain", "farooq", "arif", "iqbal", "rafiq", "bashir", "aslam",
        "imran", "nasir", "amir", "akbar", "ashraf", "akbar", "siddique", 
        "shah", "bibi", "pasha", "ather"
    ]
    for suf in suffixes:
        name = re.sub(rf'([a-z]){suf}\b', rf'\1 {suf}', name)

    # 5️⃣ Remove hyphens and “Aa…” issues
    name = re.sub(r'-', ' ', name)
    name = re.sub(r'\baa+([a-z]+)', r'A\1', name)

    # 6️⃣ Collapse spaces again
    name = re.sub(r'\s+', ' ', name).strip()

    # 7️⃣ Title case properly
    name = ' '.join(word.capitalize() for word in name.split())

    return name

def truncate_to_last_word(text, max_length):
    if len(text) <= max_length:
        return text
    truncated = text[:max_length]
    last_space = truncated.rfind(' ')
    return truncated[:last_space] if last_space != -1 else truncated

def generate_badge(data):
    folder = "C:/Users/Sukkur RMS User/Desktop/Sukkur_25/Badges" # select your folder name
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, f"{data['name']}_badge.pdf")
    name = truncate_to_last_word(data['name'], 16)
    industry = truncate_to_last_word(data['industry'], 18)
    occupation = truncate_to_last_word(data['occupation'], 18)

    # Create a Canvas with a custom page size (e.g., 8.5 inches wide by 11 inches tall)
    # 8.5 inches * 72 points/inch = 612 points
    # 11 inches * 72 points/inch = 792 points

    c = canvas.Canvas(file_path, pagesize=portrait((4 * 72, 5.5 * 72)))  # adjust page size to your needs
    c.setFont("Times-Bold", 25)
    c.drawString(48, 245, name)
    c.setFont("Times-Roman", 25)
    c.drawString(48, 180, industry)
    c.setFont("Times-Roman", 25)
    c.drawString(48, 124, occupation)
    c.save()