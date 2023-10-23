from setuptools import setup, find_packages

setup(
       # the name must match the folder name 'verysimplemodule'
        name="pdf_image_extractor", 
        version='1.0.0',
        author="jnickg",
        author_email="me@jnickg.net",
        description='PDF Image Extractor',
        long_description='A very simple executable Python package to extract images from a PDF file.',
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'PDF', 'image', 'extraction'],
)