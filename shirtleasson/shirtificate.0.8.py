from fpdf import FPDF

class CertificatePDF(FPDF):
    def __init__(self, orientation='P', unit='mm', format='A4'):
        super().__init__(orientation=orientation, unit=unit, format=format)

    def set_helvetica_font(self, style, size):
        self.set_font("Helvetica", style, size)

    def add_certificate_content(self, title, image_path, name):
        self.add_page()

        # Use Helvetica as a substitute for Arial
        self.set_helvetica_font("B", 16)
        self.ln(10)

        # Use new_x and new_y instead of ln
        new_x = int(round(self.w / 2 - self.get_string_width(title) / 2))
        new_y = int(round(self.h / 2))
        self.cell(0, 10, title, 0, align='C', new_x=new_x, new_y=new_y)

        # Add the image centered horizontally
        self.image(image_path, x=60, y=40, w=90)

        # Use Helvetica as a substitute for Arial
        self.set_helvetica_font("", 14)

        # Use new_x and new_y instead of ln
        new_x = int(round(self.w / 2 - self.get_string_width(name) / 2))
        new_y = int(round(self.h / 2)) + 10
        self.cell(0, 10, name, 0, align='C', new_x=new_x, new_y=new_y)

    def save_certificate(self, output_filename):
        self.output(output_filename)


def get_user_name():
    return input("Enter your name: ")


def generate_certificate(user_name):
    certificate_pdf = CertificatePDF()
    certificate_pdf.set_helvetica_font("B", 16)

    # Generate the shirtificate with the user's name
    certificate_pdf.add_certificate_content("CS50 Shirtificate", "shirtificate.png", user_name)
    certificate_pdf.save_certificate("shirtificate.pdf")

if __name__ == "__main__":
    user_name = get_user_name()
    generate_certificate(user_name)
