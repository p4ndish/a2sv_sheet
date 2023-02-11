      for i in range(len(arr)):
          mn = i
          for j in range(i+1, len(arr)):
              # nxt = self.select(arr, i+1)
              # mn = min(mn, arr[i])
              if j < mn :
                  mn = j

          if mn != i:
              arr[mn], arr[i] = arr[i], arr[mn]
      return arr 
