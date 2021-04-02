class Road:
    def __init__(self, length_m: float, width_m: float):
        self._length = length_m
        self._width = width_m

    def asphalt_tons_calc(self, asphalt_kg_per_sqr_meter: float, depth_sm: float) -> float:
        return self._length * self._width * asphalt_kg_per_sqr_meter * depth_sm / 1000


if __name__ == '__main__':
    road_length = float(input('Enter the length of the road in meters: '))
    road_width = float(input('Enter the width of the road in meters: '))
    asphalt_kg_per_sqr_meter = float(
        input('Enter the mass of asphalt for covering one square meter of road with asphalt in kg: '))
    depth = float(input('Enter the depth of roadbed in sm: '))
    road = Road(road_length, road_width)
    print(f'The mass of asphalt required to cover the entire roadway: {road.asphalt_tons_calc(asphalt_kg_per_sqr_meter, depth)} t', )
