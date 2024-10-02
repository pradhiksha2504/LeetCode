func twoSum(nums []int, target int) []int {
    for i, val := range nums{
        diff := target - val
        // fmt.Println(diff," ",val)
        if slices.Contains(nums, diff){
            ind:=slices.Index(nums,diff)
            if i==ind{
                continue
            }else{
                return []int{i,ind}
            }
        }
    }
    return []int{-1,-1}

}