"""
workflow.py

Main workflow for the AI DDR Generator.

Author: Sujay S Pattar
"""

import os
import json
import logging

from modules.pdf_reader import extract_text
from modules.image_extractor import extract_images
from modules.llm import extract_document, merge_documents
from modules.report_generator import DDRReportGenerator


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)


class DDRWorkflow:

    def __init__(self):

        self.inspection_pdf = "input/inspection_report.pdf"
        self.thermal_pdf = "input/thermal_report.pdf"

        self.output_folder = "output"
        self.image_folder = "extracted_images"

        os.makedirs(self.output_folder, exist_ok=True)

    def save_json(self, filename, data):
        """
        Save JSON output to the output folder.
        """

        path = os.path.join(self.output_folder, filename)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        logging.info(f"Saved {filename}")

    def run(self):

        logging.info("=" * 60)
        logging.info("DDR AI WORKFLOW STARTED")
        logging.info("=" * 60)

        # -------------------------------------------------
        # STEP 1 : READ PDFs
        # -------------------------------------------------

        logging.info("Reading Inspection Report...")

        inspection = extract_text(
            self.inspection_pdf
        )

        logging.info("Reading Thermal Report...")

        thermal = extract_text(
            self.thermal_pdf
        )

        # -------------------------------------------------
        # STEP 2 : EXTRACT IMAGES
        # -------------------------------------------------

        logging.info("Extracting inspection images...")

        extract_images(
            self.inspection_pdf,
            self.image_folder,
            "inspection"
        )

        # Thermal image extraction skipped
        # (Avoids duplicate embedded assets)

        logging.info("Thermal image extraction skipped.")

        # -------------------------------------------------
        # STEP 3 : AI EXTRACTION
        # -------------------------------------------------

        logging.info("Generating Inspection JSON...")

        inspection_json = extract_document(
            inspection["text"],
            "Inspection Report"
        )

        logging.info("Generating Thermal JSON...")

        thermal_json = extract_document(
            thermal["text"],
            "Thermal Report"
        )

        # -------------------------------------------------
        # STEP 4 : SAVE INTERMEDIATE JSONS
        # -------------------------------------------------

        self.save_json(
            "inspection.json",
            inspection_json
        )

        self.save_json(
            "thermal.json",
            thermal_json
        )

        # -------------------------------------------------
        # STEP 5 : MERGE
        # -------------------------------------------------

        logging.info("Generating Final DDR JSON...")

        final_ddr = merge_documents(
            inspection_json,
            thermal_json
        )

        self.save_json(
            "final_ddr.json",
            final_ddr
        )

        # -------------------------------------------------
        # STEP 6 : GENERATE REPORT
        # -------------------------------------------------

        logging.info("Generating Word Report...")

        generator = DDRReportGenerator(
            output_path=os.path.join(
                self.output_folder,
                "DDR_Report.docx"
            )
        )

        generator.generate(final_ddr)

        logging.info("=" * 60)
        logging.info("DDR REPORT GENERATED SUCCESSFULLY")
        logging.info("=" * 60)

        return final_ddr