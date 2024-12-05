from coursework2.queries import select_all

def test_select_row_count():
    table_name = "Host"
    columns = "*"
    result = select_all(table_name, columns)
    # There should be 30 rows in the table
    assert len(result) == 30


def test_select_host_name():
    table_name = "Host"
    columns = "host"
    expected_result = ('Rome',) # Rows are tuples
    result = select_all(table_name, columns)
    # Rome should appear in the results
    assert expected_result in result
