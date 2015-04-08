# -*-coding:Utf-8 -*

"""Fichier d'installation de notre script programme.py."""

from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "programme",
    version = "0.1",
    description = "Ce programme vous dit bonjour, et vous encourage dans votre cours sur Git & Github",
    executables = [Executable("programme.py")],
)
