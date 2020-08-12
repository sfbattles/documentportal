from django.core.management.base import BaseCommand
from documents.models import DocumentManagement
import csv, os

class Command(BaseCommand):
    help = 'This will update the document portal with current data'
    
    def handle(self, *args, **kwargs):
        file_dir = '/Users/richl/dev/source/django_rest_api/document_management_api/document_management_project/documents/management/commands/'
        file_name = 'policy_management.csv'
        file_loc = f"{file_dir}{file_name}"
        print (file_loc)
        with open(file_loc, "r") as csvfile:
            reader = csv.DictReader(csvfile, delimiter="|")
            for row in reader:
                print(row['policy_no'],row['line_of_business'])
                p = DocumentManagement(policy_no=row['policy_no'],
                pol_year=row['pol_year'],
                end_sequence=row['end_sequence'],
                sub_code=row['sub_code'],
                agent_master_code=row['agent_master_code'],
                agent_no=row['agent_no'],
                line_of_business=row['line_of_business'],
                transaction_type=row['transaction_type'],
                search_name=row['search_name'],
                eff_date=row['eff_date'],
                location_city=row['location_city'],
                location_state=row['location_state'],
                state_name=row['state_name'],
                action_type=row['action_type'],
                trans_code=row['trans_code'],
                document_name=row['document_name'],
                run_date=row['run_date'],
                policy_exp_date=row['policy_exp_date'],
                copy_name=row['copy_name'])
                p.save()                