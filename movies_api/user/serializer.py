from user.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers



class RegisterUserSerializer(serializers.ModelSerializer):

	class Meta:
		model=User
		fields=['username','password']
		required_fields=['username','password']

	def validate_password(self, data):
		if len(data) >= 8 and len(data) <= 15:
			data=make_password(data)
		else:
			raise serializers.ValidationError('new password must be between 8 to 15 characters long')
		return data





