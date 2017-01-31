import csv

from django.core.management.base import BaseCommand, CommandError
from hmda.models import Institution, LoanApplicationRecord


def convert(thing, converter):

    try:
        result = converter(thing)
    except ValueError as ex:
        result = None

    return result


class Command(BaseCommand):

    help = 'Imports institution data from a specified CSV file'

    def add_arguments(self, parser):

        parser.add_argument('data_file', nargs='?', type=str)

    def handle(self, *args, **options):

        with open(options['data_file'], 'r') as f:
            reader = csv.reader(f)
            data = [row for row in reader]

        #for i, name in enumerate(data[0]):
        #    print 'new_institution.{} = row[{}]'.format(name, i)

        for row in data[1:]:

            new_institution = Institution()

            new_institution.activity_year = int(row[0])
            new_institution.respondent_id = row[1]
            new_institution.agency_code = row[2]
            new_institution.agency_abbr = row[3]
            new_institution.agency_name = row[4]
            new_institution.federal_tax_id = row[5]
            new_institution.respondent_name = row[6]
            new_institution.respondent_address = row[7]
            new_institution.respondent_city = row[8]
            new_institution.respondent_state = row[9]
            new_institution.respondent_zip_code = row[10]
            new_institution.parent_name = row[11]
            new_institution.parent_address = row[12]
            new_institution.parent_city = row[13]
            new_institution.parent_state = row[14]
            new_institution.parent_zip_code = row[15]
            new_institution.respondent_name_panel = row[16]
            new_institution.respondent_city_panel = row[17]
            new_institution.respondent_state_panel = row[18]
            new_institution.other_lender_code = row[19]
            new_institution.region_code = row[20]
            new_institution.validity_error = row[21]
            new_institution.assets = row[22]
            new_institution.lar_count = row[23]

            new_institution.save()