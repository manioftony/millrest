from django.db import models


class Org(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Info(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    name1 = models.CharField(max_length=100, blank=True, null=True)
    name2 = models.CharField(max_length=100, blank=True, null=True)
    name3 = models.CharField(max_length=100, blank=True, null=True)
    name4 = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.name


ACTIVE = ((0, 'Inactive'), (2, 'Active'),)


class Base(models.Model):

    """ Basic Fields """

    active = models.PositiveIntegerField(choices=ACTIVE, default=2)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def switch(self):
        self.active = {0: 2, 2: 0}[self.active]
        self.save()
        return self.active

    class Meta:
        abstract = True


class Profile(Base):

    ACTIVE_CHOICES = ((0, 'Male'), (2, 'Female'),)

    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.PositiveIntegerField(
        choices=ACTIVE_CHOICES, blank=True, null=True)
    blood_group = models.CharField(max_length=100, blank=True, null=True)
    current_address = models.CharField(max_length=100, blank=True, null=True)
    permanet_address = models.CharField(max_length=100, blank=True, null=True)
    joining_date = models.DateField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(max_length=100, blank=True, null=True)
    mobile_number = models.IntegerField(blank=True, null=True, unique=True)
    landline_number = models.IntegerField(blank=True, null=True)
    voter_id = models.CharField(
        max_length=100, blank=True, null=True, unique=True)
    driving_license = models.CharField(
        max_length=100, blank=True, null=True, unique=True)
    aadhar_card = models.CharField(
        max_length=100, blank=True, null=True, unique=True)

    # def __unicode__(self):
    #     return self.first_name


class EmployeeInfo(Base):
    employee_id = models.CharField(
        max_length=100, blank=True, null=True, unique=True)
    working_shift = models.CharField(max_length=100, blank=True, null=True)
    login_time = models.TimeField(blank=True, null=True)
    logout_time = models.TimeField(blank=True, null=True)
    employee_role = models.CharField(max_length=100, blank=True, null=True)
    under_supervision = models.CharField(max_length=100, blank=True, null=True)
    break_time = models.TimeField(blank=True, null=True)
    over_time = models.TimeField(blank=True, null=True)

    def __unicode__(self):
        return self.employee_id
