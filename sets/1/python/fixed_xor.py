def fixed_xor(hex1, hex2):
  xor = int(hex1, 16) ^ int(hex2, 16)
  hex_xor = hex(xor)
  return hex_xor[2:]

def main():
  hex1 = "1c0111001f010100061a024b53535009181c"
  hex2 = "686974207468652062756c6c277320657965"
  xor_result = "746865206b696420646f6e277420706c6179"
  assert fixed_xor(hex1, hex2) == xor_result

if __name__ == '__main__':
  main()
