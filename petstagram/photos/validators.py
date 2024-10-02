from django.core.exceptions import ValidationError


def validate_file_less_than_5mb(file_obj):
    filesize = file_obj.file.size
    megabyte_limit = 5
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError(f'Max file size is {megabyte_limit}MB')