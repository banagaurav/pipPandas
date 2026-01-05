import camelot

tables = camelot.read_pdf("cene_putarina_eng.pdf", pages="1", flavor="lattice")
print(len(tables))
print(tables[0].df.head())
