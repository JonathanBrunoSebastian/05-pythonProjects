# Mittelohnberechnung
print("Mittellohnberechnung")

print("Eingabe der Anzahl der Arbeitskräfte")

print("Werker/Maschienenwerker:")
a = input()
Lohngruppe_1 = int(a)

print("Fachwerker/Maschinisten/Kraftfahrer:")
b = input()
Lohngruppe_2 = int(b)

print("Facharbeiter/Baugeräteführer/Berufskraftfahrer:")
c = input()
Lohngruppe_3 = int(c)

print("Spezialfacharbeiter/Baumaschinenführer:")
d = input()
Lohngruppe_4 = int(d)

print("Vorarbeiter/Baumaschinen-Vorarbeiter:")
e = input()
Lohngruppe_5 = int(e)

print("Werkpolier/Baumaschinen-Fachmeister:")
f = input()
Lohngruppe_6 = int(f)

# Datei erstellen
import sys

try:
    q = open("C:/Users/jonat/Documents/Studium/Hauptstudium/BIW 2-06 Bauwirtschaft/Übung/Mittellohnberechnung.txt", "w")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Zeit
import time
lt = time.localtime()
jahr, monat, tag = lt[0:3]
q.write("Zeit: {0:02d}.{1:02d}.{2:4d}\n".
        format(tag, monat, jahr))
stunde, minute, sekunde = lt[3:6]
q.write("      {0:02d}:{1:02d}:{2:02d}\n".
        format(stunde, minute, sekunde))

# Berechnung des Gesamtlohnes
q.write("--------------------------------------------------------------------------------\n")
q.write("Mittellohnberechnung\n\n")
q.write("-> Berechnung des Gesamtlohnes\n\n")
Lohn_1 = Lohngruppe_1 * 11.30
line01 = [str(Lohngruppe_1), " x Lohngruppe 1 = ", str(round(Lohn_1,2)), " Euro/h\n"]
q.writelines(line01)
Lohn_2 = Lohngruppe_2 * 12.81
line02 = [str(Lohngruppe_2), " x Lohngruppe 2 = ", str(round(Lohn_2,2)), " Euro/h\n"]
q.writelines(line02)
Lohn_3 = Lohngruppe_3 * 16.65
line03 = [str(Lohngruppe_3), " x Lohngruppe 3 = ", str(round(Lohn_3,2)), " Euro/h\n"]
q.writelines(line03)
Lohn_4 = Lohngruppe_4 * 18.15
line04 = [str(Lohngruppe_4), " x Lohngruppe 4 = ", str(round(Lohn_4,2)), " Euro/h\n"]
q.writelines(line04)
Lohn_5 = Lohngruppe_5 * 19.09
line05 = [str(Lohngruppe_5), " x Lohngruppe 5 = ", str(round(Lohn_5,2)), " Euro/h\n"]
q.writelines(line05)
Lohn_6 = Lohngruppe_6 * 20.86
line06 = [str(Lohngruppe_6), " x Lohngruppe 6 = ", str(round(Lohn_6,2)), " Euro/h\n"]
q.writelines(line06)
q.write("--------------------------------------------------------------------------------\n")

arbeiter = Lohngruppe_1 + Lohngruppe_2 + Lohngruppe_3 + Lohngruppe_4 + Lohngruppe_5 + Lohngruppe_6
ges_Lohn = Lohn_1 + Lohn_2 + Lohn_3 + Lohn_4 + Lohn_5 + Lohn_6
line07 = [str(arbeiter), " Arbeiter: Lohnsumme = ", str(round(ges_Lohn,2)), " Euro/h\n"]
q.writelines(line07)

ds_TL = ges_Lohn / arbeiter
line08 = ["Durchschnittlicher Tariflohn = ", str(round(ds_TL,2)), " Euro/h\n"]
q.writelines(line08)
q.write("--------------------------------------------------------------------------------\n")

# Berechnung der Zulagen
q.write("-> Berechnung der Zulagen\n\n")

print("Arbeiter mit Leistungszulage: ?")
AK_LZ = input()
ak_lz = int(AK_LZ)
print("Leistungszulage: ? Euro/h")
LZE = input()
lzE = float(LZE)
LZulage = lzE * ak_lz / arbeiter
line09 = ["Arbeiter mit Leistungszulage: ", str(round(ak_lz)), " Arbeiter\n"
          "Leistungszulage: ", str(round(lzE,2)), " Euro/h\n"
          , str(round(lzE,2)), " Euro/h x ", str(round(ak_lz)), " / ", str(round(arbeiter)), "\n"
          "+  Leistungszulage = ", str(round(LZulage,2)), " Euro/h\n\n"]
