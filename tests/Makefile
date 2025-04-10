SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/../hdl/dut.v
VERILOG_SOURCES += $(PWD)/wrapper/dut_test.v
TOPLEVEL = dut
MODULE = dut_test

all: dut

dut:
	rm -rf sim_build
	$(MAKE) sim MODULE=dut_test TOP_LEVEL=dut
include $(shell cocotb-config --makefiles)/Makefile.sim


