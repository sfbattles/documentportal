from django.db import models

class DocumentManagement(models.Model):
    policy_no = models.PositiveIntegerField()
    pol_year = models.PositiveSmallIntegerField()
    end_sequence = models.PositiveSmallIntegerField()
    sub_code = models.PositiveSmallIntegerField()
    agent_master_code = models.PositiveIntegerField()
    agent_no = models.PositiveIntegerField()
    line_of_business = models.PositiveIntegerField()
    transaction_type = models.CharField(max_length=50)
    search_name = models.CharField(max_length=50)
    eff_date = models.DateField()
    location_city = models.CharField(max_length=50)
    location_state = models.CharField(max_length=2)
    state_name = models.CharField(max_length=50)
    action_type = models.CharField(max_length=35)
    trans_code = models.PositiveSmallIntegerField()
    document_name = models.CharField(max_length=50)
    run_date = models.DateField(auto_now_add=True)
    policy_exp_date = models.DateField()
    copy_name = models.CharField(max_length=25)

    class Meta:
        verbose_name = "DocumentManagement"
        verbose_name_plural = "DocumentManagements"
        db_table = 'DocumentManagement'

    def __str__(self):
        return str(self.policy_no) + " " + str(self.line_of_business) +  " " +self.document_name