# import csv
# import os
# import django
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mytest/settings")
# django.setup()
#
# from safehome.models import Crime
#
# CSV_PATH = '/Users/i/Desktop/test_django/safehome/csv_data/crime_in_seoul.csv'
#
# with open(CSV_PATH, 'rt', encoding='UTF8', newline='') as csvfile:
#      data_reader = csv.DictReader(csvfile)
#      for row in data_reader:
#           print(row)
#           Crime.objects.create(
#               area_id = row['자치구'],
#               murder= row['살인'],
#               robber= row['강도'],
#               rape = row['강간강제추행'],
#               theft = row['절도'],
#               violence = row['폭력'],
#               total = row['발생합계'],
#               arr_total = row['검거합계'],
#               arrest = row['검거율']
#           )
