# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 14:19:55 2021

@author: afni
"""

print("fungsi sorting berdasarkan metode bubble sort menggunakan konsep rekursif ")

class bubbleSort:


	def __init__(self, angka):
		self.angka = angka
		self.panjang = len(angka)

	def __str__(self):
		return " ".join([str(x)
						for x in self.angka])

	def bubbleSortRecursive(self, n = None):
		if n is None:
			n = self.panjang

		if n == 1:
			return

		for i in range(n - 1):
			if self.angka[i] > self.angka[i + 1]:
				self.angka[i], self.angka[i + 1] = self.angka[i + 1], self.angka[i]

		self.bubbleSortRecursive(n - 1)

def main():
	angka = [5,1,20,25,2,100,50,4]


	sort = bubbleSort(angka)


	sort.bubbleSortRecursive()
	print("dengan sortingan sebagai berikut :\n", sort)


if __name__ == "__main__":
	main()