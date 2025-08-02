class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_finish_time = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                start_land = max(landStartTime[i], 0)
                finish_land = start_land + landDuration[i]
                start_water = max(waterStartTime[j], finish_land)
                finish_time_1 = start_water + waterDuration[j]
    
                start_water_2 = max(waterStartTime[j], 0)
                finish_water = start_water_2 + waterDuration[j]
                start_land_2 = max(landStartTime[i], finish_water)
                finish_time_2 = start_land_2 + landDuration[i]
    
                min_finish_time = min(min_finish_time, finish_time_1, finish_time_2)
    
        return min_finish_time
