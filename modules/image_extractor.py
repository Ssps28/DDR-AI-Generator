"""
image_extractor.py

Extracts all embedded images from a PDF.

Author : Sujay S Pattar
Project : AI DDR Generator
"""

import fitz
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)


def extract_images(pdf_path, output_folder, prefix):
    """
    Extract every image from a PDF.

    Args:
        pdf_path : Path of PDF
        output_folder : Folder to save images
        prefix : inspection / thermal

    Returns:
        List containing metadata of extracted images.
    """

    os.makedirs(output_folder, exist_ok=True)

    document = fitz.open(pdf_path)

    seen_xrefs = set()

    extracted_images = []

    image_count = 1

    logging.info(f"Reading images from {pdf_path}")

    for page_number in range(len(document)):

        page = document.load_page(page_number)

        image_list = page.get_images(full=True)

        logging.info(
            f"Page {page_number + 1}: {len(image_list)} images found."
        )

        for image_index, image in enumerate(image_list):

            xref = image[0]

            if xref in seen_xrefs:
                continue

            seen_xrefs.add(xref)

            base_image = document.extract_image(xref)

            image_bytes = base_image["image"]

            image_ext = base_image["ext"]

            filename = (
                f"{prefix}_page_{page_number+1}_img_{image_count}.{image_ext}"
            )

            filepath = os.path.join(output_folder, filename)

            with open(filepath, "wb") as f:
                f.write(image_bytes)

            extracted_images.append(
                {
                    "page": page_number + 1,
                    "filename": filename,
                    "path": filepath
                }
            )

            image_count += 1

    document.close()

    logging.info(
        f"Total images extracted : {len(extracted_images)}"
    )

    return extracted_images