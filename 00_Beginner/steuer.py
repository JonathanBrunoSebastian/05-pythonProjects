# Eingaben durch den Anwender
print("Monatliches Bruttogehalt in Euro: ")
z = input()
print("Familienstand (ledig = 1, verheiratet = 2): ")
x = input()

# Eingabe in Zahl umwandel
brutto = int(z)
familie =int(x)

# Steuer berechnen
if brutto > 4000 and familie == 1:
    steuer = 26/100*brutto
elif brutto > 4000 and familie == 2:
    steuer = 22/100*brutto
elif brutto <= 4000 and familie == 1:
    steuer = 22/100*brutto
elif brutto <= 4000 and familie == 2:
    steuer = 18/100*brutto
    
# Nettogehalt berechnen
netto = brutto - steuer

# Steuer ausgeben
print("Ihr Steuerbetrag ergibt sich zu ", steuer, " Euro."
      "Das monatliche Nettogehalt beträgt: ", netto," Euro")
