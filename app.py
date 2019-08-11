from flask import Flask, jsonify
from flask_restful import Resource, reqparse, Api

app = Flask(__name__)
api = Api(app)

class Version(Resource):
  def get(self):
    return '1.0.0 - August 10, 2019'

class Coordinates(Resource):
  def(self,stop):
    stops = {}
    if stop in stops:
      return(jsonify({stop:stops.get(stop)}))
    else:
      return(jsonify({"error":stop}))
      
class Routes(Resource):
  def get(self, startLat, startLng, endLat, endLng):
    startLat = float(startLat)
    startLng = float(startLng)
    endLat = float(endLat)
    endLng = float(endLng)
    
    stops = [['02 Transit - IB', 30.617798, -96.354623], ['02 Transit - OB', 30.617894, -96.354525], ['06 Transit - IB', 30.617793, -96.354621], ['06 Transit - OB', 30.617893, -96.354526], ['Academic Village', 30.631041, -96.35462], ['Ag Building - IB', 30.605639, -96.349805], ['Ag Building - OB', 30.605429, -96.350468], ['Aggie Station - IB', 30.624822, -96.352609], ['Aggie Station - OB', 30.624919, -96.352472], ['Alpine Circle', 30.606511, -96.315584], ['April Bloom - East', 30.637594, -96.31968], ['April Bloom - West', 30.637617, -96.319919], ['Arbor Square', 30.605989, -96.310399], ['Arbors @ Wolf Pen Creek - IB', 30.615851, -96.312602], ['Arbors @ Wolf Pen Creek - OB', 30.615708, -96.312498], ['Asbury Water Tower', 30.617866, -96.343404], ['Ashburn - East', 30.631888, -96.322527], ['Ashburn - West', 30.632022, -96.322744], ['Aspen Heights', 30.581506, -96.328277], ['Atlas Pear Dr - IB', 30.603147, -96.378384], ['Beutel', 30.615732, -96.343191], ['Blinn - Rellis', 30.642203, -96.467353], ['Blinn College', 30.663226, -96.351816], ['Brentwood', 30.606126, -96.313378], ['Briarwood', 30.626441, -96.309635], ['Broadmoor - East', 30.656346, -96.343768], ['Broadmoor - West', 30.656079, -96.343521], ['Bush School - IB', 30.599092, -96.352601], ['Bush School - OB', 30.59923, -96.35277], ['Callaway Villas', 30.601194, -96.338656], ['Carter Creek Shopping Center', 30.646708, -96.333511], ['Castlerock', 30.627564, -96.30651], ['Centeq 1', 30.601509, -96.357574], ['Centeq 2', 30.601203, -96.358297], ['CIR', 30.647959, -96.474683], ['Colgate Circle', 30.612126, -96.306753], ['College Main Parking Garage - IB', 30.619501, -96.34687], ['College Main Parking Garage - OB', 30.619521, -96.346681], ['Commons', 30.615178, -96.337378], ['Cripple Creek - East', 30.62394, -96.312779], ['Cripple Creek - West', 30.624031, -96.31289], ['Deacon - West', 30.572439, -96.320719], ['Eastmark/Windsor Pointe', 30.615483, -96.299839], ['Element @ University Park', 30.641514, -96.329799], ['Enclave', 30.611808, -96.318428], ['Equine Center - IB', 30.615212, -96.36619], ['Equine Center - OB', 30.6156, -96.365993], ['Facilities Services - IB', 30.619766, -96.356418], ['Facilities Services - OB', 30.61987, -96.356329], ['Fish Pond - IB', 30.616409, -96.343022], ['Fish Pond - OB', 30.616525, -96.343859], ['Fox Run', 30.591927, -96.344156], ['Fraternity Row', 30.576202, -96.314427], ['Gateway', 30.593964, -96.336676], ['Gridiron', 30.590772, -96.335683], ['GSC', 30.6218, -96.357606], ['Health Science Center', 30.597936, -96.395403], ['HEB', 30.611945, -96.318548], ['Hensel @ Texas', 30.629891, -96.339048], ['Holleman South - IB', 30.584805, -96.336722], ['Holleman South - OB', 30.584122, -96.337515], ['Howdy Street', 30.63305, -96.35424], ['Huntington Apt', 30.621318, -96.309521], ['Kleberg - IB', 30.609754, -96.346665], ['Kleberg - OB', 30.609846, -96.346985], ['Laurel Ridge', 30.639592, -96.326049], ['Laurel Ridge - West', 30.637797, -96.327072], ['Lemon Tree', 30.607067, -96.317701], ['Lexington - North', 30.608927, -96.320332], ['Lexington - South', 30.609458, -96.321265], ['Lofts @ Wolf Pen Creek - IB', 30.618471, -96.308278], ['Lofts @ Wolf Pen Creek - OB', 30.618325, -96.308056], ['Lot 100G', 30.604797, -96.345232], ['Lot 108/UPD', 30.604317, -96.358494], ['Lot 41/43', 30.598075, -96.355088], ['Lot 71', 30.615763, -96.352766], ['Madison Point', 30.593517, -96.326772], ['MSC', 30.614133, -96.343276], ['NCTM', 30.608603, -96.360708], ['North West - Park West - OB', 30.599502, -96.341795], ['Old Main', 30.614541, -96.342422], ['Olsen Field @ Blue Bell Park', 30.605027, -96.342803], ['Physical Education - IB', 30.605465, -96.349306], ['Physical Education - OB', 30.604919, -96.348996], ['PMC East', 30.609349, -96.372924], ['PMC West', 30.609246, -96.373188], ['Rec Center', 30.607005, -96.345], ['Redstone', 30.608055, -96.312795], ['Reed Arena - IB', 30.605585, -96.347413], ['Reed Arena - OB', 30.607109, -96.348008], ['Renaissance Park', 30.595204, -96.32382], ['Reveille Ranch', 30.628463, -96.359741], ['River Oaks Townhomes - IB', 30.617503, -96.31083], ['River Oaks Townhomes - OB', 30.617386, -96.310647], ['Ross and Bizzell - IB', 30.619722, -96.338433], ['Ross and Bizzell - OB', 30.619791, -96.338158], ['Ross and Ireland - IB', 30.617895, -96.341085], ['Ross and Ireland - OB', 30.617654, -96.341261], ['Scandia - North', 30.611259, -96.323467], ['Scandia - South', 30.611391, -96.323987], ['School of Public Health - IB', 30.609366, -96.353824], ['School of Public Health - OB', 30.609365, -96.353825], ['South East - Park West', 30.597336, -96.33844], ['South East - Park West 2', 30.595977, -96.339922], ['Southwest Parkway @ Cornell', 30.609516, -96.306522], ['Southwest Parkway @ Dartmouth', 30.612257, -96.303454], ['Spruce St. - IB', 30.621748, -96.349199], ['Spruce St. - OB', 30.621978, -96.349237], ['The Barracks', 30.573007, -96.320103], ['The Cambridge', 30.620485, -96.316983], ['The Gardens 1', 30.626712, -96.343138], ['The Gardens 2', 30.628543, -96.342054], ['The Junction', 30.58138, -96.33621], ['The London', 30.59392, -96.341986], ['The Marc', 30.620011, -96.317254], ['The Rail - East', 30.621589, -96.315461], ['The Rail - West', 30.62166, -96.315599], ['The Retreat', 30.589124, -96.333938], ['The Woodlands #1', 30.591871, -96.329197], ['The Woodlands #2', 30.5919, -96.329563], ['Trails @ Wolf Penn Creek', 30.617967, -96.301788], ['Treehouse', 30.601049, -96.338813], ['Trigon', 30.613928, -96.339018], ['TTI - IB', 30.601607, -96.352653], ['TTI - OB', 30.602088, -96.353173], ['Turf Lab - IB', 30.617003, -96.364226], ['Turf Lab - OB', 30.617101, -96.36434], ['U-Club', 30.596521, -96.336588], ['University Park', 30.597517, -96.321136], ['University Square - East', 30.627329, -96.327573], ['University Square - West', 30.627426, -96.327723], ['University Trails', 30.58984, -96.346495], ['Vet School', 30.61139, -96.357289], ['Vet School - IB', 30.614345, -96.351468], ['Vet School - OB', 30.615297, -96.352154], ['Villa Maria @ Green St.', 30.637974, -96.361717], ['Village on the Creek', 30.626209, -96.355866], ['Village St.', 30.610814, -96.320601], ['Wehner', 30.611935, -96.347942], ['Wehner N', 30.612138, -96.349534], ['Wehner S', 30.611936, -96.348715], ['Wellborn @ Tee', 30.633018, -96.363898], ['Welsh @ Balcones', 30.587765, -96.315014], ['Welsh @ Deacon', 30.581449, -96.309674], ['Welsh @ First Baptist', 30.587347, -96.31509], ['Welsh @ Navarro - IB', 30.584801, -96.313182], ['Welsh @ Navarro - OB', 30.584896, -96.313036], ['West - Park West - IB', 30.598274, -96.343169], ['West - Park West - OB', 30.597952, -96.343228], ['White Creek - IB', 30.607351, -96.354712], ['White Creek #2 - IB', 30.60676, -96.356981], ['White Creek - OB', 30.607513, -96.354968], ['White Creek #2 - OB', 30.606772, -96.356665], ['Willow Oaks', 30.646688, -96.33363], ['Willowick', 30.593716, -96.326031], ['Wisenbaker - East', 30.620952, -96.338117], ['Wolf Pen Creek', 30.619816, -96.304408], ['Woodsman', 30.593827, -96.339247], ['Yellow House', 30.595603, -96.322718], ['Z Islander', 30.627179, -96.358579]]
    graph = {'02 Transit - IB': {'School of Public Health - IB': [3, 2], '02 Transit - OB': [0, -1]}, '02 Transit - OB': {'Turf Lab - OB': [4, 2], '02 Transit - IB': [0, -1]}, '06 Transit - IB': {'Lot 71': [1, 6], '06 Transit - OB': [0, -1]}, '06 Transit - OB': {'Facilities Services - OB': [1, 6], '06 Transit - IB': [0, -1]}, 'Academic Village': {'Aggie Station - IB': [2, 15, 150]}, 'Ag Building - IB': {'Reed Arena - IB': [6, 305, 5]}, 'Ag Building - OB': {'TTI - OB': [1, 5]}, 'Aggie Station - IB': {'Spruce St. - IB': [1, 15, 150], 'Aggie Station - OB': [0, -1]}, 'Aggie Station - OB': {'Village on the Creek': [1, 15, 150], 'Aggie Station - IB': [0, -1]}, 'Alpine Circle': {'Lexington - North': [1, 26], 'Lemon Tree': [1, -1]}, 'April Bloom - East': {'Laurel Ridge - West': [2, 1225, 25], 'April Bloom - West': [0, -1]}, 'April Bloom - West': {'Ashburn - West': [3, 1225, 25], 'April Bloom - East': [0, -1]}, 'Arbor Square': {'Southwest Parkway @ Cornell': [3, 26]}, 'Arbors @ Wolf Pen Creek - IB': {'HEB': [1, 27], 'Arbors @ Wolf Pen Creek - OB': [0, -1]}, 'Arbors @ Wolf Pen Creek - OB': {'River Oaks Townhomes - OB': [1, 27], 'Arbors @ Wolf Pen Creek - IB': [0, -1]}, 'Asbury Water Tower': {'Wehner': [9, 1, 104], 'Fish Pond - IB': [1, 4, -1], 'Fish Pond - OB': [2, -1]}, 'Ashburn - East': {'April Bloom - East': [4, 1225, 25], 'Ashburn - West': [0, -1]}, 'Ashburn - West': {'University Square - West': [1, 1225, 25], 'Ashburn - East': [0, -1]}, 'Aspen Heights': {'Holleman South - IB': [5, 40]}, 'Atlas Pear Dr - IB': {'PMC East': [2, 2]}, 'Beutel': {'Wehner N': [3, 3, 305, 6], 'Kleberg - OB': [6, 8], 'Fish Pond - IB': [1, -1], 'Fish Pond - OB': [1, -1], 'MSC': [1, -1]}, 'Blinn - Rellis': {'CIR': [2, 47]}, 'Blinn College': {'Broadmoor - West': [3, 12, 1225]}, 'Brentwood': {'Arbor Square': [1, 26]}, 'Briarwood': {'Cripple Creek - West': [1, 22]}, 'Broadmoor - East': {'Blinn College': [5, 12, 1225], 'Broadmoor - West': [0, -1]}, 'Broadmoor - West': {'Willow Oaks': [4, 12, 1225], 'Broadmoor - East': [0, -1]}, 'Bush School - IB': {'TTI - IB': [1, 305, 5], 'Bush School - OB': [0, -1]}, 'Bush School - OB': {'Centeq 1': [1, 5], 'Bush School - IB': [0, -1]}, 'Callaway Villas': {'Trigon': [8, 36], 'Treehouse': [0, -1]}, 'Carter Creek Shopping Center': {'Broadmoor - East': [6, 12, 1225], 'Willow Oaks': [0, -1]}, 'Castlerock': {'Briarwood': [1, 22]}, 'Centeq 1': {'Lot 108/UPD': [1, 5], 'Centeq 2': [1, -1]}, 'Centeq 2': {'Lot 41/43': [1, 305, 5], 'Centeq 1': [1, -1]}, 'CIR': {'MSC': [23, 47]}, 'Colgate Circle': {'Redstone': [3, 26]}, 'College Main Parking Garage - IB': {'Fish Pond - OB': [2, 15, 150], 'College Main Parking Garage - OB': [0, -1]}, 'College Main Parking Garage - OB': {'Spruce St. - OB': [1, 150], 'College Main Parking Garage - IB': [0, -1]}, 'Commons': {'Ross and Bizzell - OB': [3, 1], 'The Gardens 1': [7, 104], 'Trigon': [6, -1]}, 'Cripple Creek - East': {'Castlerock': [1, 22], 'Cripple Creek - West': [0, -1]}, 'Cripple Creek - West': {'The Rail - West': [1, 22], 'Cripple Creek - East': [0, -1]}, 'Deacon - West': {'Aspen Heights': [3, 40]}, 'Eastmark/Windsor Pointe': {'Trails @ Wolf Penn Creek': [1, 26]}, 'Element @ University Park': {'Carter Creek Shopping Center': [2, 12, 1225]}, 'Enclave': {'Arbors @ Wolf Pen Creek - OB': [3, 27], 'HEB': [0, -1]}, 'Equine Center - IB': {'Turf Lab - IB': [2, 2], 'Equine Center - OB': [0, -1]}, 'Equine Center - OB': {'PMC West': [2, 2], 'Equine Center - IB': [0, -1]}, 'Facilities Services - IB': {'06 Transit - IB': [1, 6], 'Facilities Services - OB': [0, -1]}, 'Facilities Services - OB': {'GSC': [1, 6], 'Facilities Services - IB': [0, -1]}, 'Fish Pond - IB': {'Spruce St. - OB': [4, 15], 'School of Public Health - OB': [5, 2], 'Ross and Ireland - IB': [1, 4], 'Asbury Water Tower': [2, -1], 'Beutel': [1, -1], 'Fish Pond - OB': [0, -1], 'MSC': [5, -1]}, 'Fish Pond - OB': {'MSC': [5, 15, 150, -1], 'Ross and Ireland - IB': [1, 1, 104], 'Asbury Water Tower': [2, -1], 'Beutel': [1, -1], 'Fish Pond - IB': [0, -1]}, 'Fox Run': {'The London': [1, 35]}, 'Fraternity Row': {'Welsh @ Navarro - IB': [2, 34]}, 'Gateway': {'U-Club': [3, 36]}, 'Gridiron': {'The Retreat': [1, 35]}, 'GSC': {'Facilities Services - IB': [1, 6]}, 'Health Science Center': {'Atlas Pear Dr - IB': [3, 2]}, 'HEB': {'Village St.': [1, 27], 'Enclave': [0, -1]}, 'Hensel @ Texas': {'Ross and Bizzell - OB': [3, 104, 4]}, 'Holleman South - IB': {'West - Park West - IB': [10, 40], 'Holleman South - OB': [0, -1]}, 'Holleman South - OB': {'The Junction': [1, 40], 'Holleman South - IB': [0, -1]}, 'Howdy Street': {'Academic Village': [1, 15, 150]}, 'Huntington Apt': {'Wolf Pen Creek': [1, 27]}, 'Kleberg - IB': {'MSC': [7, 35, 40, 305, 5], 'Old Main': [4, 1, 104], 'Beutel': [9, 8], 'Kleberg - OB': [0, -1], 'Wehner': [6, -1], 'Wehner N': [6, -1], 'Wehner S': [6, -1]}, 'Kleberg - OB': {'Physical Education - OB': [1, 35, 40], 'Rec Center': [1, 1, 104], 'Reed Arena - OB': [1, 5, 8], 'Kleberg - IB': [0, -1], 'Wehner': [6, -1], 'Wehner N': [6, -1], 'Wehner S': [6, -1]}, 'Laurel Ridge': {'April Bloom - West': [3, 1225, 25]}, 'Laurel Ridge - West': {'Element @ University Park': [2, 1225], 'Laurel Ridge': [1, 25]}, 'Lemon Tree': {'Brentwood': [1, 26], 'Alpine Circle': [1, -1]}, 'Lexington - North': {'Scandia - North': [1, 26], 'Lexington - South': [0, -1]}, 'Lexington - South': {'Lemon Tree': [2, 26], 'Enclave': [2, 27], 'Lexington - North': [0, -1]}, 'Lofts @ Wolf Pen Creek - IB': {'River Oaks Townhomes - IB': [1, 27], 'Lofts @ Wolf Pen Creek - OB': [0, -1]}, 'Lofts @ Wolf Pen Creek - OB': {'Huntington Apt': [1, 27], 'Lofts @ Wolf Pen Creek - IB': [0, -1]}, 'Lot 100G': {'Reed Arena - IB': [1, 1, 104, -1], 'Reed Arena - OB': [0, -1]}, 'Lot 108/UPD': {'Centeq 2': [1, 5]}, 'Lot 41/43': {'Bush School - IB': [1, 305, 5]}, 'Lot 71': {'Vet School - IB': [1, 6]}, 'Madison Point': {'The Woodlands #2': [1, 31], 'Willowick': [0, -1]}, 'MSC': {'Fish Pond - IB': [1, 15, -1], 'Kleberg - OB': [4, 35, 40, 5], 'Wisenbaker - East': [9, 47], 'College Main Parking Garage - OB': [3, 150], 'Beutel': [1, 305, -1], 'Fish Pond - OB': [5, -1], 'Trigon': [6, -1]}, 'NCTM': {'Vet School': [2, 3]}, 'North West - Park West - OB': {'Olsen Field @ Blue Bell Park': [3, 8]}, 'Old Main': {'Fish Pond - OB': [1, 1, 104], 'Beutel': [1, 3]}, 'Olsen Field @ Blue Bell Park': {'Rec Center': [2, 8]}, 'Physical Education - IB': {'Kleberg - IB': [1, 35, 40], 'Physical Education - OB': [0, -1]}, 'Physical Education - OB': {'West - Park West - OB': [2, 35, 40], 'North West - Park West - OB': [2, 8], 'Physical Education - IB': [0, -1]}, 'PMC East': {'Equine Center - IB': [2, 2]}, 'PMC West': {'Health Science Center': [1, 2]}, 'Rec Center': {'Lot 100G': [1, 1, 104], 'Kleberg - IB': [1, 8]}, 'Redstone': {'Alpine Circle': [2, 26]}, 'Reed Arena - IB': {'Kleberg - IB': [1, 1, 104, 305, 5], 'Lot 100G': [0, -1], 'Reed Arena - OB': [1, -1]}, 'Reed Arena - OB': {'Ag Building - OB': [1, 5], 'Physical Education - OB': [1, 8], 'Lot 100G': [0, -1], 'Reed Arena - IB': [1, -1]}, 'Renaissance Park': {'Madison Point': [1, 31], 'Yellow House': [1, -1]}, 'Reveille Ranch': {'Wellborn @ Tee': [2, 15, 150]}, 'River Oaks Townhomes - IB': {'Arbors @ Wolf Pen Creek - IB': [1, 27], 'River Oaks Townhomes - OB': [0, -1]}, 'River Oaks Townhomes - OB': {'Lofts @ Wolf Pen Creek - OB': [1, 27], 'River Oaks Townhomes - IB': [0, -1]}, 'Ross and Bizzell - IB': {'Commons': [8, 1, 104], 'Wisenbaker - East': [1, 4], 'Ross and Bizzell - OB': [0, -1]}, 'Ross and Bizzell - OB': {'Ross and Ireland - OB': [2, 1, 104, 4], 'Ross and Bizzell - IB': [0, -1]}, 'Ross and Ireland - IB': {'Ross and Bizzell - IB': [1, 1, 104, 4], 'Ross and Ireland - OB': [0, -1]}, 'Ross and Ireland - OB': {'Asbury Water Tower': [2, 1, 104, 4], 'Ross and Ireland - IB': [0, -1]}, 'Scandia - North': {'Trigon': [6, 26, 27], 'Scandia - South': [0, -1]}, 'Scandia - South': {'Lexington - South': [1, 26, 27], 'Scandia - North': [0, -1]}, 'School of Public Health - IB': {'Fish Pond - IB': [4, 2], 'School of Public Health - OB': [0, -1]}, 'School of Public Health - OB': {'02 Transit - OB': [5, 2], 'School of Public Health - IB': [0, -1]}, 'South East - Park West': {'South East - Park West 2': [1, 36]}, 'South East - Park West 2': {'Woodsman': [1, 36]}, 'Southwest Parkway @ Cornell': {'Southwest Parkway @ Dartmouth': [1, 26]}, 'Southwest Parkway @ Dartmouth': {'Eastmark/Windsor Pointe': [1, 26]}, 'Spruce St. - IB': {'College Main Parking Garage - IB': [1, 15, 150], 'Spruce St. - OB': [0, -1]}, 'Spruce St. - OB': {'Aggie Station - OB': [1, 15, 150], 'Spruce St. - IB': [0, -1]}, 'The Barracks': {'Fraternity Row': [4, 34]}, 'The Cambridge': {'Trigon': [8, 22], 'The Marc': [0, -1]}, 'The Gardens 1': {'The Gardens 2': [1, 104, 4]}, 'The Gardens 2': {'Hensel @ Texas': [1, 104, 4]}, 'The Junction': {'Deacon - West': [6, 40]}, 'The London': {'West - Park West - IB': [2, 35]}, 'The Marc': {'The Rail - East': [1, 22], 'The Cambridge': [0, -1]}, 'The Rail - East': {'Cripple Creek - East': [2, 22]}, 'The Rail - West': {'The Cambridge': [1, 22]}, 'The Retreat': {'University Trails': [1, 35]}, 'The Woodlands #1': {'Willowick': [1, 31], 'The Woodlands #2': [0, -1]}, 'The Woodlands #2': {'Trigon': [7, 31], 'The Woodlands #1': [0, -1]}, 'Trails @ Wolf Penn Creek': {'Colgate Circle': [3, 26]}, 'Treehouse': {'South East - Park West': [1, 36], 'Callaway Villas': [0, -1]}, 'Trigon': {'Element @ University Park': [8, 12], 'University Square - East': [7, 1225, 25], 'The Marc': [7, 22], 'Scandia - South': [4, 26, 27], 'The Woodlands #1': [9, 31], 'Welsh @ First Baptist': [11, 34], 'Treehouse': [3, 36], 'Commons': [6, -1], 'MSC': [6, -1]}, 'TTI - IB': {'Ag Building - IB': [1, 305, 5], 'TTI - OB': [0, -1]}, 'TTI - OB': {'Bush School - OB': [1, 5], 'TTI - IB': [0, -1]}, 'Turf Lab - IB': {'02 Transit - IB': [1, 2]}, 'Turf Lab - OB': {'Equine Center - OB': [1, 2]}, 'U-Club': {'Callaway Villas': [1, 36]}, 'University Park': {'Renaissance Park': [1, 31]}, 'University Square - East': {'Ashburn - East': [1, 1225, 25], 'University Square - West': [0, -1]}, 'University Square - West': {'Trigon': [15, 1225, 25], 'University Square - East': [0, -1]}, 'University Trails': {'Fox Run': [1, 35]}, 'Vet School': {'White Creek #2 - IB': [2, 3]}, 'Vet School - IB': {'Wehner S': [1, 6], 'Vet School - OB': [0, -1]}, 'Vet School - OB': {'06 Transit - OB': [1, 6], 'Vet School - IB': [0, -1]}, 'Villa Maria @ Green St.': {'Howdy Street': [2, 15, 150]}, 'Village on the Creek': {'Z Islander': [1, 15, 150]}, 'Village St.': {'Scandia - North': [1, 27]}, 'Wehner': {'Kleberg - OB': [1, 1, 104, -1], 'Kleberg - IB': [6, -1], 'Wehner N': [2, -1, -1], 'Wehner S': [2, -1, -1]}, 'Wehner N': {'White Creek - OB': [3, 3, 305], 'Vet School - OB': [2, 6], 'Kleberg - IB': [6, -1], 'Kleberg - OB': [6, -1], 'Wehner': [2, -1, -1], 'Wehner S': [2, -1, -1]}, 'Wehner S': {'Old Main': [3, 3], 'Beutel': [5, 6], 'Kleberg - IB': [6, -1], 'Kleberg - OB': [6, -1], 'Wehner': [2, -1, -1], 'Wehner N': [2, -1, -1]}, 'Wellborn @ Tee': {'Villa Maria @ Green St.': [2, 15, 150]}, 'Welsh @ Balcones': {'Trigon': [11, 34]}, 'Welsh @ Deacon': {'The Barracks': [5, 34]}, 'Welsh @ First Baptist': {'Welsh @ Navarro - OB': [1, 34]}, 'Welsh @ Navarro - IB': {'Welsh @ Balcones': [1, 34]}, 'Welsh @ Navarro - OB': {'Welsh @ Deacon': [1, 34]}, 'West - Park West - IB': {'Physical Education - IB': [2, 35, 40]}, 'West - Park West - OB': {'Woodsman': [1, 35], 'Holleman South - OB': [10, 40]}, 'White Creek - IB': {'Wehner S': [3, 3]}, 'White Creek #2 - IB': {'White Creek - IB': [1, 3]}, 'White Creek - OB': {'White Creek #2 - OB': [1, 3], 'Centeq 2': [2, 305]}, 'White Creek #2 - OB': {'NCTM': [2, 3]}, 'Willow Oaks': {'Trigon': [13, 12], 'Laurel Ridge': [1, 1225], 'Carter Creek Shopping Center': [0, -1]}, 'Willowick': {'Yellow House': [2, 31], 'Madison Point': [0, -1]}, 'Wisenbaker - East': {'Blinn - Rellis': [21, 47], 'The Gardens 1': [2, 4]}, 'Wolf Pen Creek': {'Lofts @ Wolf Pen Creek - IB': [4, 27]}, 'Woodsman': {'Gridiron': [1, 35], 'Gateway': [2, 36]}, 'Yellow House': {'University Park': [1, 31], 'Renaissance Park': [1, -1]}, 'Z Islander': {'Reveille Ranch': [1, 15, 150]}}
    
    def dijkstras(graph,source,goal):
      Q = dict()
      for vertex in graph:
        Q[vertex] = [float("inf"),"UNDEFINED"]
      Q[source] = [0,"UNDEFINED"]
      
      trace = dict()
      stops = dict()
      previous = []
      
      while Q:
        u = min(Q, key=Q.get)
        u_dist = Q[u][0]
        u_prev = Q[u][1]
        del Q[u]
        
        if u == goal:
          S = []
          while u in trace:
            S.append(u)
            S.append(stops[u])
            u = trace[u]
          S.append(source)
          S.reverse()
          return S
        
        for v in graph[u]:
          if v in Q:
            alt = u_dist + graph[u][v][0]
            if alt < Q[v][0]:
              cur = graph[u][v][1:]
              proceed = True
              for bus in cur:
                if bus in previous or not previous:
                  Q[v] = [alt,u]
                  trace[v] = u
                  stops[v] = cur
                  previous = cur
                  proceed = False
                  break
              if proceed:
                Q[v] = [alt+2, u] # adds time for transfering busses 
                trace[v] = u
                stops[v] = cur
                previous = cur
    
    start1 = 'Not Available'
    start2 = 'Not Available'
    end1 = 'Not Available'
    end2 = 'Not Available'
    
    start1Min = float("inf")
    start2Min = float("inf")
    end1Min = float("inf")
    end2Min = float("inf")
    
    for i in range(len(stops)):
      start1Dist = ((stops[i][1] - startLat) ** 2 + (stops[i][2] - startLng) ** 2) ** 0.5
      end1Dist = ((stops[i][1] - endLat) ** 2 + (stops[i][2] - endLng) ** 2) ** 0.5
      if start1Dist < start1Min:
        start1 = stops[i][0]
        start1Min = start1Dist
      if end1Dist < end1Min:
        end1 = stops[i][0]
        end1Min = endDist
        
    for i in range(len(stops)):
      start2Dist = ((stops[i][1] - startLat) ** 2 + (stops[i][2] - startLng) ** 2) ** 0.5
      end2Dist = ((stops[i][1] - endLat) ** 2 + (stops[i][2] - endLng) ** 2) ** 0.5
      if start2Dist < start2Min and start2Dist > start1Min:
        start2 = stops[i][0]
        start2Min = start2Dist
      if end2Dist < end2Min and end2Dist > end1Min:
        end2 = stops[i][0]
        end2Min = end2Dist
    
    path1 = dijkstras(graph,start1,end1)
    path2 = dijkstras(graph,start2,end1)
    path3 = dijkstras(graph,start1,end2)
    path4 = dijkstras(grpah,start2,end2)
    
api.add_resource(Coordinates, '/coordinates/<string:stop>')
api.add_resource(Routes, '/routes/<string:startLat>/<string:startLng>/<string:endLat>/<string:endLng>')

if __name__=='__main__':
  app.run(debug=True)
    
