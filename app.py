import streamlit as st
import math
import pandas as pd  # direkt am Anfang importieren

st.set_page_config(page_title="Endnotenrechner Abschlussprüfungen", layout="centered")

st.title("🎓 Endnoten-Rechner")
st.write("Berechne deine Endnote und schaue, ob sich für dich eine mündliche Prüfung lohnt.")

# Eingabe der Noten
vornote = st.number_input("Vornote (1–6)", min_value=1, max_value=6, step=1)
abschlussnote = st.number_input("Note der Abschlussarbeit (1–6)", min_value=1, max_value=6, step=1)

def rundung_endnote(wert):
    return math.floor(wert + 0.5)

def rundung_abschluss_aus_pruefung(abschluss, pruefung):
    mittelwert = (abschluss + pruefung) / 2
    return math.floor(mittelwert)

def berechne_endnote(vornote, abschlussnote):
    schnitt = (2 * vornote + abschlussnote) / 3
    return rundung_endnote(schnitt)

def berechne_neue_endnoten(vornote, abschlussnote):
    ergebnisse = {}
    for
