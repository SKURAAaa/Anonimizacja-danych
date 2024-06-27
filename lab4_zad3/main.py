import csv
import random
import string


def anonymize_data(input_file, output_file):
    """
    Funkcja do anonimizacji danych w pliku CSV.
    """
    # otworzenie CSV
    with open(input_file, 'r') as input_csv:
        csv_reader = csv.reader(input_csv, delimiter=';')

        with open(output_file, 'w', newline='') as output_csv:
            csv_writer = csv.writer(output_csv, delimiter=';')

            # czesanie CSV
            for row in csv_reader:
                anonymized_row = []
                # czesanie w wierszu
                for item in row:
                    # Anonimizacja tylko dla danych osobowych, pomijając ostatnią kolumnę z liczbami
                    if '@' in item:  # Sprawdzenie czy w elemencie znajduje się '@' (czyli jest to e-mail)
                        email_parts = item.split('@')
                        username = ''.join(
                            random.choices(string.ascii_letters + string.digits, k=random.randint(1, 20)))
                        domain = email_parts[1]  # Zachowaj domenę
                        anonymized_email = f"{username}@{domain}"
                        anonymized_row.append(anonymized_email)
                    else:
                        anonymized_row.append(item)
                # Zapisz zanonimizowany wiersz do pliku wyjściowego
                csv_writer.writerow(anonymized_row)


# zanonimizowanie danych
anonymize_data('departament.csv', 'anonimizowane_dane.csv')
