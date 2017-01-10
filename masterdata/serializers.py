from rest_framework import serializers
from models import Profile, Org


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Org


field_data = {
    'profile': ('first_name', 'last_name', 'gender', 'blood_group', 'current_address', 'permanet_address', 'joining_date', 'date_of_birth', 'mobile_number', 'landline_number', 'voter_id', 'driving_license', 'aadhar_card',),
    'employeeinfo': ('employee_id', 'working_shift', 'login_time', 'logout_time', 'employee_role', 'under_supervision', 'break_time', 'over_time',)
}


def model_serializer_factory(mdl):

    class ModelSerializer(serializers.ModelSerializer):

        class Meta:
            model = mdl
            try:
                fields = field_data[mdl.__name__.lower()]
            except KeyError:
                pass
            error_messages = {'required': 'Please Type a Password'}

    #
    return ModelSerializer
#
