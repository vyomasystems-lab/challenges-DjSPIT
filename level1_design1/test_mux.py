# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def basic_test_mux(dut):
    """Basic Test for mux2 - Select Line == 5"""
    cocotb.log.info('##### CTB: Develop your test here ########')

    select_line = 5 # 00101
    input_val = 10

    dut.inp5.value = input_val

    dut.sel.value = 0
    yield Timer(10, 'ns')
    expected = 0
    if dut.out.value != expected:
        raise TestError("inp_data={:02}, select_line={:01}, expected value {}, found {}".format(dut.inp5.value, dut.sel.value, expected, dut.out.value))

    dut.sel.value = select_line
    yield Timer(10, 'ns')
    expected = input_val
    if dut.out.value != expected:
        raise TestError("inp_data={:02}, select_line={:01}, expected value {}, found {}".format(dut.inp5.value, dut.sel.value, expected, dut.out.value))
