import csv

from django.core.management.base import BaseCommand, CommandError
from hmda.models import LoanApplicationRecord


def convert(thing, converter):

    try:
        result = converter(thing)
    except ValueError as ex:
        result = None

    return result


class Command(BaseCommand):

    help = 'Imports LAR data from a specified CSV file'

    def add_arguments(self, parser):

        parser.add_argument('data_file', nargs='?', type=str)

    def handle(self, *args, **options):

        with open(options['data_file'], 'r') as f:
            reader = csv.reader(f)
            data = [row for row in reader]

        #for i, name in enumerate(data[0]):
        #    print i, name

        for row in data[1:100]:
            try:
                # print row
                new_record = LoanApplicationRecord()
                new_record.tract_to_msamd_income = convert(row[0], float)
                new_record.rate_spread = convert(row[1], float)
                new_record.population = convert(row[2], int)
                new_record.minority_population = convert(row[3], int)
                new_record.number_of_owner_occupied_units = convert(row[4], int)
                new_record.number_of_1_to_4_family_units = convert(row[5], int)
                new_record.loan_amount_000s = convert(row[6], int)
                new_record.hud_median_family_income = convert(row[7], int)
                new_record.applicant_income_000s = convert(row[8], int)
                new_record.state_name = row[9]
                new_record.state_abbr = row[10]
                new_record.sequence_number = convert(row[11], int)
                new_record.respondent_id = row[12]
                new_record.purchaser_type_name = row[13]
                new_record.property_type_name = row[14]
                new_record.preapproval_name = row[15]
                new_record.owner_occupancy_name = row[16]
                new_record.msamd_name = row[17]
                new_record.loan_type_name = row[18]
                new_record.loan_purpose_name = row[19]
                new_record.lien_status_name = row[20]
                new_record.hoepa_status_name = row[21]
                new_record.edit_status_name = row[22]
                new_record.denial_reason_name_3 = row[23]
                new_record.denial_reason_name_2 = row[24]
                new_record.denial_reason_name_1 = row[25]
                new_record.county_name = row[26]
                new_record.co_applicant_sex_name = row[27]
                new_record.co_applicant_race_name_5 = row[28]
                new_record.co_applicant_race_name_4 = row[29]
                new_record.co_applicant_race_name_3 = row[30]
                new_record.co_applicant_race_name_2 = row[31]
                new_record.co_applicant_race_name_1 = row[32]
                new_record.co_applicant_ethnicity_name = row[33]
                new_record.census_tract_number = row[34]
                new_record.as_of_year = convert(row[35], int)
                new_record.application_date_indicator = convert(row[36], int)
                new_record.applicant_sex_name = row[37]
                new_record.applicant_race_name_5 = row[38]
                new_record.applicant_race_name_4 = row[39]
                new_record.applicant_race_name_3 = row[40]
                new_record.applicant_race_name_2 = row[41]
                new_record.applicant_race_name_1 = row[42]
                new_record.applicant_ethnicity_name = row[43]
                new_record.agency_name = row[44]
                new_record.agency_abbr = row[45]
                new_record.action_taken_name = row[46]

                new_record.save()
            except Exception as ex:
                print ex
                print row
                raise ex
