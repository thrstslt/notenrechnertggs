import streamlit as st
import math

st.set_page_config(page_title="Endnotenrechner Abschlussprüfungen", layout="centered")

st.title("🎓 Endnoten-Rechner")
st.write("Berechne deine Endnote und schaue, ob sich für dich eine mündliche Prüfung lohnt.")

# Eingabe der Noten
vornote = st.number_input("Vornote (1–6)", min_value=1, max_value=6, step=1)
abschlussnote = st.number_input("Note der Abschlussarbeit (1–6)", min_value=1, max_value=6, step=1)

# Rundungsfunktionen
def rundung_endnote(wert):
    return math.floor(wert + 0.5)

def rundung_abschluss_aus_pruefung(abschluss, pruefung):
    mittelwert = (abschluss + pruefung) / 2
    return math.floor(mittelwert)

# Berechnung der Endnote
def berechne_endnote(vornote, abschlussnote):
    schnitt = (2 * vornote + abschlussnote) / 3
    return rundung_endnote(schnitt)

# Berechnung möglicher Endnoten bei mündlicher Prüfung
def berechne_neue_endnoten(vornote, abschlussnote):
    ergebnisse = {}
    for muendlich in range(1, 7):
        neuer_abschluss = rundung_abschluss_aus_pruefung(abschlussnote, muendlich)
        neue_endnote = berechne_endnote(vornote, neuer_abschluss)
        ergebnisse[muendlich] = neue_endnote
    return ergebnisse

# Berechnung starten
if st.button("Endnote berechnen"):
    endnote = berechne_endnote(vornote, abschlussnote)
    st.subheader(f"📝 Deine Endnote: {endnote}")

    st.subheader("📊 Endnoten bei mündlicher Prüfung")
    tabelle = berechne_neue_endnoten(vornote, abschlussnote)

    # Tabelle ohne Index anzeigen
    daten = [{"Mündliche Note": k, "Endnote": v} for k, v in tabelle.items()]
    st.table(daten)
