from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.3.0'
DESCRIPTION = 'Module  For Nguyen Minh Nhat Python'
this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

# Setting up
setup(
    name="nguyenminhnhat",
    version=VERSION,
    author="Nguyễn MIn Nhật (Khương Dừa)",
    author_email="<minhtientiny@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'nguyenminhnhat', 'api', 'nguyenminhnhat api', 'khuongdua', 'requests'],
    classifiers=[
		"Development Status :: 3 - Alpha",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Natural Language :: English",
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: Implementation :: CPython",
		"Programming Language :: Python :: Implementation :: PyPy",
		"Topic :: Communications :: Chat",
		"Topic :: Internet :: WWW/HTTP",
		"Topic :: Internet :: WWW/HTTP :: Dynamic Content",
		"Topic :: Software Development :: Libraries",
		"Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
