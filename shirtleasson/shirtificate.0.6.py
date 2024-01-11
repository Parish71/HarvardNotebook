from fpdf import FPDF

class CertificatePDF(FPDF):
    def __init__(self, orientation='P', unit='mm', format='A4'):
        super().__init__(orientation=orientation, unit=unit, format=format)

        # Set default font
        self.set_font("Helvetica", "", 14)

    def set_helvetica_font(self, style, size=10):
        self.set_font("Helvetica", style, size)

    def _print(self, user_name):
        """Print the customized text with the user's name."""
        text = f"{user_name} took the CS50"
        self.cell(0, 10, text, 0, align='C')
        self.ln(10)

    def add_title(self, title):
        """Add the title at the top, centered horizontally."""
        self.set_helvetica_font("B", 16)
        self.cell(0, 10, title, 0, align='C')
        self.ln(10)

    def add_image(self, image_path, width=90):
        """Add an image centered horizontally."""
        x_position = (self.w - width) / 2
        self.image(image_path, x=x_position, y=self.get_y(), w=width)

    def set_white_text_color(self):
        """Set font color to white."""
        self.set_text_color(255, 255, 255)

    def set_black_text_color(self):
        """Set font color to black."""
        self.set_text_color(0, 0, 0)

    def add_certificate_content(self, title, image_path, user_name):
        self.add_page()

        # Add title
        self.add_title(title)

        # Add image
        self.add_image(image_path)

        # Move to the position for the user's name
        self.ln(30)

        # Set font color to white
        self.set_white_text_color()

        # Print user's name
        self._print(user_name)

        # Reset font color to black
        self.set_black_text_color()

    def save_certificate(self, output_filename):
        self.output(output_filename)


def generate_certificate(user_name):
    certificate_pdf = CertificatePDF()

    # Generate the certificate with the user's name
    certificate_pdf.add_certificate_content("CS50 Shirtificate", "shirtificate.png", user_name)
    certificate_pdf.save_certificate("shirtificate.pdf")

if __name__ == "__main__":
    # Get user's name
    user_name = input("Enter your name: ")

    generate_certificate(user_name)
