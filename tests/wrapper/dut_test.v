module dut_test(input wire a,
	input wire b,
	output wire y
);

dut dut(
    a(a),
	b(b),
	y(y)
);

initial begin
    $dumpfile("waves.vcd");
    $dumpvars;
end
endmodule