

# def valid_url(to_validate: str):
#     if to_validate.startswith("https://www.youtube.com/"):
#         return True
#     return False

def valid_duration(to_validate: int):
    if to_validate <= 20:
         return True
    return False

# def validate_award(award_to_validate, connectivity):
#     if connectivity is not False:
#         award_to_validate = ''
#         return f'Нельзя одновременно выбрать связанные привычки и указать вознаграждение'
#     else:
#         return award_to_validate

# def validate_connectivity(connectivity_to_validate, pleasantness):
#     if pleasantness is True:
#         return connectivity_to_validate
#     else:
#         connectivity_to_validate = False
#         return f'В связанные привычки могут попадать только привычки с признаком приятной привычки'

# def validate_pleasantness(pleasantness_to_validate, award, connectivity):
#     if pleasantness_to_validate is True:
#         award = ''
#         connectivity = False
#         return f'У приятной привычки не может быть вознаграждения или связанной привычки.'
#     else:
#         pass

