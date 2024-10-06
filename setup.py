# setup.py

from setuptools import setup, find_packages

setup(
    name="ezy_calculator",                     # Όνομα του πακέτου
    version="0.1",                             # Έκδοση του πακέτου
    author="George",                     # Όνομα του συγγραφέα
    author_email="email@example.com",          # Email του συγγραφέα
    description="Μια απλή βιβλιοθήκη για βασικές αριθμητικές πράξεις.",  # Περιγραφή του πακέτου
    long_description=open("README.md").read(), # Αναλυτική περιγραφή από το αρχείο README
    long_description_content_type="text/markdown", # Τύπος περιεχομένου της αναλυτικής περιγραφής
    url="https://github.com/username/ezy_calculator", # Σύνδεσμος για το αποθετήριο
    packages=find_packages(),                  # Αυτόματη εύρεση πακέτων στο φάκελο
    classifiers=[
        "Programming Language :: Python :: 3", # Υποστηριζόμενη έκδοση Python
        "License :: OSI Approved :: MIT License", # Τύπος άδειας
        "Operating System :: OS Independent",  # Ανεξαρτήτως λειτουργικού συστήματος
    ],
    python_requires='>=3.6',                   # Ελάχιστη έκδοση Python που απαιτείται
)
