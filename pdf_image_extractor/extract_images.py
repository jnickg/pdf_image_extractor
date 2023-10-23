#!/usr/bin/env python3
import fitz
import io
import os
from PIL import Image
from argparse import ArgumentParser


def extract_images(fname: str, out_name: str) -> int:
    """Extract images from a PDF file.

    Parameters
    ----------
    fname : str
        Path to the PDF file.
    out_name : str
        Path to the output directory.

    Returns
    -------
    None
    """

    print(f'Extracting images from {fname} to {out_name}...')
    os.makedirs(out_name, exist_ok=True)
    pdf = fitz.open(fname)

    total_images = 0
    for i in range(len(pdf)):
        page = pdf[i]
        image_list = page.get_images()
        if not image_list:
            continue
        for ii, img in enumerate(image_list, start=1):
            xref = img[0]
            base_image = pdf.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            with open(f'{out_name}/image_{i}_{ii}.{image_ext}', 'wb') as f:
                    f.write(image_bytes)
            total_images += 1
    return total_images

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file', help='PDF file name')
    parser.add_argument('-o', '--out', help='Output directory')
    args = parser.parse_args()

    fname = args.file
    if args.out:
        out_name = args.out
    else:
        out_name = f'{fname}_images'
    total_extracted = extract_images(fname, out_name)
    print(f'Extracted {total_extracted} images from {fname} to {out_name}.')
    print('Done!')
