# Funktion zum Trennen der Namen und Erstellen einer Liste
def split_names(input_string):
    # Trennen der Eingabe anhand von Kommas
    names = [name.strip() for name in input_string.split(',')]
    
    return names

# Beispiel-Eingabe
input_string = "Max Mustermann, Erika Musterfrau, John Doe, Jane Doe"

# Aufrufen der Funktion
names_list = split_names(input_string)

