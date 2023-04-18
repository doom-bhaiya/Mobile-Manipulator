
from imageai.Detection import ObjectDetection

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath('retinanet arch resnet50 backbone.pth')
detector.loadModel()
import cv2
import time
import _thread
recyclable = ['Aluminum cans',
 'Batteries (rechargeable and non-rechargeable)',
 'Bicycle tires',
 'Books',
 'Cardboard boxes',
 'CDs and DVDs',
 'Cell phones',
 'Clothing (in good condition)',
 'Coffee cups (if they are made of paper)',
 'Computer equipment (e.g. monitors, keyboards, mice)',
 'Cooking oil',
 'Corks',
 'Egg cartons (made of paper or Styrofoam)',
 'Electronics',
 'Glass bottles and jars',
 'Ink cartridges',
 'Juice boxes and milk cartons',
 'Junk mail',
 'Magazines',
 'Metal cans',
 'Newspapers',
 'Office paper',
 'Packing peanuts (made of starch or corn)',
 "Paint (if it's not hazardous waste)",
 'Paper bags',
 'Paperboard boxes (e.g. cereal boxes)',
 'Plastic bottles and containers (e.g. shampoo bottles, water bottles)',
 'Printer paper',
 'Scrap metal',
 'Shoes (in good condition)',
 "Styrofoam (if it's clean and white)",
 'Tires (but not all recycling centers accept them)',
 'Toothbrushes (made of bamboo)',
 'Toys (in good condition)',
 "Wrapping paper (if it's not metallic or plastic)"]

Nonrecyclable = ['Ashes (from wood, charcoal, or coal)',
 'Baby wipes',
 'Batteries (hazardous waste)',
 'Broken glass (e.g. from a mirror)',
 'Candy wrappers',
 'Cigarette butts',
 'Cling wrap',
 'Compostable plastics (unless specified by recycling center)',
 'Diapers',
 'Disposable plates and cups (if they are made of plastic or Styrofoam)',
 'Electronics (if they cannot be recycled)',
 'Food contaminated paper',
 'Food waste (unless composted)',
 'Garden hoses',
 'Gasoline (hazardous waste)',
 'Greasy pizza boxes',
 'Hazardous waste (e.g. pesticides, fertilizers, motor oil)',
 'Incandescent light bulbs',
 'Kitty litter',
 'Medical waste (e.g. needles, syringes)',
 'Mirrors',
 'Napkins',
 'Oil filters',
 "Paint (if it's hazardous waste)",
 'Paper towels',
 'Plastic bags (unless specified by recycling center)',
 'Plastic cutlery',
 'Plastic film (e.g. bubble wrap)',
 'Plastic six-pack rings',
 'Polystyrene foam (e.g. foam cups, foam food containers)',
 'Propane tanks (unless specified by recycling center)',
 'Rubber bands',
 'Single-use plastic items (e.g. straws, stirrers)',
 "Styrofoam (if it's not clean and white)",
 'Tissues',
 'Toothbrushes (made of plastic)',
 'Used tissues',
 'Vacuum cleaner bags',
 'Wax paper',
 'Wet paper',
 'Window glass',
 'Wire hangers',
 'Wood treated with chemicals (e.g. pressure-treated wood)',
 'Worn-out clothing',
 "Wrapping paper (if it's metallic or plastic)",
 'Yoga mats']



def videostream():
    cap = cv2.VideoCapture(0) 
    counter = 0
    while(True):
        ret, frame = cap.read() 
        cv2.imshow('frame', frame)
        #cv2.imwrite('originalimage.jpg',frame)
        detection = detector.detectObjectsFromImage(
        input_image=frame,
        #r'C:\Users\Vaikunth Guruswamy\Downloads\archive\originalimage.jpg',
        output_type='array',
        minimum_percentage_probability=30
        )
        print(detection[1]) 
        # if counter ==10 :
        #     _thread.start_new_thread(detect,(frame,counter,))
        #     time.sleep(3)
        #     counter=0
        # else:
        #     counter+=1
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    cap.release()
    cv2.destroyAllWindows()

def detect(frame,name=2):
    #cv2.imwrite('originalimage'+str(name)+'.jpg',frame)
    detection = detector.detectObjectsFromImage(
    input_image=frame,
    #r'C:\Users\Vaikunth Guruswamy\Downloads\archive\originalimage'+str(name)+'.jpg',
    output_type='array',
    minimum_percentage_probability=30
    )
    
    print(detection[1])
    return(detection[1])

videostream()
