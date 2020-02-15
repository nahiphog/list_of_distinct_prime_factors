######################################################
##### [1] Quadratic residue
######################################################
input_number = 10 ** 2
quadratic_residues = [ (integer ** 2) % input_number for integer in range(0, input_number )]
quadratic_residues.sort()
print(set(quadratic_residues))

######################################################
##### [2] Last few digits
######################################################
for integer in range(1000, 9999 + 1):
    if len(str(integer ** 2)) == 8:
        if str(integer ** 2 - integer).endswith('0000'):
            print(integer)
