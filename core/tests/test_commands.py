"""
Test custom Django mgmt commands
"""
from unittest.mock import patch  # mock behaviour of DB
from psycopg2 import OperationalError as Psycopg2Error

# lets me call the custom command to test it
from django.core.management import call_command

# another exception that may get thrown from db
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for db if db ready"""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    # patch time.sleep overrides the default behaviour of sleep
    # it is esentially just a mock of it, so it stays performant for the test
    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """
        Test waiting for db when getting OperationalError.
        The first 2 times the mock-function gets called - the Psycopg2Error is being thrown -> (db not rdy for connection yet).

        The next 3 times the OperationalError is thrown. -> (db is rdy for connection but not yet finished loading)

        Expected behaviour: DB should be unavailable 5 times, then a "Database is now available" should be returned
        """

        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
