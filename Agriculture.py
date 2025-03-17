from abc import ABC, abstractmethod

class Plant(ABC):
    def __init__(self, name, water_needs, fertilizer_needs):
        self.name = name
        self.water_needs = water_needs
        self.fertilizer_needs = fertilizer_needs
    
    @abstractmethod
    def grow(self):
        pass
    
    def calculate_needs(self, rainfall, soil_moisture):
        adjusted_water = self.water_needs - (rainfall * 0.5)
        adjusted_water = max(adjusted_water, 0)  # Ensure water needs do not go negative
        
        adjusted_fertilizer = self.fertilizer_needs
        if soil_moisture > 70:
            adjusted_fertilizer *= 0.9  # Reduce fertilizer if soil moisture is high
        
        self.water_needs = adjusted_water
        self.fertilizer_needs = adjusted_fertilizer
    
    def show_needs(self, rainfall, soil_moisture):
        print(f"Weather Report: Rainfall = {rainfall} mm, Soil Moisture = {soil_moisture}%")
        print(f"Adjusted Water Needs: {self.water_needs} liters")
        print(f"Adjusted Fertilizer Needs: {self.fertilizer_needs} kg\n")

class RicePlant(Plant):
    def __init__(self):
        super().__init__("Rice", 20, 5)
    
    def grow(self):
        print("Rice is growing in the paddy field")

class CornPlant(Plant):
    def __init__(self):
        super().__init__("Corn", 18, 7)
    
    def grow(self):
        print("Corn is growing in the farm")

# Simulasi kondisi cuaca
weather_conditions = [
    {"rainfall": 10, "soil_moisture": 75},
    {"rainfall": 2, "soil_moisture": 40}
]

# Membuat objek tanaman
rice = RicePlant()
corn = CornPlant()

# Menjalankan simulasi
for plant, condition in zip([rice, corn], weather_conditions):
    plant.grow()
    plant.calculate_needs(condition["rainfall"], condition["soil_moisture"])
    plant.show_needs(condition["rainfall"], condition["soil_moisture"])
