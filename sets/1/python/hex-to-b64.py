from codecs import encode, decode

def hex_to_b64(hex_str):
  hex_bytes = decode(hex_str, 'hex')
	b64_bytes = encode(hex_bytes, 'base64')
	return b64_bytes.decode().replace("\n","")
