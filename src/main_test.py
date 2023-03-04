from click.testing import CliRunner
import unittest

from main import comp

def compile_test():
    runner = CliRunner()
    result = runner.invoke(comp,['test/index.md','--outdir=test/out.html'])
    assert result.exit_code == 0
    assert result.output == ''
