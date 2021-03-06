import mock

from iatilib import console
from . import AppTestCase


class ConsoleTestCase(AppTestCase):
    def setUp(self):
        super().setUp()
        self.runner = self.app.test_cli_runner()

    @mock.patch('subprocess.run')
    def test_build_docs(self, mock):
        command = 'make dirhtml'
        self.runner.invoke(console.build_docs)
        self.assertEquals(1, mock.call_count)
        self.assertEquals(mock.call_args.args[0], command.split(' '))

    @mock.patch('click.confirm')
    @mock.patch('iatilib.db.drop_all')
    def test_drop_db(self, prompt_mock, drop_all_mock):
        self.runner.invoke(console.drop_database)
        self.assertEquals(1, prompt_mock.call_count)
        self.assertEquals(1, drop_all_mock.call_count)
