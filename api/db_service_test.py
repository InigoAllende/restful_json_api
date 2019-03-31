import db_service, sql_queries

import pytest
import mock

from mock import patch

def test_initialize_db():
    with patch('db_service.sqlite3') as mock_db:
        db_service.initialize_db()
        mock_db.connect.assert_called_once_with('metrics.db')

        # mock_cursor = mock_db.connection.cursor.return_value
        # mock_cursor.assert_called_once_with()

        # mock_cursor = mock_connection.cursor.assert_called_once_with()
        # mock_db.connect.cursor.execute.assert_called_once_with(sql_queries.CREATE_TABLE)