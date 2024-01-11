from fpdf import FPDF


class ImagePDF(FPDF):
    def __init__(self, orientation='P', unit='mm', format='A4'):
        super().__init__(orientation=orientation, unit=unit, format=format)
        self.image_cache = None

    def use_shared_image_cache(self, image_cache):
        self.image_cache = image_cache

    def side_by_side_images(self, image_path1, image_path2):
        self.add_page()
        half_page_width = self.epw / 2

        # Full page height, half page width (left side)
        self.image(image_path1, h=self.eph, w=half_page_width)

        # Move to the right half of the page
        self.set_x(half_page_width)

        # Full page height, half page width (right side)
        self.image(image_path2, h=self.eph, w=half_page_width)

    def generate_pdf(self, output_filename):
        self.output(output_filename)


def main():
    # Example 1: Side-by-side images
    pdf1 = ImagePDF(orientation='landscape')
    pdf1.side_by_side_images("imgA.png", "imgB.jpg")
    pdf1.generate_pdf("side_by_side_images.pdf")

    # Example 2: Image blending
    pdf2 = ImagePDF()
    pdf2.add_page()
    pdf2.image("imgA.png", x=10, y=10)
    with pdf2.local_context(blend_mode="ColorBurn"):
        pdf2.image("imgB.jpg", x=50, y=50)
    pdf2.generate_pdf("blended_images.pdf")

    # Example 3: Sharing image cache
    image_cache = None
    for i in range(3):
        pdf3 = ImagePDF()
        pdf3.add_page()
        if image_cache is None:
            image_cache = pdf3.image_cache
        else:
            pdf3.use_shared_image_cache(image_cache)
        pdf3.side_by_side_images("imgA.png", "imgB.jpg")
        pdf3.generate_pdf(f"shared_image_cache_{i}.pdf")


if __name__ == "__main__":
    main()
