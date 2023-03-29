
def find_greatest(arr):
	greatest = arr[0]
	greatest_index = 0

	for i in range(1, len(arr)):
		if arr[i] > greatest:
			greatest = arr[i]
			greatest_index = i

	return greatest_index


def selection_sort(arr):
	new_arr = []

	for i in range(len(arr)):
		greatest = find_greatest(arr)
		new_arr.append(arr.pop(greatest))

	return new_arr


daftar_angka = [5, 3, 6, 2, 10, 10]
print(selection_sort(daftar_angka))

#challenge -> buatkan selection sort yg punya fitur asc, desc
#selection_sort(daftar_angka, "desc")
