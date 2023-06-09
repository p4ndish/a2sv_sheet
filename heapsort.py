#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        last_node = i 
        left = 2 * i + 1 
        right = 2 * i + 2 
        
        
        if left < n and arr[left] > arr[last_node]:
            last_node = left 
            
        if right < n and arr[right] > arr[last_node]:
            last_node = right
            
        if last_node != i:
            arr[i], arr[last_node] = arr[last_node], arr[i]
            
            self.heapify(arr, n , last_node)
            
        
        
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n//2-1, -1, -1):
            self.heapify(arr, n, i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        for i in range(n-1,-1,-1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
            
        
        
