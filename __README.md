# Coding-Challenges
In Preparation for Interviews, I am coding common data structures and algorithms as an exercise and for fun!

## Background

## Format
##### A. I will first write the code to a data structure or an algorithm with Python without looking at example codes.
##### B. I will evaluate my code and find potential problems and improvements that I could made.
##### C. I will compare my code to a conventionally written one and study how I could have written it better or had I made any mistakes.

## Hash Table
#### What is it?
  My understanding of a hash table is that: it is a data structure which each datum being stored has a key and whatever data associated with that key (a name [key] and a phone number [data], for example).
#### Hash Function
  Hashtables allows quick access to stored data by having a hash function. A hash function takes in the input of a key then outputs a number, which can be used as the index of that datum's storage in an Array/List.
  Ideally, the hash function produces an even distribution of numbers and the hash table is large enough that there will not be any collisions of two different keys that has the same result of a hash function.
#### Collision Solution
  Collision can be solved by using Open Addressing or Closed Addressing.
##### Open Addressing
  Open addressing involves storing the conflicting data into another index of a set distance away. If Index[3] is already occupied, a Linear Probing algorithm can be used to find the next empty slot such as Index[4]. However, storing data this way can cause what is known as Primary Clustering, which has a part of the data storage bunched up with stored data.
  To resolve this, other methods can be used, such as Plus 3 Rehash, which finds space in index number of 3 over, quadratic probing which looks for a space in index number of the square of the failed attempts, or another hash function can be used to find the next index, known as Double Hashing.
##### Closed Addressing
  Closed addressing refers to the use of another data structure when collision occurs. Commonly, a linked list is used to solve collisions. When there is a collision, the datum being stored can be pointed to by the current occupant of where the datum was intended to be stored. 

### A. Self Implimentation
  File Name: "Coding Challenges/Data Structures/Hash Table.py"
#### Comments:
 - I was not sure if I was making a correct form of linked list. In C/C++, I am very used to using a pointer, however, I have not had the experience of using that in Python. I will investigate later to see if I did it right or wrong.
 - I understand that a Load Factor can be calculated from "The Total Numbers of Items Stored" divided by "Size of the Array", and some structures automatically increase the size once load factor reaches a certain value. I am not quite sure how that is implemented without ruining the hash values. I will investigate further.
 
 
 ## Sorting Algorithms
#### What is it?
  I am planning to code all the major sorting algorithms. I will read the explanations of the algorithm online but not the psudocode or code themselves.
#### Insertion Sort
  Insertion Sort takes each item from the list, compares it with the "sorted" list before its index (because the first item by itself is technically "sorted", second item can be sorted to be inserted in front of it or behind it, and so on...) and inserts the item in its appropriate position.
#### Selection Sort
  Selection sort involves finding the smallest item in a list, inserting that item at index[0], then repeat the process to find the second smallest item and insert it into the next index.
##### Bubble Sort
  Bubble sort iterate through the list and compares each index item with the next, and switching them around should the larger index item be smaller. Therefore, with the first iteration, the largest item should be at the very end of the list, meaning that next time the algorithm iterate through the list, it can igore the latter sorted items. Once the algorithm does an iteration with no swaps, the list is sorted.
##### Quick Sort
  Quick sort picks a pivot from the list and sorts the list so that indexes lower than the pivot will have smaller values than the pivot, while indexes higher than the pivot will have values higher than the pivot. With recursion, this process is repeated until all items are sorted in order.

### A. Self Implimentation
  File Name: "Coding Challenges/Algorithms/Sorting/Sorting.py"
#### Comments:
 - While most of the sorting methods were quite easy to implement, I hate to admit but the quick sort did take me some time to get it completely fool proof. However, the code for quick sort is still very sloppy and I hope to clean it up.
 - I believe I can make bubble sort slightly faster by ignoring more of the sorted index at the back.
 
