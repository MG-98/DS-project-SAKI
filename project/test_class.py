import os
import pandas as pd
import pytest 

class TestClass:

    def test_existence_of_DB(self):
        """ Check the existence of the DB in the right path """

        assert os.path.exists('../data/project.sqlite')

    def test_tables(self):
        """ Check the existence of the tables in the DB """

        try:
            pd.read_sql_table('hotspots_in_koeln', '../data/project.sqlite')
        except :
            pytest.fail("'hotspots_in_koeln' table is not in the databse ..")    
        try:
            pd.read_sql_table('road_sections', '../data/project.sqlite')
        except :
            pytest.fail("'road_sections' table is not in the databse ..")    

    def test_number_of_coloumsin_tables(self):
        """ Check the tables' number of coloums in the DB in the right number """

        hotspots_in_koeln_df = pd.read_sql_table('hotspots_in_koeln', '../data/project.sqlite')
        road_sections_df = pd.read_sql_table('road_sections', '../data/project.sqlite')

        assert len(hotspots_in_koeln_df.columns) == 8
        assert len(road_sections_df.columns) == 11
