import cocotb
from cocotb.triggers import Timer
from random import random as rand

def xor(a, b):
    return a^b

@cocotb.test()
async def dut_test(dut):
    dut.a.value = 0
    dut.b.value = 0
    await Timer(1, 'ns')
    assert dut.y.value == 0, "Simple Test"
    for i in range(10):
        dut.a.value = 0 if rand() < 0.5 else 1
        dut.b.value = 0 if rand() < 0.5 else 1
        await Timer(1, 'ns')
        assert dut.y.value == xor(dut.a.value, dut.b.value), f"Random Test {i+1}"
    