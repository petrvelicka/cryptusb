import lib

c = lib.Crypto("/tmp/key.key")
inf = input("Input file: ")
outf = input("Output file: ")

print("Input file:", open(inf).read(), sep="\n")

c.encrypt_file(inf, outf)
print("Encrypted file:", open(outf).read(), sep="\n")

c.decrypt_file(outf, inf+".dec")
print("Decrypted file:", open(inf+".dec").read(), sep="\n")