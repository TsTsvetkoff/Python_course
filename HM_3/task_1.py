"""
Help your future career! You know bubble sort already. Find information on Inserion Sort, Merge
Sort and Quicksort. Wikipedia has a pseudocode example for each of them as well as visualisation. Try
to implement them in Python. Once you have understood them try to make a simple document so you
have an explanation in your own words for reference.
"""

"1) Insertion  + vizualization - https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-6.php "

""" 
Insertion sort in my words : 
A simple example is like when you play cards you order your cards by "strength" from left to right.
We compare the the first item of unsorted portion, with item from sorted portion.
Visualization : https://en.wikipedia.org/wiki/Insertion_sort#/media/File:Insertion_sort.gif 
"""

def insertionSort(nlist):
   for index in range(1,len(nlist)):

     currentvalue = nlist[index]
     position = index

     while position>0 and nlist[position-1]>currentvalue:
         nlist[position]=nlist[position-1]
         position = position-1

     nlist[position]=currentvalue

nlist = [14,46,43,27,57,41,45,21,70]
insertionSort(nlist)
print(nlist)

"2) Merge + vizualization - https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-8.php "


"""
Merge sort in my words :
This type of sorting is based on the principle "divide & conquer" .
This  sorting method is constantly dividing the list by half.
Example : my_list = [2, 8, 5, 3, 9, 4, 1, 7]
The first iteration is the split list into 2 halves
Half_1 = [2, 8, 5, 3]
Half_2  [9, 4, 1, 7]

Second iteration again the 2 halves are again split into 2 halves
Half_3 = [2,8]
Half_4 [5,3]

Half_5 [9,4]
Half_6 [1,7]

This halving iteration continues up to the point where only individual items are left in the list

    [2, 8, 5, 3, 9, 4, 1, 7]
            ||      ||
    [2, 8, 5, 3] [9, 4, 1, 7]
            ||      ||
     [2,8] [5,3]   [9,4]  [1,7]
       ||   ||     ||      ||
    [2][8] [5][3]  [9][4] [1][7]

From that point on (where we have only individual items in the list ) we review the individual items and compare the
values and merge them in temp lists up to the point where all items are sorted
    [2][8] [5][3]  [9][4] [1][7]
      ||    ||       ||     ||
    [2,8]  [3,5]   [4,9]  [7,1]
      ||    ||       ||     ||
      [2,3,5,8]    [1,4,7,9]
             \      /
              \    /
               \  /
          [1,2,3,4,5,7,8,9]   - Expected sorted list 
Visualization : https://bg.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%B0%D0%BD%D0%B5_%D1%87%D1%80%D0%B5%D0%B7_%D1%81%D0%BB%D0%B8%D0%B2%D0%B0%D0%BD%D0%B5#/media/%D0%A4%D0%B0%D0%B9%D0%BB:Merge_sort_animation2.gif

"""


def mergeSort(nlist):
    print("Splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",nlist)

nlist = [2, 8, 5, 3, 9, 4, 1, 7]
mergeSort(nlist)
print(nlist)

"3) Quick + vizualization - https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-9.php "

"""
Quick sort in my words : 
Starting point is where we pick a so called "pivot" == its just one of the items from the list.
We aim to be in the median of the list.
After all items are sorted there are 3 mandatory conditions:
1. The pivot is in correct position in a final / sorted list
2. Items to the left are smaller
3. Items to the right are larger

Example : my_list = [2, 6, 5, 3, 8, 7, 1, 0]
from the list above , pivot = 3

1) The 1st iteration the pivot number (3) is placed at the end of the list
updated_list = [2, 6, 5, 0, 8, 7, 1, 3]

Now in our updated_list we start to search for 2 items:
I) item_From_left that is larger than pivot(3)
II) item_from_right that is smaller than pivot(3)

                                Pivot number (3)
                               / 
        [2, 6, 5, 0, 8, 7, 1, 3]
            ||             ||
    I)item_From_left  II)item_from_right
    
We swap the numbers I) and II) and my_list is now == [2, 1, 5, 0, 8, 7, 6, 3]

2) The second iteration we again aim for I) and II) in the latest version on the list

          II)item_from_right
           /  
[2, 1, 5, 0, 8, 7, 6, 3]
       |
  I)item_From_left
  
Now since we identified the number again we swap those two number (5 and 0) 
The list now is
[2, 1, 0, 5, 8, 7, 6, 3]

Now we swap the pivot number with I)item_From_left ( 5 <--> 3 )

[2, 1, 0, 3, 8, 7, 6, 5]

Now number 3 is in correct spot, why ? 
Because  it meets the 3 mandatory conditions (listed above in the doc):
1. The pivot is in correct position in a final / sorted list
2. Items to the left are smaller [2,1,0]
3. Items to the right are larger [8,7,6,5]

This iterations continues up to the point when:
  index of I)items_From_left > index of II) item_from_right

Expected sorted list is == [0, 1, 2, 3, 5, 6, 7, 8]
Visualization : https://en.wikipedia.org/wiki/Quicksort#/media/File:Sorting_quicksort_anim.gif

"""

def quickSort(data_list):
   quickSortHlp(data_list,0,len(data_list)-1)

def quickSortHlp(data_list,first,last):
   if first < last:

       splitpoint = partition(data_list,first,last)

       quickSortHlp(data_list,first,splitpoint-1)
       quickSortHlp(data_list,splitpoint+1,last)


def partition(data_list,first,last):
   pivotvalue = data_list[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and data_list[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while data_list[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = data_list[leftmark]
           data_list[leftmark] = data_list[rightmark]
           data_list[rightmark] = temp

   temp = data_list[first]
   data_list[first] = data_list[rightmark]
   data_list[rightmark] = temp


   return rightmark

data_list = [2, 6, 5, 3, 8, 7, 1, 0]
quickSort(data_list)
print(data_list)