class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        Kelvin = celsius + 273.15
        Farrenheit = celsius * 1.80 + 32.00

        return [Kelvin,Farrenheit]
        