bytes = b'rxx3xa9sumxc3xa9'.decode()
print(bytes)
latin1 = bytes.encode("Latin1")
print(latin1)
latin_bytes = latin1.decode("Latin1")
print(latin_bytes)


