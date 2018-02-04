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
  File Name: "1. Hash Table.py"
#### Comments:
 - I wasn't sure if I was making a correct form of linked list. In C/C++, I am very used to using a pointer, however, I have not had the experience of using that in Python. I will investigate later to see if I did it right or wrong.
 - I understand that a Load Factor can be calculated from "The Total Numbers of Items Stored" divided by "Size of the Array", and some structures automatically increase the size once load factor reaches a certain value. I am not quite sure how that is implemented without ruining the hash values. I will investigate further.
 
