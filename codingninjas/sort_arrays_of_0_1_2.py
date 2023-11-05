def sortArray(arr, n):
	low,mid,high=0,0,n-1
	while mid<=high:
		if arr[mid]==0:
			arr[low],arr[mid]=arr[mid],arr[low]
			low+=1
			mid+=1
		elif arr[mid]==2:
			arr[high],arr[mid]=arr[mid],arr[high]
			high-=1
		else:
			mid+=1