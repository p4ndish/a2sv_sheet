class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
#         mod = 10 ** -5
        return [(celsius+273.15),(celsius)*1.80+32.00]
