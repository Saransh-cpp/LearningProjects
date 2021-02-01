import colour

table = colour.LUT1D.linear_table(4096)
table = colour.gamma_function(table, 1.8)
LUT = colour.LUT1D(table=table)
path = './MyFile.spi1D'
colour.write_LUT(LUT, path)
