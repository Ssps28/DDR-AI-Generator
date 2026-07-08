import fitz
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)


def extract_text(pdf_path):
    """
    Extract all text from a PDF.

    Args:
        pdf_path (str): Path to PDF

    Returns:
        dict
    """

    try:

        document = fitz.open(pdf_path)

        total_pages = len(document)

        logging.info(f"Opened PDF: {pdf_path}")

        full_text = ""

        for page_number in range(total_pages):

            page = document.load_page(page_number)

            full_text += f"\n\n========== PAGE {page_number+1} ==========\n"

            full_text += page.get_text("text")

        document.close()

        logging.info(f"Successfully extracted {total_pages} pages.")

        return {
            "total_pages": total_pages,
            "text": full_text
        }

    except Exception as e:

        logging.error(f"Error reading PDF: {e}")

        raise