q.writelines(line09)

print("Arbeiter mit Stammarbeiterzulage: ?")
SAZ = input()
saz = int(SAZ)
print("Stammarbeiterzulage: ? Euro/h")
SAZE = input()
sazE = float(SAZE)
SaZulage = sazE * saz / arbeiter
line10 = ["Arbeiter mit Stammarbeiterzulage: ", str(round(saz)), " Arbeiter\n"
          "Stammarbeiterzulage: ", str(round(sazE,2)), " Euro/h\n"
          , str(round(sazE,2)), " Euro/h x ", str(round(saz)), " / ", str(round(arbeiter)), "\n"
          "+  Stammarbeiterzulage = ", str(round(SaZulage,2)), " Euro/h\n\n"]
q.writelines(line10)

Lohn_Z = ds_TL + LZulage + SaZulage
line11 = ["Lohnsumme + Zulagen = ", str(round(Lohn_Z,2)), " Euro/h\n"]
q.writelines(line11)
q.write("--------------------------------------------------------------------------------\n\n")

# Berechnung der Zuschläge
q.write("+  Überstundenzuschlag\n")
print("Tarifliche Arbeitszeit pro Woche: ? in h/Woche")
TAZ = input()
tar_AZ = float(TAZ)
print("Überstunden pro Woche: ? in h/Woche")
USt = input()
uStunden = float(USt)
wArbeitszeit = tar_AZ + uStunden
line12 = ["Tarifliche Arbeitszeit pro Woche: ", str(round(tar_AZ,1)), " h/Woche\n"
          "Wöchentliche Arbeitszeit: ", str(round(wArbeitszeit,1)), " h/Woche\n"]
q.writelines(line12)

line13 = ["Überstunden pro Woche: ", str(round(uStunden,1)), " h/Woche\n"
          "Zuschlag: "]
q.writelines(line13)

prozent = uStunden * 0.25 / wArbeitszeit * 100
uZuschlag = prozent / 100 * Lohn_Z
line14 = [str(round(uStunden,1)), " h/Woche / ", str(round(wArbeitszeit,1)), " h/Woche x 25% = ", str(round(prozent,2)), "%\n",
          str(round(prozent,2)), " % / 100 % x ", str(round(Lohn_Z,2)), " Euro/h = ", str(round(uZuschlag,2)), " Euro/h\n\n"
          "+  Vermögensbildung für "]
q.writelines(line14)

print("Vermögensbildung für ? in %")
VB = input()
V_Bildung = float(VB)
print("Höhe der Vermögensbildung: ? in Euro/h")
VBE = input()
V_BildungE = float(VBE)
VB_Zuschlag = V_Bildung / 100 * V_BildungE 
line15 = [str(round(V_Bildung,2)), " % der Belegschaft:\n",
          str(round(V_Bildung,2))," % / 100 % x ", str(round(V_BildungE,2)), " Euro/h = ", str(round(VB_Zuschlag,2)), " Euro/h\n\n"]
q.writelines(line15)

# Mittellohn A
Mittellohn_A = Lohn_Z + uZuschlag + VB_Zuschlag
line16 = ["Mittellohn A = ", str(round(Mittellohn_A,2)), " Euro/h\n"]
q.writelines(line16)
q.write("--------------------------------------------------------------------------------\n\n")

# Mittellohn AS
print("Sozialkosten: ? in %")
SK = input()
SozialP = float(SK)
Sozialkosten = SozialP / 100 * Mittellohn_A          
Mittellohn_AS = Mittellohn_A + Sozialkosten
line17 = ["+  Sozialkosten = ", str(round(SozialP,2)), " % / 100 % x ", str(round(Mittellohn_A,2)), " Euro/h = ", str(round(Sozialkosten,2)), " Euro/h\n"
          "Mittellohn AS = ", str(round(Mittellohn_AS,2)), " Euro/h\n"]
q.writelines(line17)
q.write("--------------------------------------------------------------------------------\n\n")

# Mittellohn ASL
print("Lohnnebenkosten: ? in %")
LK = input()
LohnnP = float(LK)
Lohnnebenkosten = LohnnP / 100 * Mittellohn_AS 
Mittellohn_ASL = Mittellohn_AS + Lohnnebenkosten
line18 = ["+  Lohnnebenkosten = ", str(round(LohnnP,2)), " % / 100 % x ", str(round(Mittellohn_AS,2)), " Euro/h = ", str(round(Lohnnebenkosten,2)), " Euro/h\n"
          "Mittellohn ASL = ", str(round(Mittellohn_ASL,2)), " Euro/h\n"]
q.writelines(line18)
q.write("--------------------------------------------------------------------------------\n\n")

q.close()
