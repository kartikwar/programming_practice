
def queue_structure(values):
	while len(values) != 0:
		print(values.pop(0))


if __name__ == "__main__":
	values = [1, 2, 3]
	queue_structure(values)
