from Crypto.Cipher import AES
from sys import argv

BITS = ('0', '1')
ASCII_BITS = 8

def pad_bits(bits, pad):
	assert len(bits) <= pad
	return [0] * (pad - len(bits)) + bits


def convert_to_bits(n):
	result = []
	if n == 0:
		return [0]
	while n > 0:
		result = [(n % 2)] + result
		n /= 2
	return result

def string_to_bits(s):
	def chr_to_bit(c):
		return pad_bits(convert_to_bits(ord(c)), ASCII_BITS)
	return [b for group in 
			map(chr_to_bit, s)
			for b in group]

#password = string_to_bits(raw_input(": "))
password = string_to_bits("Secret Password")
print password