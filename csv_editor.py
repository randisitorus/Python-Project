import csv

with open('survey_results_public.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('clean_survey_data.csv', 'w', newline='') as new_csv:
        fieldnames = ['Respondent', 'LanguageWorkedWith',
                      'LanguageDesireNextYear']

        csv_writer = csv.DictWriter(new_csv, fieldnames=fieldnames)
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow({'Respondent': line['Respondent'], 'LanguageWorkedWith': line['LanguageWorkedWith'],
                                 'LanguageDesireNextYear': line['LanguageDesireNextYear']})
