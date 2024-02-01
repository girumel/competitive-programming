class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        answer = [celsius + 273.15, (celsius * (9/5)) + 32]
        return answer