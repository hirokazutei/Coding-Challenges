
# Hash Table
## What is it?
  Hash Table is a type of data structure that can retrieve a piece of data when you provide a key to it in often O(1) time so as long as the Hash Table is designed well.
  
### How does it work?
  An array structure takes O(1) to retrieve a piece of data when you give it an index. This is because with the given index, the computer can know the exact address of the data stored inside. 
  
  For example:
  You were asked to search for "Kaz's House" to deliver a document on a particular street without any additional information.
  In this case, you will have to ring every doorbell of every residence to check if the individual living there is named "Kaz". 
  This process takes O(N) times meaning that with N amount of houses on the street, you must ring the doorbell proportion of N times to find Kaz. 
  However, if you were given the exact address of the house, there is only really one dorbell you would have ring!  
  
  But indexes are integers and "Kaz" is a string! How do we obtain an index from a data type that is not an integer?
  The answer is:
  
#### Hash Function
  Hash tables allows quick access to stored data by having a hash function. A hash function is a method which takes in the input of a key then outputs an integer, which can be used as the index of that data's storage in an Array/List.
  
  For example:
  We may convert the name "Kaz" into its ASCII representation and concatenate it into "075097122", typecast it into an int 75097122 and voila, we have an index! While it is true that with this method, no name other than "Kaz" would result in the index 75097122, we would need ENORMOUS amount of data to acommodate for various kinds of names with this form of hash function. What if we must store people's names with 10 characters? That would require an array with 10^30 indexes!
  On the other hand, if we change our hash function so that after each ASCII character values are added, "Kaz" would be 294. While this solves the problem of array size since to acommodate for someone with 10 character names, we would only need an array of 1220 size, we are presented with another potential problem. If we were to put other names like "Sen" or "Var" into this particular hash function, they would also result in the index 294, resulting what is known as Collision.
  
  Ideally, the hash function produces an even distribution of numbers and the hash table is large enough that there will not be any collisions of two different keys that has the same result of a hash function, however, it is very common that collision is simply unavoidable. However, there are solutions for such a problem.
  
#### Collision Solution
  Collision can be solved by using Open Addressing or Closed Addressing.
##### Open Addressing
  Open addressing involves storing the conflicting data into another index of a set distance away. If Index[3] is already occupied, a Linear Probing algorithm can be used to find the next empty slot such as Index[4]. However, storing data this way can cause what is known as Primary Clustering, which has a part of the data storage bunched up with stored data.
  To resolve this, other methods can be used, such as Plus 3 Rehash, which finds space in index number of 3 over, quadratic probing which looks for a space in index number of the square of the failed attempts, or another hash function can be used to find the next index, known as Double Hashing.
##### Closed Addressing
  Closed addressing refers to the use of another data structure when collision occurs. Commonly, a linked list is used to solve collisions. When there is a collision, the computer can simply iterate through a linked list to check if what is contained in the linked list is the data needing to be retrieved.
 
