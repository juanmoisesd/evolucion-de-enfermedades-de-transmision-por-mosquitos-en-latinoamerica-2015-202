from setuptools import setup, find_packages
setup(
    name="evolucion-de-enfermedades-de-transmision-por-mosquitos-en-latinoamerica-2015-202",
    version="1.0.0",
    description="evolucion de enfermedades de transmision por mosquitos en latinoamerica 2015 202",
    author="de la Serna, Juan Moisés",
    url="https://github.com/juanmoisesd/evolucion-de-enfermedades-de-transmision-por-mosquitos-en-latinoamerica-2015-202",
    packages=find_packages(),
    install_requires=["pandas>=1.3.0","requests>=2.26.0"],
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Topic :: Scientific/Engineering"],
    keywords="age-structure, cc0, citation, dataset, demographic-transition, demography, epidemiology, fair-data, global-health, infectious-diseases, juan-moises-de-la-serna, latin-america, open-data, open-science, orcid, population-data, public-health, research, vector-borne-diseases, zenodo, zenodo, open-data",
)