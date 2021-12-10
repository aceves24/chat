
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as file:
		for line in file:
			# if 'Allen' in line or 'Tom' in line
			lines.append(line.strip())			
	return lines

def convert(lines):
	new = []
	person = None                       # person 設定預設值為 None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:                     # if person: 表示如果person有值
			new.append(person + ': ' + line)
	return new


def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8') as file:
		for line in lines:
			file.write(line + '\n')


def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()