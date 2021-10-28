## Data Structures in Python

### List
1. List is an mutable data structure
2. It's a linear data structure.
3. With index number of elements in List, we can insert or delete elements.
4. Indexing starts with 0 from left to right and -1 from right to left.

```py
# List program
numbers = [1, "3", 4.5]
print(type(listVar))
```
### Tuple
1. Tuple is immutable data structure
2. It's a linear data structure.
3. With index number of elements in List, we can retrieve elements.
4. It is ordered collection from left to right in sequences.
5. Tuples are classified as immutable sequences. Direct change operations cannot be applied to tuples.
6. Tuples are heterogeneous like Lists. It can store different data types and data structures.
7. Tuples can't be modified. In case of modification, you need to create copy and change elements.

```py
tupleVar = (1, 2, 3)
print(type(tupleVar))
```

### Sets
1. Sets is immutable data structure
2. Sets are unordered. It means it doesn't have indexing for its elements.
3. Sets elements are unique. Duplicate elements are not allowed.
4. A set itself may be modified, but the elements contained in the set must be of an immutable type.

```py
setVar = {1,2,3}
print(type(setVar))
```

### Dictionary
1. Its a key-value data structure.
2. Value can only be retrived by its asociated key.
3. Dictionary supports heterogenous structure.

```py
dictVar = {"name":"rahul", "age":5}
print(type(dictVar))
```
