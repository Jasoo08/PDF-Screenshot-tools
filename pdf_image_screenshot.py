#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
screenshot_pdf_pages.py

功能：
  將指定 PDF 的每一頁轉成高解析度影像（PNG），
  並存到使用者桌面上的 "<PDF 檔名> images" 資料夾。

用法：
    pip install PyMuPDF
    python screenshot_pdf_pages.py /path/to/your/file.pdf [dpi]

  可選參數：
    dpi — 影像解析度，預設 150
"""

import os
import sys
import fitz  # PyMuPDF

def list_pdfs_in_directory(directory):
    """列出指定資料夾中的所有 PDF 檔案，並返回檔案清單"""
    pdf_files = [f for f in os.listdir(directory) if f.lower().endswith('.pdf')]
    return pdf_files

def screenshot_pages(pdf_path, dpi=150):
    """將 PDF 的每一頁轉成影像並存檔"""
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    output_dir = os.path.join(f"{pdf_name} images")
    os.makedirs(output_dir, exist_ok=True)

    doc = fitz.open(pdf_path)
    page_count = doc.page_count

    for i in range(page_count):
        page = doc[i]
        pix = page.get_pixmap(dpi=dpi, alpha=False)
        filename = f"page{(i+1):03d}.png"
        out_path = os.path.join(output_dir, filename)
        pix.save(out_path)
        print(f"Saved {out_path}")

    doc.close()
    print(f"\n完成！已將 {page_count} 頁存成影像，存放於:\n{output_dir}")

if __name__ == "__main__":
    # desktop = os.path.join(os.path.expanduser("~"))
    pdf_database_dir = os.path.join( "PDF_Database")

    if not os.path.isdir(pdf_database_dir):
        print(f"錯誤：找不到資料夾 {pdf_database_dir}")
        sys.exit(1)

    pdf_files = list_pdfs_in_directory(pdf_database_dir)
    if not pdf_files:
        print(f"錯誤：資料夾 {pdf_database_dir} 中沒有 PDF 檔案")
        sys.exit(1)

    print("請選擇要擷取的 PDF 檔案：")
    for idx, pdf in enumerate(pdf_files, start=1):
        print(f"{idx}. {pdf}")

    try:
        choice = int(input("輸入編號：")) - 1
        if choice < 0 or choice >= len(pdf_files):
            raise ValueError
    except ValueError:
        print("錯誤：無效的編號")
        sys.exit(1)

    selected_pdf = pdf_files[choice]
    pdf_path = os.path.join(pdf_database_dir, selected_pdf)

    dpi_value = input("請輸入解析度 (預設 150 dpi)：")
    dpi_value = int(dpi_value) if dpi_value.isdigit() else 150

    screenshot_pages(pdf_path, dpi=dpi_value)
